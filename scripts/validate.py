#!/usr/bin/env python3
"""Validate the OSINT catalog with only the Python standard library."""
import csv
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

root = Path(__file__).resolve().parents[1]
tools = json.loads((root / "data/tools.json").read_text(encoding="utf-8"))
required = {"id", "name", "description", "access", "category", "url", "responsible_use"}
errors = []
seen = set()
for i, tool in enumerate(tools, 1):
    missing = required - tool.keys()
    if missing:
        errors.append(f"Entry {i}: missing {sorted(missing)}")
        continue
    key = (tool["category"].casefold(), tool["name"].casefold())
    if key in seen:
        errors.append(f"Entry {i}: duplicate tool/category {key}")
    seen.add(key)
    if not all(isinstance(tool[k], str) and tool[k].strip() for k in required):
        errors.append(f"Entry {i}: blank or non-string field")
    u = urlparse(tool["url"])
    if u.scheme != "https" or not u.netloc or " " in tool["url"]:
        errors.append(f"Entry {i}: malformed URL {tool['url']}")
with (root / "data/tools.csv").open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
if len(rows) != len(tools):
    errors.append("CSV and JSON entry counts differ")
else:
    for i, (a, b) in enumerate(zip(rows, tools), 1):
        if a != b:
            errors.append(f"CSV/JSON mismatch at entry {i}")
            break
print(f"Validated {len(tools)} entries in {len(Counter(t['category'] for t in tools))} categories")
if errors:
    print("\n".join(errors))
    raise SystemExit(1)
print("PASS")
