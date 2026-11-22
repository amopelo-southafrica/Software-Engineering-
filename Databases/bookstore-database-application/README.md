# Bookstore Database Application

This portfolio project examines a Python and SQLite bookstore inventory program originally submitted as a software-engineering task. It includes **both original project versions** and a separately labelled supplementary implementation with automated tests.

## Project files

- [`shelf_track.py`](shelf_track.py): portfolio script reflecting the original task, including known functional limitations.
- [`shelf_track_original.py`](shelf_track_original.py): preserved earlier submitted script.
- [`shelf_track_verified.py`](shelf_track_verified.py): **supplementary refactored implementation**, not part of the original submission.
- [Unit tests](tests/test_shelf_track_verified.py): 10 SQLite tests, run automatically via GitHub Actions.
- [Research paper](RESEARCH_PAPER.md): source-code review, relational design, observed defects and evidence of test coverage.
- [Research PDF](RESEARCH_PAPER.pdf): generated automatically from the paper.

The original files are retained for provenance, not represented as fully functional applications. The supplementary version has an explicit author/book relationship, safe SQL parameters, record validation, transactions and a menu loop.

## Run the verified implementation

Python 3.10 or newer; no third-party dependencies.

```bash
python shelf_track_verified.py --seed
```

This creates/opens `ebookstore.db` in the current directory and inserts the five example book records **only if they are missing**. For a different database path:

```bash
python shelf_track_verified.py --database /path/to/store.db --seed
```

Without `--seed`, the database schema is created but demonstration records are not inserted.

To run the automated tests:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

GitHub's **Test bookstore SQLite extension** workflow has successfully executed all 10 tests in the hosted runner. This establishes the tested operations but is **not** production-level security, concurrency or deployment validation.

## Main design corrections

| Original code risk | Treatment in supplementary version |
|:--|:--|
| Some inserted books omit their author ID | Required author foreign key |
| Delete does not commit | Transactional deletion |
| Search can return no visible result | Search displays matching rows |
| Author-edit SQL references nonexistent columns | Author update targets `author` table |
| Only one top-level menu action | Repeating CLI menu until exit |
| Missing/invalid quantity constraints | Nonnegative quantity checks |
| Record modification by title | Update/delete by unique book ID |
| No automated verification | 10 repeatable tests |

The sample catalogue and metadata are demonstration inputs, not audited commercial inventory. This is a local command-line application, not a network service with authentication or role-based authorisation.
