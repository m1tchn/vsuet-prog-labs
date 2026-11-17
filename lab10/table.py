def row_sums(matrix):
    #Возвращает суммы строк матрицы
    return [sum(row) for row in matrix]


def column_sums(matrix):
    #Возвращает суммы столбцов прямоугольной матрицы
    if not matrix:
        return []

    return [sum(row[column] for row in matrix) for column in range(len(matrix[0]))]


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


def selected_sum(matrix):
    #Вариант 12: суммирует элементы строк с чётными индексами
    return sum(
        number
        for row_index, row in enumerate(matrix)
        if row_index % 2 == 0
        for number in row
    )
