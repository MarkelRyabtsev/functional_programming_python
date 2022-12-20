import math


def set_real_number(
        description: str,
        only_positive: bool = False,
        not_equal: float = None
) -> float:
    while True:
        try:
            value = float(input(f'{description} : '))
            if only_positive:
                if value < 0:
                    print(f'Введенное число должно быть больше 0!')
                    continue
            if not_equal is not None and value == not_equal:
                print(f'Введенное число должно отличаться от {not_equal}!')
                continue
            return value
        except:
            print('Введенное значение не является вещественным числом, повторите!')
            continue


solve_discriminant = lambda a, b, c: b**2 - (4 * a * c)

find_roots = lambda discriminant, a, b: (
    (-b + math.sqrt(discriminant)) / (2 * a),
    (-b - math.sqrt(discriminant)) / (2 * a)
)


print("Программа вычисления квадратного уравнения вида: ax^2 + bx + c = 0")
print("Введите исходные данные:")
a = set_real_number("a", only_positive=True)
b = set_real_number("b")
c = set_real_number("c")

discriminant = solve_discriminant(a, b, c)
print(f'Дискриминант: {discriminant}')

if discriminant > 0:
    result = find_roots(discriminant, a, b)
    print(f'x1={round(result[0], 4)}, x2={round(result[1], 4)}')
elif discriminant == 0:
    result = find_roots(discriminant, a, b)
    print(f'x={round(result[0], 4)}')
else:
    print("Т.к. дискриминант < 0, уравнение корней не имеет.")

input('\nНажмите <ENTER> для завершения')
