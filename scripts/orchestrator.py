from __future__ import annotations

import subprocess


def run(cmd: list[str]) -> int:
    print("$", " ".join(cmd))
    return subprocess.run(cmd).returncode


def main() -> int:
    rc = 0
    rc |= run(["/Applications/teamAI/venv/bin/python", "-m", "scripts.manager"])  # manager
    rc |= run(["/Applications/teamAI/venv/bin/python", "-m", "scripts.developer"])  # dev
    rc |= run(["/Applications/teamAI/venv/bin/python", "-m", "scripts.tester"])  # tester
    rc |= run(["/Applications/teamAI/venv/bin/python", "-m", "scripts.copilot_pro"])  # copilot
    rc |= run(["/Applications/teamAI/venv/bin/python", "-m", "scripts.docs_agent"])  # docs
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
