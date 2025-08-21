from __future__ import annotations


def greet(name: str = "world") -> str:
    return f"Hello, {name}!"


def main(argv: list[str] | None = None) -> int:
    # Simple CLI behavior just to demonstrate tests
    name = argv[1] if argv and len(argv) > 1 else "world"
    print(greet(name))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
