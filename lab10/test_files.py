from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from files_lab import read_matrix
from main import read_positive_integer
from table import column_sums, diagonal_pattern, row_sums, selected_sum


def assert_value_error(content, expected_text=None):
    with TemporaryDirectory() as directory:
        path = Path(directory) / "matrix.txt"
        path.write_text(content, encoding="utf-8")
        try:
            read_matrix(path)
        except ValueError as error:
            if expected_text is not None:
                assert expected_text in str(error)
        else:
            raise AssertionError("Ошибка формата не обнаружена")


with TemporaryDirectory() as directory:
    path = Path(directory) / "matrix.txt"
    path.write_text("1 2\n7 -1\n", encoding="utf-8")
    assert read_matrix(path) == [[7, -1]]

with TemporaryDirectory() as directory:
    path = Path(directory) / "matrix.txt"
    path.write_text("1 1\n0\n", encoding="utf-8")
    assert read_matrix(path) == [[0]]

assert_value_error("")
assert_value_error("0 3\n")
assert_value_error("1 2\n1\n", "Строка 2")
assert_value_error("1 2\n1 x\n", "Строка 2")
assert_value_error("1 1\n7\n8\n")

with TemporaryDirectory() as directory:
    missing_path = Path(directory) / "missing.txt"
    try:
        read_matrix(missing_path)
    except FileNotFoundError:
        pass
    else:
        raise AssertionError("FileNotFoundError не обнаружен")

matrix = [[1, 2, 3], [4, 5, 6]]
assert row_sums(matrix) == [6, 15]
assert column_sums(matrix) == [5, 7, 9]
assert selected_sum(matrix) == 6
assert selected_sum([]) == 0
assert selected_sum([[7]]) == 7
assert selected_sum([[1], [2], [3]]) == 4
assert diagonal_pattern(3) == [[0, 1, 1], [2, 0, 1], [2, 2, 0]]

with patch("builtins.input", side_effect=["abc", "0", "-2", "3"]):
    assert read_positive_integer() == 3

print("Проверки файлов и таблицы пройдены")
