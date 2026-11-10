#!/usr/bin/env python3
"""Static integrity checks for the original Twine source and published assets.

No third-party packages required. This does not substitute for browser gameplay tests.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = (ROOT / "Home.twee").read_text(encoding="utf-8")
HTML = (ROOT / "index.html").read_text(encoding="utf-8")

names = re.findall(r"^::\s*(.+)$", SOURCE, flags=re.M)
names = [re.split(r"\s+(?=\[|\{)", n, maxsplit=1)[0].strip() for n in names]
name_set = set(names)
assert len(names) == len(name_set), "Duplicate passage declarations"
assert "Awakening" in name_set, "Missing start passage"
assert '"format": "SugarCube"' in SOURCE, "Unexpected story engine"

wiki = re.findall(r"\[\[([^\]]+)\]\]", SOURCE)
def target(link):
    if "->" in link: return link.rsplit("->", 1)[1].strip()
    if "<-" in link: return link.split("<-", 1)[0].strip()
    if "|" in link: return link.rsplit("|", 1)[1].strip()
    return link.strip()
broken = [(link,target(link)) for link in wiki if target(link) not in name_set]
assert not broken, "Unknown wiki targets: " + repr(broken[:10])

# Only inspect references with concrete local paths. Programmatically assembled
# paths and external URLs require separate runtime/manual tests.
refs = set(re.findall(r"(?:\./)?(?:images|music)/[A-Za-z0-9_.()-]+\.(?:png|jpg|jpeg|mp3|wav)", SOURCE, flags=re.I))
missing = [p for p in sorted(refs) if not (ROOT / p.lstrip('./')).is_file()]
assert not missing, "Missing media references: " + repr(missing)

assert "<html" in HTML.lower(), "Missing compiled HTML"
assert "SugarCube" in HTML, "Missing compiled story engine"
compiled = set(re.findall(r'<tw-passagedata\b[^>]*\bname="([^"]+)"', HTML))
special = {"StoryTitle", "StoryData", "StoryScript", "StoryStylesheet"}
assert compiled == name_set - special, "Compiled HTML passage set differs from source"
assert 'startnode="13"' in HTML, "Unexpected compiled start passage"
assert re.search(r'<tw-passagedata(?=[^>]*\bname="Awakening")(?=[^>]*\bpid="13")[^>]*>', HTML), "Start passage absent from compiled HTML"
assert (ROOT/"images"/"logo.png").is_file()

assets = {"images":len(list((ROOT/"images").glob("*"))),"music":len(list((ROOT/"music").glob("*.mp3")))}
print(f"PASS: {len(names)} source declarations and {len(compiled)} matching compiled passages")
print(f"PASS: {len(wiki)} resolved wiki links")
print(f"PASS: {len(refs)} referenced media paths exist")
print(f"PASS: {assets['images']} images; {assets['music']} audio files; compiled HTML present")
print("NOTE: font binaries are intentionally omitted, and end-to-end gameplay is not verified")
