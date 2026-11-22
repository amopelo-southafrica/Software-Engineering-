"""Verified supplementary bookstore application using SQLite and Python's standard library.

This is a portfolio extension, NOT the original HyperionDev source submission.
Run: python shelf_track_verified.py --seed
Test: python -m unittest discover -s tests -v
"""
from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path
from typing import Any


AUTHORS = [
    (1290, "Charles Dickens", "England"),
    (8937, "J.K. Rowling", "England"),
    (2356, "C.S. Lewis", "Ireland"),
    (6380, "J.R.R. Tolkien", "South Africa"),
    (5620, "Lewis Carroll", "England"),
]
BOOKS = [
    (3001, "A Tale of Two Cities", 1290, 30),
    (3002, "Harry Potter and the Philosophers Stone", 8937, 40),
    (3003, "The Lion, the Witch and the Wardrobe", 2356, 25),
    (3004, "The Lord of the Rings", 6380, 37),
    (3005, "Alices Adventures in Wonderland", 5620, 12),
]


def connect_database(path: str | Path = "ebookstore.db") -> sqlite3.Connection:
    conn = sqlite3.connect(str(path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def initialise_database(conn: sqlite3.Connection) -> None:
    """Create related tables with minimum data-integrity constraints."""
    conn.execute("PRAGMA foreign_keys = ON")
    with conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS author (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL CHECK(length(trim(name)) > 0),
                country TEXT NOT NULL CHECK(length(trim(country)) > 0)
            )
            """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS book (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL UNIQUE CHECK(length(trim(title)) > 0),
                authorID INTEGER NOT NULL
                    REFERENCES author(id) ON DELETE RESTRICT,
                qty INTEGER NOT NULL CHECK(qty >= 0)
            )
            """
        )


def seed_example_records(conn: sqlite3.Connection) -> None:
    """Seed the original project's example records without replacing existing rows."""
    with conn:
        conn.executemany(
            "INSERT OR IGNORE INTO author (id, name, country) VALUES (?, ?, ?)",
            AUTHORS,
        )
        conn.executemany(
            "INSERT OR IGNORE INTO book (id, title, authorID, qty) VALUES (?, ?, ?, ?)",
            BOOKS,
        )


def _positive_id(value: int | str, label: str) -> int:
    try:
        parsed = int(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{label} must be an integer") from exc
    if parsed < 1:
        raise ValueError(f"{label} must be a positive integer")
    return parsed


def _quantity(value: int | str) -> int:
    try:
        parsed = int(value)
    except (TypeError, ValueError) as exc:
        raise ValueError("Quantity must be a whole number") from exc
    if parsed < 0:
        raise ValueError("Quantity cannot be negative")
    return parsed


def _nonempty(value: str, field: str) -> str:
    cleaned = str(value).strip()
    if not cleaned:
        raise ValueError(f"{field} cannot be blank")
    return cleaned


def list_books(conn: sqlite3.Connection) -> list[dict[str, Any]]:
    rows = conn.execute(
        """
        SELECT b.id, b.title, b.authorID, a.name AS author,
               a.country, b.qty
          FROM book AS b
          JOIN author AS a ON b.authorID = a.id
         ORDER BY a.name COLLATE NOCASE, b.title COLLATE NOCASE
        """
    ).fetchall()
    return [dict(row) for row in rows]


def search_books(conn: sqlite3.Connection, phrase: str) -> list[dict[str, Any]]:
    """Case-insensitive substring search; never concatenate input into SQL."""
    query = _nonempty(phrase, "Search term")
    rows = conn.execute(
        """
        SELECT b.id, b.title, b.authorID, a.name AS author,
               a.country, b.qty
          FROM book AS b
          JOIN author AS a ON b.authorID = a.id
         WHERE instr(lower(b.title), lower(?)) > 0
            OR instr(lower(a.name), lower(?)) > 0
         ORDER BY b.title COLLATE NOCASE
        """,
        (query, query),
    ).fetchall()
    return [dict(row) for row in rows]


def add_book(
    conn: sqlite3.Connection, title: str, author_id: int, quantity: int
) -> int:
    """Return new book ID. Foreign keys and uniqueness are checked by SQLite."""
    title = _nonempty(title, "Title")
    author_id = _positive_id(author_id, "Author ID")
    quantity = _quantity(quantity)
    with conn:
        cursor = conn.execute(
            "INSERT INTO book (title, authorID, qty) VALUES (?, ?, ?)",
            (title, author_id, quantity),
        )
    return int(cursor.lastrowid)


def update_book(
    conn: sqlite3.Connection,
    book_id: int,
    *,
    title: str | None = None,
    author_id: int | None = None,
    quantity: int | None = None,
) -> bool:
    """Update selected fields by stable book ID; return False for missing IDs."""
    book_id = _positive_id(book_id, "Book ID")
    fields: list[str] = []
    values: list[Any] = []
    if title is not None:
        fields.append("title = ?")
        values.append(_nonempty(title, "Title"))
    if author_id is not None:
        fields.append("authorID = ?")
        values.append(_positive_id(author_id, "Author ID"))
    if quantity is not None:
        fields.append("qty = ?")
        values.append(_quantity(quantity))
    if not fields:
        raise ValueError("Provide at least one field to update")
    values.append(book_id)
    with conn:
        result = conn.execute(
            f"UPDATE book SET {', '.join(fields)} WHERE id = ?", values
        )
    return result.rowcount > 0


def delete_book(conn: sqlite3.Connection, book_id: int) -> bool:
    book_id = _positive_id(book_id, "Book ID")
    with conn:
        result = conn.execute("DELETE FROM book WHERE id = ?", (book_id,))
    return result.rowcount > 0


def update_author(
    conn: sqlite3.Connection,
    author_id: int,
    *,
    name: str | None = None,
    country: str | None = None,
) -> bool:
    author_id = _positive_id(author_id, "Author ID")
    fields: list[str] = []
    values: list[Any] = []
    if name is not None:
        fields.append("name = ?")
        values.append(_nonempty(name, "Author name"))
    if country is not None:
        fields.append("country = ?")
        values.append(_nonempty(country, "Country"))
    if not fields:
        raise ValueError("Provide at least one author field to update")
    values.append(author_id)
    with conn:
        result = conn.execute(
            f"UPDATE author SET {', '.join(fields)} WHERE id = ?", values
        )
    return result.rowcount > 0


def _print_books(rows: list[dict[str, Any]]) -> None:
    if not rows:
        print("No matching books found.")
        return
    for book in rows:
        print(
            f"[{book['id']}] {book['title']} | "
            f"{book['author']} ({book['country']}) | Stock: {book['qty']}"
        )


def _optional_int(prompt: str) -> int | None:
    entered = input(prompt).strip()
    return int(entered) if entered else None


def run_menu(conn: sqlite3.Connection) -> None:
    """Console interface; all SQL and validation lives in testable functions."""
    while True:
        print(
            "\nBOOKSTORE DATABASE\n"
            "1. Add book\n"
            "2. Update book\n"
            "3. Delete book\n"
            "4. Search title or author\n"
            "5. View all books\n"
            "6. Update author\n"
            "0. Exit"
        )
        choice = input("Option (0-6): ").strip()
        try:
            if choice == "0":
                print("Goodbye.")
                return
            if choice == "1":
                title = input("Title: ")
                author_id = int(input("Existing author ID: "))
                qty = int(input("Quantity: "))
                new_id = add_book(conn, title, author_id, qty)
                print(f"Book {new_id} added.")
            elif choice == "2":
                book_id = int(input("Book ID: "))
                title = input("New title (blank to keep): ").strip() or None
                author_id = _optional_int("New author ID (blank to keep): ")
                qty = _optional_int("New quantity (blank to keep): ")
                changed = update_book(
                    conn, book_id, title=title, author_id=author_id, quantity=qty
                )
                print("Book updated." if changed else "Book not found.")
            elif choice == "3":
                book_id = int(input("Book ID: "))
                confirmation = input("Type DELETE to confirm: ").strip()
                if confirmation == "DELETE":
                    print(
                        "Book deleted."
                        if delete_book(conn, book_id)
                        else "Book not found."
                    )
                else:
                    print("Deletion cancelled.")
            elif choice == "4":
                _print_books(search_books(conn, input("Title or author: ")))
            elif choice == "5":
                _print_books(list_books(conn))
            elif choice == "6":
                author_id = int(input("Author ID: "))
                name = input("New author name (blank to keep): ").strip() or None
                country = input("New country (blank to keep): ").strip() or None
                changed = update_author(conn, author_id, name=name, country=country)
                print("Author updated." if changed else "Author not found.")
            else:
                print("Invalid option.")
        except (ValueError, sqlite3.IntegrityError) as exc:
            print(f"Operation cancelled: {exc}")


def main() -> None:
    parser = argparse.ArgumentParser(description="SQLite bookstore CLI")
    parser.add_argument("--database", default="ebookstore.db")
    parser.add_argument(
        "--seed", action="store_true",
        help="Insert initial demonstration books and authors if missing",
    )
    args = parser.parse_args()
    conn = connect_database(args.database)
    try:
        initialise_database(conn)
        if args.seed:
            seed_example_records(conn)
        run_menu(conn)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
