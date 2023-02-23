import random


# ------------------------- Utility methods -------------------------
def set_real_number(description: str, numbers_range: tuple) -> float:
    while True:
        try:
            value = float(input(f'{description} : '))
            if numbers_range[0] < value < numbers_range[1]:
                return value
            print(f'Введенное число должно быть в диапозоне от {numbers_range[0]} до {numbers_range[1]}!')
        except:
            print('Введенное значение не является вещественным числом, повторите!')
            continue


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


def get_random_float_array(n: int, values_range: range, is_uniq: bool = False) -> []:
    random_array = []
    for i in range(0, n):
        random_value = float(random.randint(values_range.start * 10, values_range.stop * 10) / 10)
        if is_uniq:
            while True:
                if random_value not in random_array:
                    break
                else:
                    random_value = float(random.randint(values_range.start * 10, values_range.stop * 10) / 10)
        random_array.insert(i, random_value)
    return random_array


def print_divider(): print("--------------------------------------------------------")


# ------------------------- Task methods -------------------------
def find_first_two_max_items(array: []):
    first_max = (0, array[0])
    second_max = (0, array[0])
    for i in range(0, len(array)):
        item = abs(array[i])
        if first_max[1] < item:
            second_max = (first_max[0], first_max[1])
            first_max = (i, item)
        elif first_max[1] > item > second_max[1]:
            second_max = (i, item)
    print(f'Первый макс. элемент по модулю: {array[first_max[0]]}, второй {array[second_max[0]]}')


def find_sum_of_abs_values(array: []):
    filtered_values = list(filter(lambda i: abs(i) < 1.0, array))
    print(f'Элементы по модулю < 1: {filtered_values}, их сумма = {round(sum(filtered_values), 1)}')


def set_to_zero_by_max(array: [], max_value: float) -> []:
    return list(map(lambda i: 0.0 if abs(i) > max_value else i, array))


# ------------------------- Start program -------------------------
array_length = set_natural_number("Введите длину массива (макс=30)", range(1, 31))
random_array = get_random_float_array(array_length, range(-5, 5), True)
print(f'Массив: {random_array}')
print_divider()

find_first_two_max_items(random_array)
print_divider()

find_sum_of_abs_values(random_array)
print_divider()

a_max = set_real_number(
    f'Введите пороговое значение (от 0 до {max(random_array)})',
    (0, max(random_array))
)
zeroed_array = set_to_zero_by_max(random_array, a_max)
print(f'Обнуленный массив: {zeroed_array}')
print_divider()
print(f'Исходный массив: {zeroed_array}')
print(f'Отсортированный массив: {sorted(zeroed_array, key=lambda i: i == 0)}')


input('\nНажмите <ENTER> для завершения')

