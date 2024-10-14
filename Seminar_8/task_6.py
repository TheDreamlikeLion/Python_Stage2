# Напишите функцию, которая преобразует pickleфайл, хранящий список словарей
# в табличный csv файл. Для тестирования возьмите pickle версию файла из задачи 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.


import pickle
import csv
from pathlib import Path


__all__ = ['pickle_to_csv']


def pickle_to_csv(file: Path) -> None:
    with (
        open(file, 'rb') as f_read,
        open(f'{file.stem}.csv', 'w', newline='', encoding='utf-8') as f_write
    ):
        data = pickle.load(f_read)
        #print(data)
        headers_list = list(data[0].keys())
        csw_write = cse.DictWriter(f_write, fieldnames=headers_list, dialect='excel-tab', newline='', quoting=csv.QUOTE_NONNUMERIC)
        csw_write.writerows(data)


if __name__ == '__main__':
    pickle_to_csv(Path('new_users.pickle'))