import math
from decimal import Decimal
import sys
from tabulate import tabulate


def set_real_number(description: str, only_positive: bool = False, not_equal: float = None) -> float:
    while True:
        try:
            value = float(input(f'{description} : '))
            if only_positive:
                if value <= 0:
                    print(f'Введенное число должно быть больше 0!')
                    continue
            if not_equal is not None and value == not_equal:
                print(f'Введенное число должно отличаться от {not_equal}!')
                continue
            return value
        except:
            print('Введенное значение не является вещественным числом, повторите!')
            continue


def sequence_element(x: float, n: int) -> float:
    return math.pow(x, n) / n


def find_root(x: float, eps: float, n: int = 1, element: float = None, sum: float = 0.0):
    if element is not None:
        if abs(element) <= eps:
            return -(sum - element), n
        else:
            n += 1
            sum += element
    return find_root(x=x, eps=eps, n=n, element=sequence_element(x, n), sum=sum)


print("Вычислить и вывести на экран в виде таблицы значения функции, заданной с помощью ряда Тейлора,\n"
      "на интервале от Xнач до Xкон с шагом dx с точностью ε. Таблицу снабдить заголовком и шапкой.\n"
      "Каждая строка таблицы должна содержать значение аргумента, значение функции и количество просуммированных\n"
      "членов ряда. Диапазон изменения переменной Х, шаг dx, точность ε вводить с консоли.")
step = set_real_number("Введите шаг dx", only_positive=True)
eps = set_real_number("Введите точность ε", only_positive=True)
print("--------------------------------------------------------")
print("Значения функции ln(1-x) = -(x + x^2/2 + x^3/3 + ...)")
table = []
header = ["Аргумент (х)", "Значение функции", "Количество суммирований"]
x_start = -1 + step
x_end = 1
sys.setrecursionlimit(50000)
while x_start <= x_end:
    root = find_root(round(x_start, 1), eps)
    table.append([round(x_start, 1), root[0], root[1]])
    x_start += step
print(tabulate(table, header))

input('\nНажмите <ENTER> для завершения')
