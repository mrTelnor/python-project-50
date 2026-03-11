import sys
import pytest
from gendiff.scripts.gendiff import main


def test_cli_stylish_format(monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "gendiff",
            "tests/test_data/file1.json",
            "tests/test_data/file2.json",
        ],
    )

    main()

    captured = capsys.readouterr()
    assert "host" in captured.out


def test_cli_plain_format(monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "gendiff",
            "-f",
            "plain",
            "tests/test_data/file1.json",
            "tests/test_data/file2.json",
        ],
    )

    main()

    captured = capsys.readouterr()
    assert "Property" in captured.out


def test_cli_json_format(monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "gendiff",
            "-f",
            "json",
            "tests/test_data/file1.json",
            "tests/test_data/file2.json",
        ],
    )

    main()

    captured = capsys.readouterr()
    assert captured.out.strip().startswith("[")


def test_cli_version(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["gendiff", "-v"])

    with pytest.raises(SystemExit):
        main()