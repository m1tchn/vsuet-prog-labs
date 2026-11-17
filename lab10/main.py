from pathlib import Path

from files_lab import read_matrix
from table import column_sums, row_sums, selected_sum


FOLDER = Path(__file__).resolve().parent
MATRIX_PATH = FOLDER / "matrix.txt"
REPORT_PATH = FOLDER / "report.txt"


def read_positive_integer():
    #Повторяет ввод, пока не получит целое число больше нуля
    while True:
        value = input()
        try:
            number = int(value)
        except ValueError:
            print("Нужно ввести целое число")
            continue
        if number <= 0:
            print("Число должно быть больше нуля")
            continue
        return number


def write_report(matrix, path):
    #Записывает отчёт для уже проверенной матрицы
    lines = [
        f"Суммы строк: {' '.join(map(str, row_sums(matrix)))}",
        f"Суммы столбцов: {' '.join(map(str, column_sums(matrix)))}",
        f"Результат варианта: {selected_sum(matrix)}",
    ]
    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    try:
        matrix = read_matrix(MATRIX_PATH)
        write_report(matrix, REPORT_PATH)
    except FileNotFoundError:
        print(f"Файл не найден: {MATRIX_PATH.name}")
    except UnicodeError:
        print("Ошибка кодировки входного файла")
    except ValueError as error:
        print(f"Ошибка формата: {error}")
    except OSError as error:
        print(f"Ошибка доступа к файлу: {error}")
    else:
        print(f"Отчёт сохранён: {REPORT_PATH.name}")


if __name__ == "__main__":
    main()
