#!/usr/bin/env python3
"""Render repository research manuscripts as formal, date-free PDF documents."""
from pathlib import Path
import html
import re
from urllib.parse import quote
import markdown2
from bs4 import BeautifulSoup
from weasyprint import HTML

REPO=Path(__file__).resolve().parents[2]
CSS=r"""
@page { size: A4; margin: 20mm 21mm 21mm; @bottom-right {
 content: counter(page); color:#000; font-size:9pt; font-family:Inter;
}}
@page:first { margin:0; @bottom-right {content:none} }
* {box-sizing:border-box}
html, body {margin:0; padding:0}
body {font-family:Inter, sans-serif; font-size:10.5pt; color:#000;
 line-height:1.48; font-weight:400}
.cover {width:210mm; height:297mm; padding:24mm;
 display:flex; align-items:center; justify-content:center;
 page-break-after:always}
.cover-box {border:0.45pt solid #000; width:100%; height:100%;
 display:flex; flex-direction:column; align-items:center;
 justify-content:center; padding:25mm; text-align:center}
.cover h1 {font-size:24pt; line-height:1.19; font-weight:700; color:#000;
 text-transform:uppercase; margin:0 0 16mm}
.cover .subtitle {font-size:13pt; line-height:1.3; margin:0 0 23mm; font-weight:400}
.cover .author {font-size:11.5pt; font-weight:600; margin:0}
.toc {page-break-after:always; padding-top:7mm}
.toc h2 {font-size:16pt; color:#000; letter-spacing:.02em; margin-bottom:15mm}
.toc p {margin:0 0 4.7mm; font-size:11pt}
.toc a {color:#000; text-decoration:none; display:block}
.toc a::after {content:leader('.') target-counter(attr(href), page); float:right}
.paper h2 {font-size:13pt; font-weight:700; color:#000; margin:8mm 0 3mm;
 break-after:avoid}
.paper h3 {font-size:11pt; font-weight:600; color:#2C5472;
 margin:5mm 0 2mm; break-after:avoid}
.paper p {margin:0 0 3.5mm; text-align:justify; orphans:3; widows:3}
.paper ul,.paper ol {margin:0 0 4mm 5mm; padding-left:5mm}
.paper li {margin-bottom:1.5mm}
.paper strong {font-weight:700}
.paper table {border-collapse:collapse; width:100%; margin:4.5mm 0;
 font-size:8.7pt; break-inside:avoid}
.paper th {background:#DDEBF6; color:#000; font-weight:700;
 text-align:left; border:0.5pt solid #a9b6bd; padding:2.4mm}
.paper td {border:0.5pt solid #a9b6bd; padding:2mm; vertical-align:top}
.paper img {max-width:100%; max-height:105mm; object-fit:contain}
.paper figure {text-align:center; margin:4mm 0 5mm; break-inside:avoid}
.paper figcaption {font-size:8.5pt; color:#000; text-align:left; margin:2mm 0}
.paper pre {font-family:monospace; font-size:8.6pt; white-space:pre-wrap;
 background:#f9f9f9; padding:3mm}
.paper code {font-size:.93em}
.paper a {color:#000; text-decoration:underline}
.paper blockquote {margin-left:8mm; border-left:0.4pt solid #555; padding-left:4mm}
.paper #references {break-before:page; margin-top:0}
.paper #references~p {font-size:9pt; text-align:left; margin-bottom:3mm}
.paper hr {display:none}
"""
def extract(txt):
    lines=txt.splitlines()
    title=next((x[2:].strip() for x in lines if x.startswith("# ")), "Research paper")
    start=next((i for i,x in enumerate(lines) if x.startswith("# ")),0)
    sub,author="","Amogelang R. Pelo"
    for line in lines[start+1:start+12]:
        z=line.strip()
        if z.startswith("## "):break
        if z.startswith("**") and z.endswith("**"):
            v=z.strip("*").strip()
            if v.startswith(("A ","An ")) and not sub:sub=v
            if "Pelo" in v:author=re.sub(r"^Author:\s*","",v)
    # Do not carry over any document-preparation date or old TOC.
    begin=re.search(r"(?im)^##\s+Abstract\s*$",txt)
    if begin:
        body=txt[begin.start():]
    else:
        first=re.search(r"(?m)^##\s+",txt)
        body=txt[first.start():] if first else txt
    body=re.sub(r"\s*\(Accessed:\s*\d{1,2}\s+[A-Za-z]+\s+\d{4}\)","",body)
    body=re.sub(r"(?im)^\s*\*\*Date:\*\*.*$","",body)
    body=re.sub(r"(?im)^\s*\*\*Analysis performed:\*\*.*$","",body)
    return title,sub,author,body
def render(src):
    title,sub,author,body=extract(src.read_text(encoding="utf-8"))
    body_html=markdown2.markdown(body,extras=["tables","fenced-code-blocks","header-ids","strike"])
    soup=BeautifulSoup(body_html,"html.parser")
    headings=[]
    used=set()
    for h in soup.find_all(["h2","h3"]):
        raw=h.get_text(" ",strip=True)
        anchor=re.sub("[^a-z0-9]+","-",raw.lower()).strip("-")
        if not anchor:anchor="section"
        base=anchor
        j=2
        while anchor in used:anchor=base+"-"+str(j); j+=1
        h["id"]=anchor;used.add(anchor)
        if h.name=="h2":headings.append((raw,anchor))
    cover=(f'<section class="cover"><div class="cover-box">'
      f'<h1>{html.escape(title)}</h1>'
      f'<p class="subtitle">{html.escape(sub)}</p>'
      f'<p class="author">{html.escape(author)}</p></div></section>')
    toc='<section class="toc"><h2>TABLE OF CONTENTS</h2>'+''.join(
      f'<p><a href="#{html.escape(anchor)}">{html.escape(label)}</a></p>'
      for label,anchor in headings)+'</section>'
    doc=('<!doctype html><html><head><meta charset="utf-8"><style>'
         +CSS+'</style></head><body>'+cover+toc
         +'<main class="paper">'+str(soup)+'</main></body></html>')
    out=src.with_suffix(".pdf")
    HTML(string=doc,base_url=src.parent.as_uri()+"/").write_pdf(out)
    print("CREATED",out.relative_to(REPO),out.stat().st_size)
if __name__=="__main__":
    import sys
    targets=[Path(a) for a in sys.argv[1:]] if len(sys.argv)>1 else list(REPO.rglob("RESEARCH_PAPER.md"))
    for target in targets:
        if ".git" not in target.parts:render(target)
