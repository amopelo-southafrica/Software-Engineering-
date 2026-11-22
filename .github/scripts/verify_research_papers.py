#!/usr/bin/env python3
"""Report research manuscript pagination and detect papers outside the body-length target."""
from pathlib import Path
import re
from pypdf import PdfReader

for file in sorted(Path(".").rglob("RESEARCH_PAPER.pdf")):
    if ".git" in file.parts:
        continue
    reader = PdfReader(str(file))
    all_pages = [p.extract_text() or "" for p in reader.pages]
    refs_index = next(
        (i for i, content in enumerate(all_pages[2:], start=2)
         if re.search(r"(?im)^\\s*References\\s*$", content)),
        None,
    )
    # Cover and TOC are each one page; references begin at refs_index.
    body = refs_index - 2 if refs_index is not None else len(all_pages) - 3
    print(f"{file}: total={len(all_pages)}, research_body={body}, reference_starts={refs_index+1 if refs_index is not None else 'unknown'}")
    if body < 5 or body > 10:
        print(f"WARNING: {file} is outside the requested 5-10 body pages")
