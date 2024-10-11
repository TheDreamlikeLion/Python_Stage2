# Дорабатываем функции из предыдущих задач.
# Генерируйте файлы в указанную директорию - отдельный параметр функции.
# Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки)
# Существующие файлы не должны удаляться/изменяться в случае совпадения имен.

import os
from random import randint, choices
from pathlib import Path
from string import ascii_lowercase, digits


__all__ = ['generate_file', 'create_file']


def create_file(extension: str, min_len: int = 6, max_len: int = 30, min_size: int = 256, max_size: int = 4096, count: int = 42) -> None:
    for _ in range(count):
        print(Path.cwd())
        while True:
            file_name = ''.join(choices(ascii_lowercase+digits+'_', k=randint(min_len, max_len)))+'.'+ extension
            if not Path(file_name).is_file():
                break
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        print(f'Создан файл {file_name}')
        with open(file_name, 'wb') as f:
            f.write(data)


def generate_file(filepath: str|Path, **kwargs) -> None:
    if isinstance(filepath, str):
        filepath = Path(filepath)
    if not filepath.is_dir():
        filepath.mkdir(parents=True)
    os.chdir(filepath)
    for extension, amount in kwargs.items():
        try:
            create_file(extension, count = amount)
        except FileExistsError:
            print(f'Такой файл уже существует.')


if __name__ == '__main__':
    os.chdir('./Seminar_7')
    generate_file('new_dir', txt=2, bin=2)