from table import column_sums, diagonal_pattern, row_sums, transform


def print_matrix(matrix):
    #Выводит строки матрицы через пробел
    for row in matrix:
        print(*row)


def read_matrix():
    #Считывает прямоугольную матрицу с повтором строк неверной длины
    rows = int(input())
    columns = int(input())
    matrix = []

    for _ in range(rows):
        row = [int(part) for part in input().split()]
        while len(row) != columns:
            print(f"Нужно ровно {columns} чисел")
            row = [int(part) for part in input().split()]
        matrix.append(row)

    return matrix


def read_positive_size():
    #Считывает положительный размер квадратного узора
    size = int(input())
    while size < 1:
        print("Размер должен быть положительным")
        size = int(input())
    return size


def main():
    matrix = read_matrix()
    print("Исходная таблица:")
    print_matrix(matrix)
    print(f"Суммы строк: {row_sums(matrix)}")
    print(f"Суммы столбцов: {column_sums(matrix)}")

    transformed = transform(matrix)
    print("Преобразованная таблица:")
    print_matrix(transformed)

    size = read_positive_size()
    print("Диагональный узор:")
    print_matrix(diagonal_pattern(size))


if __name__ == "__main__":
    main()
