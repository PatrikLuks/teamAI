from __future__ import annotations

import subprocess


def main() -> int:
    print("Tester: running pytest...")
    result = subprocess.run(["/Applications/teamAI/venv/bin/python", "-m", "pytest", "-q"])  # adjust if needed
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
