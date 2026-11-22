"""Tests for the supplementary verified SQLite implementation (not the original task)."""
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from shelf_track_verified import (  # noqa: E402
    add_book,
    connect_database,
    delete_book,
    initialise_database,
    list_books,
    search_books,
    seed_example_records,
    update_author,
    update_book,
)


class BookstoreTests(unittest.TestCase):
    def setUp(self):
        self.conn = connect_database(":memory:")
        initialise_database(self.conn)
        seed_example_records(self.conn)

    def tearDown(self):
        self.conn.close()

    def test_seed_has_five_books_with_authors(self):
        rows = list_books(self.conn)
        self.assertEqual(len(rows), 5)
        self.assertEqual(sum(row["qty"] for row in rows), 144)
        self.assertTrue(all(row["author"] and row["title"] for row in rows))

    def test_seed_is_idempotent(self):
        seed_example_records(self.conn)
        self.assertEqual(len(list_books(self.conn)), 5)

    def test_create_and_find_book_by_title_or_author(self):
        new_id = add_book(self.conn, "New Python Book", 1290, 9)
        self.assertEqual(
            [r["id"] for r in search_books(self.conn, "python")], [new_id]
        )
        self.assertTrue(any(r["id"] == new_id for r in search_books(self.conn, "dickens")))

    def test_quantity_update_and_delete_by_id(self):
        self.assertTrue(update_book(self.conn, 3001, quantity=0))
        match = [x for x in list_books(self.conn) if x["id"] == 3001][0]
        self.assertEqual(match["qty"], 0)
        self.assertTrue(delete_book(self.conn, 3001))
        self.assertEqual(len(list_books(self.conn)), 4)
        self.assertFalse(delete_book(self.conn, 3001))

    def test_author_update_and_join(self):
        self.assertTrue(update_author(self.conn, 1290, country="United Kingdom"))
        self.assertEqual(
            search_books(self.conn, "two cities")[0]["country"], "United Kingdom"
        )

    def test_invalid_quantities_are_rejected(self):
        with self.assertRaises(ValueError):
            add_book(self.conn, "Invalid book", 1290, -1)
        with self.assertRaises(ValueError):
            update_book(self.conn, 3001, quantity=-20)
        self.assertEqual(len(list_books(self.conn)), 5)

    def test_invalid_author_violates_foreign_key(self):
        with self.assertRaises(sqlite3.IntegrityError):
            add_book(self.conn, "Orphan book", 999999, 2)
        self.assertEqual(len(list_books(self.conn)), 5)

    def test_missing_ids_and_empty_updates(self):
        self.assertFalse(update_book(self.conn, 9999, quantity=1))
        with self.assertRaises(ValueError):
            update_book(self.conn, 3001)
        self.assertFalse(update_author(self.conn, 999999, name="Missing"))
        with self.assertRaises(ValueError):
            search_books(self.conn, "   ")

    def test_search_is_parameterised(self):
        self.assertEqual(search_books(self.conn, "' OR 1=1 --"), [])
        self.assertEqual(len(list_books(self.conn)), 5)

    def test_commits_survive_new_connection(self):
        with tempfile.TemporaryDirectory() as tmp:
            file_path = Path(tmp) / "store.db"
            first = connect_database(file_path)
            try:
                initialise_database(first)
                seed_example_records(first)
                delete_book(first, 3001)
            finally:
                first.close()
            second = connect_database(file_path)
            try:
                self.assertEqual(len(list_books(second)), 4)
            finally:
                second.close()


if __name__ == "__main__":
    unittest.main()
