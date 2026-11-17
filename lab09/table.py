def row_sums(matrix):
    #Возвращает суммы строк матрицы
    return [sum(row) for row in matrix]


def column_sums(matrix):
    #Возвращает суммы столбцов матрицы
    if not matrix:
        return []

    sums = []
    for column in range(len(matrix[0])):
        total = 0
        for row in matrix:
            total += row[column]
        sums.append(total)
    return sums


def diagonal_pattern(size):
    #Создаёт квадратный узор: 0 на диагонали, 1 выше, 2 ниже
    pattern = []
    for row in range(size):
        pattern_row = []
        for column in range(size):
            if row == column:
                pattern_row.append(0)
            elif row < column:
                pattern_row.append(1)
            else:
                pattern_row.append(2)
        pattern.append(pattern_row)
    return pattern


def transform(matrix):
    #Вариант 12: увеличивает каждый нечётный элемент на 1
    result = []
    for row in matrix:
        result_row = []
        for number in row:
            if number % 2 != 0:
                result_row.append(number + 1)
            else:
                result_row.append(number)
        result.append(result_row)
    return result
