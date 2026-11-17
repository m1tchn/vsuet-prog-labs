from table import column_sums, diagonal_pattern, row_sums, transform


matrix = [[1, 2, 3], [4, 5, 6]]
assert row_sums(matrix) == [6, 15]
assert column_sums(matrix) == [5, 7, 9]

assert row_sums([[7]]) == [7]
assert column_sums([[7]]) == [7]
assert diagonal_pattern(1) == [[0]]

single_column = [[1], [-1], [0]]
assert row_sums(single_column) == [1, -1, 0]
assert column_sums(single_column) == [0]

assert row_sums([]) == []
assert column_sums([]) == []
assert transform([]) == []
assert diagonal_pattern(3) == [[0, 1, 1], [2, 0, 1], [2, 2, 0]]

source = [[-2, 0, 3], [4, -5, 6]]
source_copy = [row.copy() for row in source]
result = transform(source)
assert result == [[-2, 0, 4], [4, -4, 6]]
assert source == source_copy
result[0][0] = 100
assert source[0][0] == -2

assert transform([[1, 1], [2, 3]]) == [[2, 2], [2, 4]]

print("Проверки таблиц пройдены")
