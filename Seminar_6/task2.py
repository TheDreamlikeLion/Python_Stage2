# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числаЖ нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки "больше" и "меньше".
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

import random as rnd
from sys import argv
from puzzle_mystery import puzzle as p
from puzzle_mistery_with_dict import new_puzzle as new_p
from puzzle_mistery_with_dict import show_statistic
import leap_year

__all__ = ['guess']

def guess(lower: int = 0, upper: int = 100, count: int = 10) -> bool:
    number = rnd.randint(lower, upper)
    search_count = 0
    for nn in range(1, count + 1):
        answer = int(input(f"Попытка №{nn}, введите число от {lower} до {upper}: "))
        if answer > number:
            print(f"Число {answer} больше загаданного.")
        elif answer < num:
            print(f"Число {answer} меньше загаданного.")
        else:
            return True
    return False


__name__ == '__main__':
    print(guess())