#!/usr/bin/env python3
"""Structural release checks for an English Forge exam package.

This validates manifests and file presence only. It cannot verify answer correctness,
English naturalness, evidence quality, copyright status, or rendered visual quality.
"""
from pathlib import Path
import argparse, json, sys

REQUIRED = {
    "exam_pdf": [".pdf"],
    "solutions_pdf": [".pdf"],
    "writing_pptx": [".pptx"],
    "qa_report": [".md", ".json"],
}
def main():
    p=argparse.ArgumentParser()
    p.add_argument("manifest", nargs="?", default="outputs/release_manifest.json")
    a=p.parse_args()
    path=Path(a.manifest)
    if not path.exists():
        print(f"FAIL: manifest not found: {path}")
        return 2
    data=json.loads(path.read_text(encoding="utf-8"))
    errors=[]
    for key, exts in REQUIRED.items():
        value=data.get(key)
        if not value:
            errors.append(f"missing manifest field: {key}")
            continue
        f=Path(value)
        if not f.exists():
            errors.append(f"missing artifact: {f}")
        elif f.suffix.lower() not in exts:
            errors.append(f"unexpected extension for {key}: {f.suffix}")
        elif f.stat().st_size == 0:
            errors.append(f"empty artifact: {f}")
    inventory=data.get("coverage", {})
    for field in ("pages_total","questions_total","questions_explained","slides_total","slides_reviewed"):
        if field not in inventory:
            errors.append(f"missing coverage field: {field}")
    if inventory.get("questions_total") != inventory.get("questions_explained"):
        errors.append("question coverage mismatch")
    if inventory.get("slides_total") != inventory.get("slides_reviewed"):
        errors.append("slide review coverage mismatch")
    if errors:
        print("FAIL")
        print("\n".join(f"- {x}" for x in errors))
        return 1
    print("PASS: structural manifest checks only; pedagogical and visual review remain separate.")
    return 0
if __name__=="__main__":
    sys.exit(main())
