from __future__ import annotations

from pathlib import Path

SRC_DIR = Path("src")
TEAMAI_DIR = SRC_DIR / "teamai"


def implement_feature() -> None:
    TEAMAI_DIR.mkdir(parents=True, exist_ok=True)
    app_path = Path("src/app.py")
    if not app_path.exists():
        # ensure a minimal app exists
        app_path.write_text(
            "from flask import Flask\napp = Flask(__name__)\n@app.get('/')\ndef index(): return 'OK'\n",
            encoding="utf-8",
        )


def main() -> int:
    implement_feature()
    print("Developer: ensured minimal app exists.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
