from pathlib import Path

from gendiff import generate_diff


def get_path(filename):
    return Path(__file__).parent / "test_data" / filename


def test_generate_diff():
    file1 = get_path("file1.json")
    file2 = get_path("file2.json")
    expected = get_path("expected.txt").read_text()

    result = generate_diff(file1, file2)

    assert result == expected
