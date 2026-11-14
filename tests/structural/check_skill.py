#!/usr/bin/env python3
"""Structural checks for the editorial-ux-skill payload (standard library only).

Usage: python3 tests/structural/check_skill.py [skill_dir]

Checks (see docs/architecture.md, docs/decisions.md D-005, D-008, D-015, D-017):
  - frontmatter: only spec fields, name == directory name, name rules, description length
  - SKILL.md: under 500 lines and about 5000 tokens
  - no argument placeholders in any skill file
  - every file listed in SKILL.md exists; no skill file is unlisted
  - reference files contain no links to other files (reference depth one)
  - per-file size budgets from budgets.json
Exit code 0 = all checks passed, 1 = at least one failed.
"""
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ALLOWED_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
PLACEHOLDER_RE = re.compile(r"\$ARGUMENTS|\$\{|\{\{|\$[0-9]\b")
MD_LINK_RE = re.compile(r"\]\((?!https?://|#)([^)]+)\)")

failures = []


def fail(msg):
    failures.append(msg)
    print("FAIL:", msg)


def ok(msg):
    print("ok:  ", msg)


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    block = text[4:end]
    body = text[end + 4:]
    data, current = {}, None
    for line in block.split("\n"):
        if not line.strip():
            continue
        if line.startswith((" ", "\t")):
            if current is not None and isinstance(data.get(current), dict):
                k, _, v = line.strip().partition(":")
                data[current][k.strip()] = v.strip().strip('"')
            continue
        k, _, v = line.partition(":")
        k, v = k.strip(), v.strip()
        if v == "":
            data[k] = {}
            current = k
        else:
            data[k] = v.strip('"')
            current = k
    return data, body


def main():
    root = Path(__file__).resolve().parents[2]
    skill_dir = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else root / "skills" / "editorial-ux-skill"
    budgets = json.loads((Path(__file__).parent / "budgets.json").read_text(encoding="utf-8"))

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        fail(f"{skill_md} missing")
        return 1
    text = skill_md.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    if fm is None:
        fail("SKILL.md has no frontmatter starting on line 1")
        return 1

    # frontmatter
    extra = set(fm) - ALLOWED_KEYS
    if extra:
        fail(f"frontmatter has fields outside the Agent Skills spec: {sorted(extra)}")
    else:
        ok("frontmatter uses only spec fields")
    name = fm.get("name", "")
    if not name or len(name) > 64 or not NAME_RE.match(name):
        fail(f"invalid name: {name!r}")
    elif name != skill_dir.name:
        fail(f"name {name!r} does not match directory {skill_dir.name!r}")
    else:
        ok(f"name '{name}' valid and equals directory name")
    desc = fm.get("description", "")
    if not (1 <= len(desc) <= 1024):
        fail(f"description length {len(desc)} not in 1..1024")
    else:
        ok(f"description length {len(desc)} (max 1024)")

    # size
    lines = text.count("\n") + 1
    approx_tokens = len(text) // 4
    if lines >= 500:
        fail(f"SKILL.md has {lines} lines (limit 500)")
    else:
        ok(f"SKILL.md {lines} lines (limit 500)")
    if approx_tokens >= 5000:
        fail(f"SKILL.md about {approx_tokens} tokens (limit 5000, estimated as chars/4)")
    else:
        ok(f"SKILL.md about {approx_tokens} tokens (limit 5000, estimated)")

    files = sorted(p for p in skill_dir.rglob("*") if p.is_file())
    rel = {p.relative_to(skill_dir).as_posix(): p for p in files}

    # placeholders
    bad = [r for r, p in rel.items() if PLACEHOLDER_RE.search(p.read_text(encoding="utf-8"))]
    if bad:
        fail(f"argument placeholders found in: {bad}")
    else:
        ok("no argument placeholders")

    # listed files exist, none unlisted
    listed = set(re.findall(r"`((?:references|assets)/[^`\s]+)`", body))
    missing = sorted(x for x in listed if x not in rel)
    if missing:
        fail(f"files listed in SKILL.md do not exist: {missing}")
    else:
        ok(f"all {len(listed)} files listed in SKILL.md exist")
    unlisted = sorted(r for r in rel if r != "SKILL.md" and r not in listed)
    if unlisted:
        fail(f"files not listed in SKILL.md: {unlisted}")
    else:
        ok("no unlisted skill files")

    # depth one
    deep = []
    for r, p in rel.items():
        if r == "SKILL.md":
            continue
        if MD_LINK_RE.search(p.read_text(encoding="utf-8")):
            deep.append(r)
    if deep:
        fail(f"reference files link to other files (depth > 1): {deep}")
    else:
        ok("reference depth is one")

    # budgets
    over = []
    for r, p in rel.items():
        limit = budgets.get("files", {}).get(r)
        if limit is None:
            over.append(f"{r}: no budget defined")
        elif p.stat().st_size > limit:
            over.append(f"{r}: {p.stat().st_size} bytes > {limit}")
    if over:
        fail("budget problems: " + "; ".join(over))
    else:
        ok("all files within size budgets")

    # per-command load size
    for cmd, members in budgets.get("commands", {}).items():
        total = sum(rel[m].stat().st_size for m in members if m in rel) + rel["SKILL.md"].stat().st_size
        limit = budgets.get("command_limit_bytes", 0)
        if limit and total > limit:
            fail(f"command '{cmd}' loads {total} bytes > {limit}")
        else:
            ok(f"command '{cmd}' loads {total} bytes (limit {limit})")

    # official validator (optional: pip install skills-ref from github.com/agentskills/agentskills)
    exe = os.environ.get("SKILLS_REF") or shutil.which("skills-ref")
    if exe:
        res = subprocess.run([exe, "validate", str(skill_dir)], capture_output=True, text=True)
        if res.returncode == 0:
            ok("skills-ref validate passed")
        else:
            fail("skills-ref validate failed: " + (res.stdout + res.stderr).strip().replace("\n", " | "))
    else:
        print("skip: skills-ref not found (optional, set SKILLS_REF or install it)")

    print()
    if failures:
        print(f"{len(failures)} check(s) failed")
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
