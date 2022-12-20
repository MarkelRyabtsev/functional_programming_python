
def set_natural_number(description: str, numbers_range: range = None, all_numbers: bool = False) -> int:
    while True:
        try:
            value = int(input(f'{description} : '))
            if not all_numbers:
                if value < 1:
                    print('Число должно быть больше 0!')
                    continue
            if numbers_range is not None and value not in numbers_range:
                print(f'Введенное число должно быть в диапозоне от {numbers_range.start} до {numbers_range.stop - 1}!')
                continue
            return value
        except:
            print('Введенное значение не является натуральным числом, повторите!')
            continue


def simple_fibonacci(number: int) -> int:
    if number <= 1:
        return number
    return simple_fibonacci(number - 1) + simple_fibonacci(number - 2)


def all_fibonacci_elements(number: int, elements: []) -> []:
    if number == 0:
        return elements.append(number)
    elements.append(simple_fibonacci(number))
    return all_fibonacci_elements(number - 1, elements)


def all_less_than(limit_number: int, elements: [] = None, number: int = None) -> []:
    if elements is None:
        elements = []
    if number is None:
        number = 0
    else:
        number += 1
    fibonacci_number = simple_fibonacci(number)
    if fibonacci_number > limit_number:
        return elements
    elements.append(fibonacci_number)
    return all_less_than(limit_number, elements, number)


print("Основное задание.\n")

print("1) Вывод конкретного элемента последовательности.")
print("2) Вывод всех элементов последовательности до указанного пользователем элемента.")
print("3) Вывод той части последовательности, значение последнего элемента которой\n"
      "не превосходит введённое пользователем значение")

task_number = set_natural_number("Выберите задание", range(1, 4))
if task_number == 1:
    number = set_natural_number("Введите номер элемента последовательности")
    print(f'{number} элемент равен {simple_fibonacci(number)}')
elif task_number == 2:
    limit_number = set_natural_number("До какого элемента вывести значения")
    limited_list = []
    all_fibonacci_elements(limit_number, limited_list)
    limited_list.reverse()
    print(f'Все элементы до {limit_number}: {limited_list}')
else:
    limit = set_natural_number("Не больше какого числа нужно показать элементы")
    print(f'Все элементы меньше {limit}: {all_less_than(limit)}')

input('\nНажмите <ENTER> для завершения')
