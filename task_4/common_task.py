import random
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


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


def get_random_range(difficulty: int) -> range:
    if difficulty == 1:
        return range(1, 10)
    elif difficulty == 2:
        return range(1, 30)
    else:
        return range(1, 99)


def run_game(random_number: int, counter: int, limit: int):
    print(f'Было попыток: {counter}')
    if limit != 0:
        print(f'Осталось попыток: {limit - counter}')
    number = set_natural_number("Введи своё число", )
    counter += 1
    if limit > 0 and limit == (counter):
        clear()
        print("----------")
        print("GAME OVER!")
        print("----------")
    elif number != random_number:
        clear()
        if number > random_number:
            print("Попробуй ввести число меньше")
        else:
            print("Попробуй ввести число больше")
        run_game(random_number, counter, limit)
    else:
        clear()
        print("Ты угадал!!!")
        print(f'Количество попыток: {counter}')


print("Игра 'Угадай число'\n")
print("Компьютер задумал число в выбранном диапозоне.")
print("Твоя задача: угадать это число за меньшее число шагов.")
print("Каждый раз компьютер будет говорить больше или меньше указанное тобой число.\n")
print("1) Легко (1-10, попыток: 5)")
print("2) Средне (1-30), попыток: 10")
print("3) Сложно (1-99), попыток: 15")

diffilulty = set_natural_number("Выбери сложность", range(1, 4))
use_limits = set_natural_number("Ограничить попытки? (1-да, 2-нет)", range(1, 3))
random_number = random.randint(
    get_random_range(diffilulty).start,
    get_random_range(diffilulty).stop
)
counter = 0
limit = diffilulty * 5 * (use_limits == 1)
run_game(random_number, counter, limit)

input('\nНажмите <ENTER> для завершения')
