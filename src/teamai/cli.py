from __future__ import annotations

import argparse

from . import __version__


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="teamai", description="Team AI CLI")
    parser.add_argument("--version", action="version", version=f"teamai {__version__}")
    parser.add_argument(
        "-n",
        "--name",
        default="world",
        help="Jméno pro pozdrav",
    )
    args = parser.parse_args(argv)
    print(f"Hello, {args.name}!")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
