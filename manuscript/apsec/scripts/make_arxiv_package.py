#!/usr/bin/env python3
"""Build the arXiv submission package for the accepted APSEC 2026 paper.

arXiv compiles the sources it receives and does *not* run BibTeX, so the package
ships the .bbl. The author block, which lives outside version control in
authors_apsec.tex, is inlined: the arXiv version is public and named. A footnote
records the acceptance and the IEEE copyright notice, as the IEEE author posting
policy requires for an author's accepted version.

Run from the repository root or from manuscript/:  make apsec-arxiv
Output: manuscript/apsec/arxiv/ with the sources, the compiled PDF and the
tar.gz to upload.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tarfile
from pathlib import Path

APSEC = Path(__file__).resolve().parent.parent
OUT = APSEC / "arxiv"
NOTE = (
    r"\thanks{Accepted at the 33rd Asia-Pacific Software Engineering Conference "
    r"(APSEC 2026), Software Engineering in Practice track, Bali, Indonesia, "
    r"7--10 December 2026. This is the authors' accepted version. "
    r"\copyright~2026 IEEE. Personal use of this material is permitted. Permission from "
    r"IEEE must be obtained for all other uses, in any current or future media, including "
    r"reprinting/republishing this material for advertising or promotional purposes, creating "
    r"new collective works, for resale or redistribution to servers or lists, or reuse of any "
    r"copyrighted component of this work in other works.}"
)


def build() -> Path:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    # 1. Sources, with the author block inlined and the acceptance footnote added.
    authors_file = APSEC / "authors_apsec.tex"
    if not authors_file.exists():
        sys.exit("authors_apsec.tex is missing: the arXiv version must carry the author block.")
    authors = "\n".join(
        line for line in authors_file.read_text(encoding="utf-8").splitlines()
        if not line.lstrip().startswith("%")
    ).strip()

    tex = (APSEC / "main_apsec.tex").read_text(encoding="utf-8")
    block = re.search(r"\\author\{%.*?\n\}\n", tex, re.S)
    if not block:
        sys.exit("could not find the \\author{...} block in main_apsec.tex")
    tex = tex.replace(block.group(0), "\\author{%\n" + authors + "%\n}\n")

    title = re.search(r"(\\title\{.*?)\}\n", tex, re.S)
    if not title:
        sys.exit("could not find \\title{...}")
    tex = tex.replace(title.group(0), title.group(1) + NOTE + "}\n")

    (OUT / "main.tex").write_text(tex, encoding="utf-8")

    # 2. Everything the sources need.
    for name in ("IEEEtran.cls", "IEEEtran.bst", "etc.sty", "references.bib"):
        shutil.copy2(APSEC / name, OUT / name)
    figures = OUT / "figures"
    figures.mkdir()
    for fig in sorted((APSEC / "figures").iterdir()):
        if fig.suffix.lower() in {".png", ".pdf", ".jpg"}:
            shutil.copy2(fig, figures / fig.name)

    # 3. Compile once to produce the .bbl arXiv needs, then keep it next to the sources.
    subprocess.run(
        ["latexmk", "-pdf", "-interaction=nonstopmode", "-file-line-error", "main.tex"],
        cwd=OUT, check=True, capture_output=True,
    )
    log = (OUT / "main.log").read_text(encoding="utf-8", errors="replace")
    errors = [line for line in log.splitlines() if line.startswith("!")]
    if errors:
        sys.exit("LaTeX errors in the arXiv build:\n" + "\n".join(errors[:5]))

    # 4. The tarball: sources, class and style files, figures, and the .bbl. No logs.
    keep = {"main.tex", "main.bbl", "IEEEtran.cls", "IEEEtran.bst", "etc.sty", "references.bib"}
    tarball = OUT / "vera-apsec2026-arxiv.tar.gz"
    with tarfile.open(tarball, "w:gz") as tar:
        for name in sorted(keep):
            tar.add(OUT / name, arcname=name)
        for fig in sorted(figures.iterdir()):
            tar.add(fig, arcname=f"figures/{fig.name}")

    for junk in OUT.glob("main.*"):
        if junk.suffix not in {".tex", ".bbl", ".pdf"}:
            junk.unlink()
    return tarball


if __name__ == "__main__":
    tarball = build()
    pdf = OUT / "main.pdf"
    size = tarball.stat().st_size / 1024
    print(f"arXiv package: {tarball.relative_to(APSEC.parent.parent)} ({size:.0f} KB)")
    print(f"compiled PDF:  {pdf.relative_to(APSEC.parent.parent)}")
    print("Upload the tar.gz at arxiv.org/submit; see apsec/ARXIV_SUBMISSION.md.")
