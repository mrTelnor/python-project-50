from pathlib import Path

from gendiff import generate_diff


def get_path(filename):
    return Path(__file__).parent / "test_data" / filename


def test_json_json():
    file1 = get_path("file1.json")
    file2 = get_path("file2.json")
    expected = get_path("expected_json.txt").read_text().strip()

    result = generate_diff(file1, file2, 'json')
    assert result == expected


def test_json_yaml():
    file1 = get_path("file1.yml")
    file2 = get_path("file2.yml")
    expected = get_path("expected_json.txt").read_text().strip()

    result = generate_diff(file1, file2, 'json')
    assert result == expected


def test_json_nested_json():
    file1 = get_path("file1_nested.json")
    file2 = get_path("file2_nested.json")
    expected = get_path("expected_nested_json.txt").read_text().strip()

    result = generate_diff(file1, file2, 'json')
    assert result == expected


def test_json_nested_yaml():
    file1 = get_path("file1_nested.yml")
    file2 = get_path("file2_nested.yml")
    expected = get_path("expected_nested_json.txt").read_text().strip()

    result = generate_diff(file1, file2, 'json')
    assert result == expected