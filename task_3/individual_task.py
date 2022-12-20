import math


def set_natural_number(description: str, numbers_range: range = None, all_numbers: bool = False) -> int:
    while True:
        try:
            value = int(input(f'{description} : '))
            if not all_numbers:
                if value < 1:
                    print('Число должно быть больше 0!')
                    continue
            if numbers_range is not None and value not in numbers_range:
                print(f'Введенное число должно быть в диапозоне от {numbers_range.start} до {numbers_range.stop}!')
                continue
            return value
        except:
            print('Введенное значение не является натуральным числом, повторите!')
            continue


solve_func_1 = lambda x: 2 * x

solve_func_2 = lambda x: x**2

solve_func_3 = lambda x: x / 3

function_y = lambda a, b, x, fi: ((2/3) * a * math.sin(x)**2) - (((3*b)/4) * math.cos(fi(x))**2)


print("Вычислить значение y в зависимости от выбранной функции fi(x)")
a = set_natural_number("Введите значение a", all_numbers=True)
b = set_natural_number("Введите значение b", all_numbers=True)
z = set_natural_number("Введите значение z", all_numbers=True)

print("Выберите функцию fi(x):")
print("1) fi(x) = 2x")
print("2) fi(x) = x^2")
print("3) fi(x) = x/3")
function_number = set_natural_number("Введите номер функции", range(1, 3))

selected_function = None
selected_function_string = ""
if function_number == 1:
    selected_function = solve_func_1
    selected_function_string = "2x"
elif function_number == 2:
    selected_function = solve_func_2
    selected_function_string = "x^2"
else:
    selected_function = solve_func_3
    selected_function_string = "x/3"

x = None
if z < 0:
    x = z
else:
    x = math.sin(z)

print(f'При fi(x) = {selected_function_string}, x = {round(x, 4)}  =>  y = {round(function_y(a, b, x, selected_function), 4)}')

input('\nНажмите <ENTER> для завершения')
