#!/usr/bin/env python3
"""
my-skills validator — quality gate for the collection.

Checks every <category>/<skill>/SKILL.md against:
  1. SKILL.md exists
  2. YAML frontmatter present and parseable
  3. Required fields: name, description
  4. name == directory name
  5. description contains a trigger phrase (Use when / Use for / Triggers / Use this)
  6. description length in [30, 200] chars
  7. body word count in [50, 3000]

Exit 0 = all clean. Exit 1 = at least one error.
Warnings (yellow) don't fail the gate. Errors (red) do.
"""
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # repo root (one above scripts/)

CATEGORIES = ["dev", "doc", "marketing", "biz", "meta"]

REQUIRED_FM = ["name", "description"]
TRIGGER_WORDS = [
    # English triggers
    "use when", "use for", "triggers", "use this",
    # Chinese triggers (for zh-* and zh-only collections)
    "用于", "适用", "使用场景", "使用", "触发", "当", "场景",
]


def parse_frontmatter(content):
    """Extract flat YAML frontmatter (key: value lines). Returns dict or None."""
    if not content.startswith("---"):
        return None
    end = content.find("\n---", 3)
    if end == -1:
        return None
    fm_text = content[3:end].lstrip("\n")
    result = {}
    for line in fm_text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = re.match(r"^(\S+):\s*(.+)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip().strip('"').strip("'")
            result[key] = val
    return result


def body_word_count(content):
    if content.startswith("---"):
        end = content.find("\n---", 3)
        if end != -1:
            content = content[end + 4:]
    return len(content.split())


def validate_skill(skill_md: Path, skill_name: str):
    errors, warnings, notes = [], [], []
    if not skill_md.is_file():
        return [f"SKILL.md missing in {skill_md.parent}"], [], []

    content = skill_md.read_text(encoding="utf-8", errors="replace")

    fm = parse_frontmatter(content)
    if fm is None:
        return ["missing or malformed YAML frontmatter"], [], []

    for field in REQUIRED_FM:
        if field not in fm or not fm[field]:
            errors.append(f"missing required frontmatter field: {field}")

    if "name" in fm and fm["name"] != skill_name:
        errors.append(f"name mismatch: frontmatter says '{fm['name']}' but directory is '{skill_name}'")

    desc = fm.get("description", "")
    if desc:
        # Length thresholds are language-aware: Chinese text packs more content per char
        is_zh = any("\u4e00" <= ch <= "\u9fff" for ch in desc)
        min_len, max_len = (15, 80) if is_zh else (30, 200)
        if len(desc) < min_len:
            warnings.append(f"description is very short ({len(desc)} chars, min {min_len})")
        elif len(desc) > max_len:
            warnings.append(f"description is very long ({len(desc)} chars, max {max_len})")
        if not any(t in desc.lower() for t in TRIGGER_WORDS):
            triggers_hint = "use when / use for / triggers / use this — 或中文 用于/适用/使用场景/触发"
            warnings.append(f"description lacks trigger phrase ({triggers_hint})")

    wc = body_word_count(content)
    notes.append(f"body: {wc} words")
    if wc < 50:
        warnings.append(f"body is very short ({wc} words) — may be incomplete")
    elif wc > 3000:
        warnings.append(f"body is very long ({wc} words) — consider splitting into references/")

    return errors, warnings, notes


def main():
    total_skills, total_errors, total_warnings = 0, 0, 0
    per_skill = []

    for cat in CATEGORIES:
        cat_dir = ROOT / cat
        if not cat_dir.is_dir():
            continue
        for entry in sorted(cat_dir.iterdir()):
            if not entry.is_dir():
                continue
            skill_md = entry / "SKILL.md"
            total_skills += 1
            errors, warnings, notes = validate_skill(skill_md, entry.name)
            total_errors += len(errors)
            total_warnings += len(warnings)
            if errors or warnings:
                per_skill.append((cat, entry.name, errors, warnings, notes))

    # Report
    RED, YELLOW, DIM, BOLD, RESET = "\033[91m", "\033[93m", "\033[2m", "\033[1m", "\033[0m"
    print(f"\n{BOLD}{'=' * 60}")
    print(f" my-skills validator")
    print(f"{'=' * 60}{RESET}\n")
    print(f"  scanned:   {total_skills} skills")
    print(f"  errors:    {total_errors}")
    print(f"  warnings:  {total_warnings}\n")

    if per_skill:
        for cat, name, errs, warns, notes in per_skill:
            print(f"{BOLD}{cat}/{name}{RESET}")
            for e in errs:
                print(f"  {RED}ERR  {e}{RESET}")
            for w in warns:
                print(f"  {YELLOW}WARN {w}{RESET}")
            for n in notes:
                print(f"  {DIM}     {n}{RESET}")
            print()
    else:
        print(f"  {BOLD}all clean — zero issues{RESET}\n")

    print(f"{BOLD}{'=' * 60}{RESET}")
    if total_errors == 0:
        print(f"  {BOLD}PASS{RESET} ({total_warnings} warnings, {total_skills} skills)")
    else:
        print(f"  {RED}{BOLD}FAIL{RESET}  {total_errors} errors, {total_warnings} warnings")
    print(f"{BOLD}{'=' * 60}{RESET}\n")

    sys.exit(1 if total_errors > 0 else 0)


if __name__ == "__main__":
    main()
