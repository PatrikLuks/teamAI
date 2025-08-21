from __future__ import annotations

from teamai.app import greet


def test_greet_default():
    assert greet() == "Hello, world!"


def test_greet_custom():
    assert greet("Team") == "Hello, Team!"
