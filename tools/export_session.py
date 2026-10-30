"""
Render the current Claude Code transcript into markdown for a session file's Part 1.

Usage:
    python3 tools/export_session.py            # newest transcript, from the last session marker
    python3 tools/export_session.py FILE.jsonl # a specific transcript

Slices from the last line matching "=== SESSION NNN: Topic ===" (printed by /session),
keeps only the human-readable turns (the learner's messages, Claude's prose, AskUserQuestion Q&A),
drops tool noise and system reminders, and prints markdown to stdout.
"""

import json
import re
import sys
from pathlib import Path

PROJECT_DIR = Path.home() / ".claude" / "projects" / re.sub(r"[^a-zA-Z0-9]", "-", str(Path.cwd()))
MARKER = re.compile(r"^=== SESSION (\d{3}): (.+?) ===\s*$", re.M)
NOISE = (
    "<system-reminder>", "<command-", "<local-command", "<task-notification>",
    "Base directory for this skill", "Caveat:", "[Request interrupted",
)


def newest_transcript():
    files = sorted(PROJECT_DIR.glob("*.jsonl"), key=lambda p: p.stat().st_mtime)
    if not files:
        sys.exit(f"no transcripts in {PROJECT_DIR}")
    return files[-1]


def clean(text):
    text = re.sub(r"<system-reminder>.*?</system-reminder>", "", text, flags=re.S)
    return text.strip()


def turns(path):
    """Yield (speaker, text) in order. One record per line; only top-level user/assistant records."""
    seen = set()
    for line in path.open():
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        if rec.get("type") not in ("user", "assistant") or rec.get("isSidechain") or rec.get("isMeta"):
            continue
        uid = rec.get("uuid")
        if uid in seen:
            continue
        seen.add(uid)
        msg = rec.get("message") or {}
        content = msg.get("content")
        blocks = [{"type": "text", "text": content}] if isinstance(content, str) else (content or [])
        for b in blocks:
            if not isinstance(b, dict):
                continue
            if b.get("type") == "text":
                text = clean(b.get("text", ""))
                if text and not text.startswith(NOISE):
                    yield ("Learner" if rec["type"] == "user" else "Claude"), text
            elif b.get("type") == "tool_use" and b.get("name") == "AskUserQuestion":
                qs = (b.get("input") or {}).get("questions") or []
                for q in qs:
                    opts = "\n".join(f"  - {o.get('label')}: {o.get('description', '')}" for o in q.get("options", []))
                    yield "Claude", f"**Q: {q.get('question')}**\n{opts}"
            elif b.get("type") == "tool_result":
                raw = b.get("content")
                raw = raw if isinstance(raw, str) else " ".join(x.get("text", "") for x in raw or [] if isinstance(x, dict))
                if "have been answered" in raw:
                    yield "Learner", raw.split("You can now continue")[0].strip()


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else newest_transcript()
    all_turns = list(turns(path))
    start = 0
    for i, (who, text) in enumerate(all_turns):
        if who == "Claude" and MARKER.search(text):
            start = i
    out = []
    for who, text in all_turns[start:]:
        text = MARKER.sub("", text).strip() if who == "Claude" else text
        if text:
            out.append(f"**{who}:**\n\n{text}\n")
    if not out:
        sys.exit("no turns found after the last session marker")
    print("\n---\n\n".join(out))


if __name__ == "__main__":
    main()
