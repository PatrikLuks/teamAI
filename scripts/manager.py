from __future__ import annotations

import json
from pathlib import Path

TASKS_FILE = Path("tasks.json")


def generate_tasks() -> list[dict[str, str | int]]:
    # Minimal demo tasks; in real use, read from prompts/manager.md and reason
    return [
        {"id": 1, "title": "Implement greet API", "owner": "dev"},
        {"id": 2, "title": "Write tests for greet API", "owner": "qa"},
        {"id": 3, "title": "Update README", "owner": "docs"},
    ]


def main() -> int:
    tasks = generate_tasks()
    TASKS_FILE.write_text(json.dumps(tasks, indent=2), encoding="utf-8")
    print(f"Wrote {len(tasks)} tasks to {TASKS_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
