from pathlib import Path

from gendiff import generate_diff


def test_plain_format():
    
    file1 = get_path("file1_nested.json")
    file2 = get_path("file2_nested.json")
    expected = get_path("expected_plain.txt").read_text()

    result = generate_diff(file1, file2, 'plain')

    assert result == expected