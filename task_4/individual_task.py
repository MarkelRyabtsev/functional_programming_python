
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


print("Индивидуальное задание.")
print("Каждая бактерия делится на 2 в течение одной минуты.\n"
      "В начальный момент имеется одна бактерия. Составить алгоритм, рассчитывающий количество\n"
      "бактерий на заданное Вами целое значение момента времени (ввести с клавиатуры).\n"
      "Результат вывести на экран.\n")

minuts = set_natural_number("Введи количество минут")
count = 1
minuts_counter = 0

while minuts_counter != minuts:
    count *= 2
    minuts_counter += 1

print(f'Через {minuts_counter} мин. количество бактерий: {count}.')

input('\nНажмите <ENTER> для завершения')
