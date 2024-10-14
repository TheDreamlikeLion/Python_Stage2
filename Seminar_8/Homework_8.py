# Напишите функцию, которая получает на вход директорию и
# рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# - Для дочерних объектов указывайте родительскую директорию.
# - Для каждого объекта укажите файл это или директория.
# - Для файлов сохраните его размер в байтах, а для директорий размер
#   файлов в ней с учётом всех вложенных файлов и директорий.


import csv
import json
import os
import pickle


__all__ = ['scan_dirs', 'write_pickle', 'write_json', 'write_csv']


def scan_dirs(current_dir: str) -> dict[int:{str: str | int}]:
    sum_dir_size = 0
    dir_dict = {}
    for i, file in enumerate(os.listdir(current_dir), 1):
        path = os.path.join(current_dir, file)
        object_dict = {'name': path.split('\\')[-1], 'parent': path.split('\\')[-2], 'type': None, 'size': None}
        dir_dict[i] = object_dict
        if os.path.isfile(path):
            #object_dict['size'] = f'{round(os.path.getsize(path)/1024, 2)} kb'
            object_dict['size'] = f'{os.path.getsize(path)} b'
            object_dict['type'] = 'File'#types[0]
        elif os.path.isdir(path):
            #sum_dir_size += round(os.path.getsize(path)/1024, 2)
            sum_dir_size += os.path.getsize(path)
            object_dict['size'] = f'{sum_dir_size} b'
            object_dict['type'] = 'Dir'#types[1]
            dir_dict.update(scan_dirs(path))
    return dir_dict


def write_json(file, data: dict[int:{str: str | int}]) -> None:
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def write_csv(file, data: dict[int:{str: str | int}]) -> None:
    with open(file, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC, delimiter='\t')
        writer.writerow(('id', 'name', 'parent', 'type', 'size'))
        for k, v in data.items():
            writer.writerow((k, v['name'], v['parent'], v['type'], v['size']))


def write_pickle(file, data: dict[int:{str: str | int}]) -> None:
    with open(file, 'wb') as f:
        pickle.dump(data, f)



if __name__ == '__main__':
    dir_inventory = scan_dirs('C:\\GitFolder\\Python_stage2\\Python_Stage2')
    write_pickle('dir_info.pickle', dir_inventory)
    write_csv('dir_info.csv', dir_inventory)
    write_json('dir_info.json', dir_inventory)