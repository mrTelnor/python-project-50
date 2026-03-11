import sys
from pathlib import Path

import pytest

from gendiff import generate_diff
from gendiff.scripts.gendiff import main
from gendiff.scripts.parser import parse_file


def get_path(filename):
    return Path(__file__).parent / "test_data" / filename


# stylish
@pytest.mark.parametrize('file1, file2, expected', [
    ('file1.json', 'file2.json', 'expected_stylish.txt'),
    ('file1.yml', 'file2.yml', 'expected_stylish.txt'),
    ('file1_nested.json', 'file2_nested.json', 'expected_nested_stylish.txt'),
    ('file1_nested.yml', 'file2_nested.yml', 'expected_nested_stylish.txt'),
])
def test_stylish(file1, file2, expected):
    result = generate_diff(get_path(file1), get_path(file2))
    assert result == get_path(expected).read_text()


# plain
@pytest.mark.parametrize('file1, file2, expected', [
    ('file1.json', 'file2.json', 'expected_plain.txt'),
    ('file1.yml', 'file2.yml', 'expected_plain.txt'),
    ('file1_nested.json', 'file2_nested.json', 'expected_nested_plain.txt'),
    ('file1_nested.yml', 'file2_nested.yml', 'expected_nested_plain.txt'),
])
def test_plain(file1, file2, expected):
    result = generate_diff(get_path(file1), get_path(file2), 'plain')
    assert result == get_path(expected).read_text()


# json
@pytest.mark.parametrize('file1, file2, expected', [
    ('file1.json', 'file2.json', 'expected_json.txt'),
    ('file1.yml', 'file2.yml', 'expected_json.txt'),
    ('file1_nested.json', 'file2_nested.json', 'expected_nested_json.txt'),
    ('file1_nested.yml', 'file2_nested.yml', 'expected_nested_json.txt'),
])
def test_json(file1, file2, expected):
    result = generate_diff(get_path(file1), get_path(file2), 'json')
    assert result == get_path(expected).read_text().strip()


# parser
def test_unknown_extension():
    with pytest.raises(ValueError):
        parse_file("file.txt")


def test_nonexistent_json_file():
    with pytest.raises(FileNotFoundError):
        parse_file("missing.json")


def test_invalid_json(tmp_path):
    file = tmp_path / "bad.json"
    file.write_text("{ invalid json }")
    with pytest.raises(Exception):
        parse_file(file)


# CLI
def test_cli_stylish(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", [
        "gendiff",
        "tests/test_data/file1.json",
        "tests/test_data/file2.json",
    ])
    main()
    assert "host" in capsys.readouterr().out


def test_cli_plain(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", [
        "gendiff", "-f", "plain",
        "tests/test_data/file1.json",
        "tests/test_data/file2.json",
    ])
    main()
    assert "Property" in capsys.readouterr().out


def test_cli_json(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", [
        "gendiff", "-f", "json",
        "tests/test_data/file1.json",
        "tests/test_data/file2.json",
    ])
    main()
    assert capsys.readouterr().out.strip().startswith("[")


def test_cli_version(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["gendiff", "-v"])
    with pytest.raises(SystemExit):
        main()
