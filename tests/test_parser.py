import pytest

from gendiff.parser import parse_file


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