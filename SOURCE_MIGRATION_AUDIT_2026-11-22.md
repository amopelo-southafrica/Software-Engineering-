# HyperionDev portfolio migration audit — 22 November 2026

## Scope and method

**Source repository:** [hyperiondev-bootcamps/AP25070018785](https://github.com/hyperiondev-bootcamps/AP25070018785)

**Destination portfolios:**
- [AI Engineering and Research](https://github.com/amopelo-southafrica/AI-Engineering-and-Research)
- [Mathematics and Statistics](https://github.com/amopelo-southafrica/Mathematics-and-Statistics)
- [Software Engineering](https://github.com/amopelo-southafrica/Software-Engineering-)

The complete source `main` tree contained **841 files** at the audit time. This is **not** a claim that 841 files should be republished. Many are training handouts, examples, website assets, duplicates, or materials that the owner asked to exclude.

I made a **selected source-file inventory** of 128 non-curriculum candidates from Levels 1–3, prioritising `.py`, `.ipynb`, `.csv`, `.txt`, `.zip` and certain other useful formats. The inventory deliberately omitted files in common training/example folders, numbered PDF handouts, Level 4 Python work, the named sequential/neural capstones and e-commerce projects.

A comparison of **Git blob SHA hashes** against the three destination repository trees found:

| Selected-file inventory check | Count |
|:--|--:|
| Candidates in the scoped inventory | 128 |
| Exact content matches in destination portfolios | 104 |
| No matching blob hash located | 24 |

Hash equality verifies that a source file's bytes are present in at least one destination, even if its filename or directory changed. A nonmatch **does not always prove a missing submission**, because the destination may contain an edited, converted or extracted version.

## Remaining unmatched files requiring explicit classification

| Category | Count | Assessment |
|:--|--:|:--|
| Django Sticky Notes Part One source and archives | 15 | Do not mirror until the earlier Django exclusions are resolved; related portfolio folder exists |
| Task Manager capstone text data (`tasks.txt`, `user.txt`, `user_overview.txt`) | 3 | Inspect/redact before any public upload; may include identifiers, account records or credentials |
| Git/deployment screenshots, including a CV image | 3 | Do not publish without checking private personal content |
| `taskmanager.zip` from OOP Modules | 1 | Large original archive (~12.3 MB); inspect contents, license and duplication before migration |
| `news_project.zip` Django capstone archive | 1 | Large original archive (~25.7 MB); inspect and confirm exclusion status before migration |
| Neural-networks capstone notebook | 1 | Intentionally out of scope under the user's stated exclusions |
| **Total** | **24** | |

The 15 Django entries include loose Python and HTML source, a test file, and two archived app versions. They should not be treated as automatically authorised for copying, particularly given the prior exclusion of specific Django and e-commerce work.

## Completed work verified during this pass

- Restored the original `dockerfolder.zip` to [the Docker portfolio](Web-Systems-and-Delivery/containerising-applications-with-docker/dockerfolder-original.zip); source and destination Git blob SHA both equal `a3ecd70eb901a5fa31472b0c92419713f3267312`.
- Preserved the original source archive and instructions separately from later research or refactoring.
- Added research indexing to all three repository READMEs, with links to available Markdown papers and PDFs.
- Verified that the [SQLite bookstore supplementary implementation](Databases/bookstore-database-application/) passes ten automated tests; its original submissions remain preserved.

## Limitations and final reconciliation tasks

1. **Scope confirmation:** Resolve which Django, e-commerce and news archives are intentionally excluded, rather than silently publishing them.
2. **Sensitive-file inspection:** Review task-manager user data and screenshots before any migration to these public repositories.
3. **Large-archive evaluation:** Determine whether `taskmanager.zip` and `news_project.zip` contain meaningful source work or large dependency/vendor directories.
4. **Completeness:** This SHA-based shortlist is **not a full manual audit of every one of the source's 841 files**, and omitted instructional/example files were not exhaustively classified.
5. **Folder renaming:** No additional directory names were changed during this audit. Confirm final naming conventions after inclusion/exclusion decisions.

The audit supports an accurate status statement: **the selected portfolio already contains substantial exact source copies, but full migration completion is not yet established**.
