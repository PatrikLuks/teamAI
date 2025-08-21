from __future__ import annotations

from pathlib import Path

README = Path("README.md")


def main() -> int:
    if README.exists():
        content = README.read_text(encoding="utf-8")
        if "## Daily Workflow" not in content:
            content += "\n\n## Daily Workflow\n\nRun `python -m scripts.orchestrator`.\n"
            README.write_text(content, encoding="utf-8")
            print("Docs: updated README with Daily Workflow section.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
