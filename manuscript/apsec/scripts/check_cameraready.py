#!/usr/bin/env python3
"""Check an APSEC 2026 camera-ready PDF against the instructions in the acceptance mail.

Checks the page size is A4, that every font is embedded, and reports the page
count. Run through `make apsec-cameraready`.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

A4_PT = (595, 842)


def main(pdf: Path) -> int:
    if not pdf.exists():
        print(f"missing {pdf}")
        return 2
    findings = []

    if shutil.which("pdfinfo"):
        out = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
        size = re.search(r"Page size:\s+([\d.]+) x ([\d.]+) pts", out)
        pages = re.search(r"Pages:\s+(\d+)", out)
        if size:
            dims = (round(float(size.group(1))), round(float(size.group(2))))
            ok = abs(dims[0] - A4_PT[0]) <= 1 and abs(dims[1] - A4_PT[1]) <= 1
            print(f"  page size {dims[0]}x{dims[1]} pt  {'A4 ok' if ok else 'NOT A4'}")
            if not ok:
                findings.append(f"page size is {dims}, A4 is {A4_PT}")
        if pages:
            print(f"  pages: {pages.group(1)}")

    if shutil.which("pdffonts"):
        lines = subprocess.run(["pdffonts", str(pdf)], capture_output=True, text=True).stdout.splitlines()
        if len(lines) >= 2:
            spans = [(m.start(), m.end()) for m in re.finditer(r"-+", lines[1])]
            header = [lines[0][a:b].strip() for a, b in spans[:-1]] + [lines[0][spans[-1][0]:].strip()]
            rows = [{h: r[a:b].strip() for h, (a, b) in zip(header, spans)} for r in lines[2:]]
            missing = [r.get("name", "?") for r in rows if r.get("emb") == "no"]
            type3 = [r.get("name", "?") for r in rows if r.get("type", "").startswith("Type 3")]
            print(f"  fonts: {len(rows)} used, {len(missing)} not embedded, {len(type3)} Type 3")
            findings += [f"font not embedded: {n}" for n in missing]
            findings += [f"Type 3 font: {n}" for n in type3]

    print("  reminder: add the conference copyright notice from the camera-ready toolkit,")
    print("  and check the page limit of the accepted version before uploading.")
    if findings:
        print("\n  findings:")
        for f in findings:
            print(f"    - {f}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1] if len(sys.argv) > 1 else "main_apsec_cameraready.pdf").resolve()))
