from pathlib import Path

def _parse_integers(line, line_number, expected_count, kind):
    #Преобразует строку в числа и проверяет её длину
    parts = line.strip().split()
    if len(parts) != expected_count:
        raise ValueError(
            f"Строка {line_number}: ожидалось {expected_count} чисел, получено {len(parts)}"
        )

    try:
        return [int(part) for part in parts]
    except ValueError as error:
        raise ValueError(f"Строка {line_number}: {kind} содержит нецелое значение") from error


def read_matrix(path):
    #Читает и проверяет прямоугольную матрицу из файла
    path = Path(path)
    with path.open("r", encoding="utf-8") as file:
        lines = file.readlines()

    if not lines:
        raise ValueError("Файл пуст")

    header = _parse_integers(lines[0], 1, 2, "Заголовок")
    rows, columns = header
    if rows <= 0 or columns <= 0:
        raise ValueError("Строка 1: размеры таблицы должны быть больше нуля")

    expected_lines = rows + 1
    if len(lines) > expected_lines:
        raise ValueError(
            f"Лишние строки: ожидалось {rows} строк данных, найдено больше"
        )
    if len(lines) < expected_lines:
        missing_line = len(lines) + 1
        raise ValueError(f"Строка {missing_line}: отсутствует строка данных")

    matrix = []
    for line_number, line in enumerate(lines[1:], start=2):
        matrix.append(_parse_integers(line, line_number, columns, "Строка данных"))
    return matrix
