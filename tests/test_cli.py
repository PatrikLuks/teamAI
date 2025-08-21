from __future__ import annotations

import teamai
from teamai.cli import main


def test_version():
    assert isinstance(teamai.__version__, str)


def test_main_prints_greeting(capsys):
    rc = main(["--name", "Team"])
    assert rc == 0
    captured = capsys.readouterr()
    assert "Hello, Team!" in captured.out
