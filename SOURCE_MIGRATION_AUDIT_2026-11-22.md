# HyperionDev portfolio migration audit — 22 November 2026

## Source and explicit exclusions

Source: private `hyperiondev-bootcamps/AP25070018785` repository (841 files on the `main` tree at this audit).

Target repositories:
- [AI Engineering and Research](https://github.com/amopelo-southafrica/AI-Engineering-and-Research)
- [Mathematics and Statistics](https://github.com/amopelo-southafrica/Mathematics-and-Statistics)
- [Software Engineering](https://github.com/amopelo-southafrica/Software-Engineering-)

The owner's **precise November 22 exclusions** are: **Django Sticky Notes Application Part One; eCommerce Application Part Two; Capstone Project Consolidation; mastering sequential models; the neural-networks capstone; and every Level 4 Python Programme project.** These projects should not be restored. **eCommerce Application Part One is permitted**, and its original ZIP is already in the Software Engineering portfolio.

Exclude generated `venv`, `__pycache__` and `.git` folders from project uploads. Many source files are instructor examples, course PDFs or vendor content and should not be republished as original student work.

## Selected source-file comparison

I selected 128 likely submission-related files from Levels 1–3 by file type and path, excluding numbered course PDF handouts, examples, the named sequential/neural tasks, eCommerce paths and Level 4. This selection is deliberately **not** all 841 source files.

I compared the Git blob SHA of each selected source file against **all three destination trees**, which detects exact byte-for-byte copies even after files are renamed.

| Metric | Number |
|:--|--:|
| Source files in entire repository | 841 |
| Files in this selected audit inventory | 128 |
| Exact source-content matches in destinations | 104 |
| No exact SHA match located | 24 |
| Of those 24, expressly excluded by the user | 16 |
| Remaining unmatched candidates requiring review/upload | 8 |

A hash mismatch does **not** necessarily mean an omitted project: a source file may have been intentionally rewritten, converted or extracted into several destination files.

## The 16 unmatched source files intentionally excluded

- **15** loose code/template files and ZIPs under `Level 2 - Software Engineering/M06T04 – Django – Sticky Notes Application Part 1`.
- **1** notebook under `Level 3 - Data Science/M12T07 – Capstone Project – Neural Networks`.

Those entries remain out of scope under the owner's instructions. The other named exclusions were already removed by this audit's initial selection filters.

## Eight remaining unmatched eligible-file candidates

| Source category | Number | Disposition |
|:--|--:|:--|
| `tasks.txt`, `user.txt`, `user_overview.txt` in Level 1 Task Manager capstone | 3 | Do not automatically publish a user-record file: `user.txt` has two-field records consistent with username/credential pairs; inspect and redact first |
| Version-control screenshot, static-deployment screenshot and `my_cv.png` | 3 | Inspect for personal information, contacts, identifiers and unintended exposure before copying to public repositories |
| `taskmanager.zip` under M06T03 OOP Modules | 1 | 12,291,901-byte original archive; requires inspection and removal of generated dependencies/venv if present |
| `news_project.zip` under M06T08 News Application | 1 | 25,678,933-byte original archive; **in scope** (distinct from excluded Capstone Project Consolidation), but requires inspection and removal of generated dependencies/venv if present |
| **Total** | **8** | |

The original source repository is private, whereas the portfolio repositories are public. Replicating files with possible account credentials, personal details or embedded generated dependencies without inspection would be inappropriate.

The connected GitHub tool returned no content for the original 12.3 MB binary ZIP through its content endpoint, and the blob endpoint could not decode the archive as text. Thus the present workflow **could not inspect or directly upload those large original ZIPs safely**. They remain genuinely unfinished, not silently marked complete.

## Verified uploads and research deliverables

- Original Docker project archive restored to [Docker exercise](Web-Systems-and-Delivery/containerising-applications-with-docker/dockerfolder-original.zip), with source and destination Git SHA `a3ecd70eb901a5fa31472b0c92419713f3267312` matching.
- Original eCommerce Part One archive present at [eCommerce architecture](Web-Systems-and-Delivery/django-ecommerce-architecture/ecommerce-store-part-one-original.zip); Part Two remains excluded.
- Bookstore original scripts preserved, while a separate [verified SQLite implementation](Databases/bookstore-database-application/shelf_track_verified.py) passes 10 automated tests.
- Markdown research papers and generated PDFs indexed in all three portfolio READMEs.

## Outstanding work

1. Inspect and recover the **two permitted large ZIP archives**, ideally outside this restricted binary-read connector, and remove any `venv`, dependency cache, source secrets or generated noise before uploading.
2. Inspect and sanitise Level 1 task user data and the three screenshots before any public upload. The source content may need to be replaced by safe example fixtures rather than copied verbatim.
3. Conduct a broader **file-by-file** assessment of remaining course materials and authored deliverables that the selected-file filters deliberately did not cover.
4. Reconcile folders and aliases after confirming the final set of included projects. No additional project folders were renamed in this pass.

**Current status:** substantially migrated and documented, but not fully complete. The 104 exact matches describe the selected source-file audit, not 104 complete projects and not 104 out of all 841 files.
