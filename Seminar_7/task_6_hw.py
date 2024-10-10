# Дорабатываем функции из предыдущих задач.
# Генерируйте файлы в указанную директорию - отдельный параметр функции.
# Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки)
# Существующие файлы не должны удаляться/изменяться в случае совпадения имен.

import os
from random import randint, choice, choices
from pathlib import Path
from string import ascii_lowercase, digits


__all__ = ['generate_files']


def generate_files(extensions: list[str], filecount: int, directory=Path().cwd()):
    ext = [choice(extensions) for _ in range(filecount)]
    if Path(directory).is_dir():
        os.chdir(directory)
    else:
        directory = Path().cwd() / directory
        Path(directory).mkdir(parents=True)
        os.chdir(directory)
        #print(directory)
    for x in ext:
        try:
            create_file(x,count=1)
        except FileExistsError:
            print(f'Такой файл уже существует')


def create_file(extension: str, min_len: int = 6, max_len: int = 30, min_size: int = 256, max_size: int = 4096, count: int = 42) -> None:
    for _ in range(count):
        #print(Path.cwd())
        while True:
            file_name = ''.join(choices(ascii_lowercase+digits+'_', k=randint(min_len, max_len)))+'.'+ extension
            if not Path(file_name).is_file():
                break
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        print(f'Создан файл {file_name}')
        with open(file_name, 'wb') as f:
            f.write(data)



if __name__ == '__main__':
    os.chdir('./Seminar_7')
    generate_files('new_dir', txt=2, bin=2)