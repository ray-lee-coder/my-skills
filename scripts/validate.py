#!/usr/bin/env python3
"""
my-skills validator — quality gate for the collection.

v2 upgrades (2026-06-08, after coreyhaines31 + mattpocock audit):
  - name field: 1-64 chars, lowercase a-z 0-9 -, no leading/trailing/double hyphen
  - description: length 30-1024 (en) / 15-200 (zh)
  - block shell injection syntax `` !`command` `` (cross-agent principle)
  - tolerant of `metadata:` nested block (coreyhaines31 style)

Checks every <category>/<skill>/SKILL.md against:
  1. SKILL.md exists
  2. YAML frontmatter present and parseable (tolerates nested `metadata:`)
  3. Required fields: name, description
  4. name == directory name AND name has strict kebab-case syntax
  5. description contains a trigger phrase (Use when / Use for / Triggers / Use this)
  6. description length in [30, 1024] chars (en) / [15, 200] (zh)
  7. body word count in [50, 3000]
  8. body does NOT contain Claude-Code-only shell-injection syntax `` !`cmd` ``

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

# Shell-injection syntax Claude Code uses; cross-agent skills must not embed it.
# Pattern: !`command`  (literal backticks wrapping a shell command)
# Use a negative lookbehind to avoid matching things like `#REF!` in code blocks
# (the actual Claude Code syntax is `!`cmd`` — exclamation, backtick, ...)
SHELL_INJECTION_RE = re.compile(r"(?<![\w#.])!`[^`\n]{1,500}`")

# Name field syntax rules (agentskills.io + coreyhaines31 convention)
NAME_RE = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?$")
# Disallow consecutive hyphens
NAME_DOUBLE_HYPHEN_RE = re.compile(r"--")


def parse_frontmatter(content):
    """Extract flat YAML frontmatter. Tolerates a single nested `metadata:` block.

    Returns dict with `name`, `description`, and (if present) `metadata_version` etc.
    """
    if not content.startswith("---"):
        return None
    end = content.find("\n---", 3)
    if end == -1:
        return None
    fm_text = content[3:end].lstrip("\n")
    result = {}
    in_metadata = False
    metadata = {}
    for line in fm_text.splitlines():
        raw = line
        line_stripped = line.strip()
        if not line_stripped or line_stripped.startswith("#"):
            continue
        if line_stripped == "metadata:":
            in_metadata = True
            continue
        if in_metadata:
            # End of metadata block when indentation drops to 0
            if not raw.startswith((" ", "\t")):
                in_metadata = False
            else:
                m = re.match(r"^\s+(\S+):\s*(.+)$", line)
                if m:
                    metadata[m.group(1)] = m.group(2).strip().strip('"').strip("'")
                continue
        m = re.match(r"^(\S+):\s*(.+)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip().strip('"').strip("'")
            result[key] = val
    if metadata:
        result["__metadata"] = metadata
    return result


def body_word_count(content):
    if content.startswith("---"):
        end = content.find("\n---", 3)
        if end != -1:
            content = content[end + 4:]
    return len(content.split())


def body_text(content):
    """Return the body portion of the SKILL.md (after frontmatter)."""
    if content.startswith("---"):
        end = content.find("\n---", 3)
        if end != -1:
            return content[end + 4:]
    return content


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

    # name: match dir + strict syntax
    name = fm.get("name", "")
    if name:
        if name != skill_name:
            errors.append(f"name mismatch: frontmatter says '{name}' but directory is '{skill_name}'")
        if len(name) > 64:
            errors.append(f"name too long ({len(name)} chars, max 64)")
        elif not NAME_RE.match(name):
            errors.append(f"name syntax invalid: must be 1-64 chars, lowercase a-z 0-9 -, no leading/trailing hyphen")
        if NAME_DOUBLE_HYPHEN_RE.search(name):
            errors.append(f"name contains consecutive hyphens '--' (disallowed)")

    desc = fm.get("description", "")
    if desc:
        # Length thresholds are language-aware
        is_zh = any("\u4e00" <= ch <= "\u9fff" for ch in desc)
        min_len, max_len = (15, 200) if is_zh else (30, 1024)
        if len(desc) < min_len:
            warnings.append(f"description is very short ({len(desc)} chars, min {min_len})")
        elif len(desc) > max_len:
            warnings.append(f"description is very long ({len(desc)} chars, max {max_len})")
        if not any(t in desc.lower() for t in TRIGGER_WORDS):
            triggers_hint = "use when / use for / triggers / use this — 或中文 用于/适用/使用场景/触发"
            warnings.append(f"description lacks trigger phrase ({triggers_hint})")

    # Body checks
    body = body_text(content)
    wc = len(body.split())
    notes.append(f"body: {wc} words")
    if wc < 50:
        warnings.append(f"body is very short ({wc} words) — may be incomplete")
    elif wc > 3000:
        warnings.append(f"body is very long ({wc} words) — consider splitting into references/")

    # Shell-injection: only flag inside the body, not in frontmatter (which is meta-only)
    inj = SHELL_INJECTION_RE.search(body)
    if inj:
        errors.append(
            f"body contains Claude-Code shell-injection syntax `!`command`` "
            f"({inj.group(0)[:40]}...) — cross-agent skills must not embed this"
        )

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
    print(f" my-skills validator v2")
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
