# Доработайте предыдущую задачу.
# Создайте новую функцию, которая генерирует файлы с разными расширениями.
# Расширения и количество файлов функция принимает в качестве параметров.
# Количество переданных расширений может быть любым.
# Количество файлов для каждого расширения различно.
# Внутри используйте вызов функции из прошлой задачи.

import os
import random as rd
from pathlib import Path
from task_4 import create_file


def generate_file(**kwargs) -> None:
    for extension, amount in kwargs.items():
        try:
            create_file(extension, count = amount)
        except FileExistsError:
            print(f'Такой файл уже существует.')


if __name__ == '__main__':
    os.chdir('./Seminar_7')
    generate_file(bin=2, jpg=1, txt=3)