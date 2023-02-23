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
def find_sum_between(array: []):
    first_positive_index = None
    last_positive_index = None
    for i in range(0, len(array)):
        item = array[i]
        if item > 0 and first_positive_index is None:
            first_positive_index = i
            last_positive_index = i
        elif item > 0:
            last_positive_index = i
    print(f'Первый положительный элемент: {array[first_positive_index]}, последний {array[last_positive_index]}')
    print(f'Элементы между первым и последним положительными значениями\n'
          f'{array[first_positive_index + 1 : last_positive_index]}\n'
          f'их сумма = {round(sum(array[first_positive_index + 1 : last_positive_index]), 1)}')


def set_to_zero_negative_elements(array: []) -> []:
    return list(map(lambda i: 0.0 if i < 0.0 else i, array))


# ------------------------- Start program -------------------------
array_length = set_natural_number("Введите длину массива (макс=30)", range(1, 31))
random_array = get_random_float_array(array_length, range(-5, 5), True)
print(f'Массив: {random_array}')
print_divider()

print(f'Минимальный элемент: {min(random_array)}')
print_divider()

find_sum_between(random_array)
print_divider()

zeroed_array = set_to_zero_negative_elements(random_array)
print(f'Обнуленный массив: {zeroed_array}')
print(f'Отсортированный массив: {sorted(zeroed_array, key=lambda i: i != 0)}')


input('\nНажмите <ENTER> для завершения')

