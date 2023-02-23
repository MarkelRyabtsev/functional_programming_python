import random


# ------------------------- Utility methods -------------------------
def set_natural_number(description: str, numbers_range: range) -> int:
    while True:
        try:
            value = int(input(f'{description} : '))

            if numbers_range is not None and value not in numbers_range:
                print(f'Введенное число должно быть в диапозоне от {numbers_range.start} до {numbers_range.stop - 1}!')
                continue
            return value
        except:
            print('Введенное значение не является натуральным числом, повторите!')
            continue


def get_random_matrix(rows: int, columns: int, values_range: range) -> [[]]:
    random_array = []
    for i in range(0, rows):
        row = []
        for j in range(0, columns):
            row.insert(j, random.randint(values_range.start, values_range.stop))
        random_array.insert(i, row)
    return random_array


def print_matrix(matrix: [[]]):
    for row in matrix:
        for i in range(0, len(row)):
            str_value = str(row[i])
            if len(str_value) == 1:
                str_value = f'  {str_value}'
            elif len(str_value) == 2:
                str_value = f' {str_value}'
            print(f'[{str_value}]', end='')
        print('')


def print_array_vertically(array: []):
    for i in range(0, len(array)):
        str_value = str(array[i])
        if len(str_value) == 1:
            str_value = f'  {str_value}'
        elif len(str_value) == 2:
            str_value = f' {str_value}'
        print(f'[{str_value}]')


def print_divider(): print("--------------------------------------------------------")


# ------------------------- Task methods -------------------------
def find_sum_by_row(matrix: [[]]):
    sum_array = []
    for row in range(0, len(matrix)):
        if any(item < 0 for item in matrix[row]):
            sum_array.insert(row, sum(matrix[row]))
        else:
            sum_array.insert(row, "---")
    print("Суммы элементов в строках, если есть хотя бы один отрицательный")
    print_array_vertically(sum_array)


def find_saddle_points(matrix: [[]]):
    saddle_points_array = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if is_saddle_point(matrix, i, j):
                saddle_points_array.append((i, j))
    print(f'Седловые точки матрицы: {"Отсутствуют" if len(saddle_points_array) == 0 else saddle_points_array}')


is_saddle_point = lambda matrix, i, j: matrix[i][j] == min(matrix[i]) and matrix[i][j] == max([row[j] for row in matrix])


# ------------------------- Start program -------------------------
row_count = set_natural_number("Количество строк", range(1, 11))
column_count = set_natural_number("Количество столбцов", range(1, 11))
random_matrix = get_random_matrix(row_count, column_count, range(-5, 9))
#test_saddle_point_matrix = [[7, 1, 5, 3], [3, 2, 6, 4], [5, 2, 8, 6]]
print_matrix(random_matrix)
print_divider()

find_sum_by_row(random_matrix)
print_divider()

find_saddle_points(random_matrix)

input('\nНажмите <ENTER> для завершения')

