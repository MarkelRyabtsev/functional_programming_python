import math


def set_real_number(description: str, only_positive: bool = False, not_equal: float = None) -> float:
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


result = lambda x, y, z: math.sqrt(10 * (math.pow(x, 1/3) + math.pow(x, y + 2))) \
                         * (math.pow(math.asin(z), 2) - abs(x - y))

round_result = lambda x: round(x, 6)

print("Создать программу вычисления указанной величины."
      "\nРезультат проверить при заданных исходных значениях. Результат при заданных значениях = -40.630694")
print("Введите исходные данные (x=0.01655, y=-2.75, z=0.15)")
x = set_real_number("x")
y = set_real_number("y")
z = set_real_number("z")
print(f'Ответ: {round_result(result(x, y, z))}')

input('\nНажмите <ENTER> для завершения')
