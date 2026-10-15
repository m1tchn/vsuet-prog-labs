from functions import average, normalize_text, select_numbers, sum_digits


assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert average([1, 2]) == 1.5
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""

source = [-5, 0, 2, 5]
source_copy = source.copy()
assert select_numbers(source, 2) == []
assert source == source_copy

assert select_numbers([-4, 2, 8, 3, 8], 2) == [8, 8]
assert select_numbers([], 2) == []
assert select_numbers([4, 4, 6], 2) == [4, 4, 6]
assert select_numbers([2, 5, 7], 2) == []

print("Базовые проверки и проверки варианта пройдены")
