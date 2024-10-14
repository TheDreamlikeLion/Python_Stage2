# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните idдо 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хэш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка csv представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.


import csv
import json
from pathlib import Path


def csv_to_json(csv_file: Path, json_file: Path) -> None:
    with (open(csv_file, 'r', newline='', encoding='utf-8') as f_read:
        csv_read = csv.reader(f_read, dialect='excel-tab')
        for i, line in enumerate(csv_read):
            json_dict = {}
            if i != 0:
                level, id, name = line
                json_dict['level'] = int(level)
                json_dict['id'] = f'{int(id):010}'
                json_dict['name'] = name.title()
                json_dict['hash'] = hash(f"{json_dict['name']}{json_dict['id']}")
                json_list.append(json_dict)
            
    with open(json_file, 'w', encoding='utf-8') as f_write:
        json.dump(json_list, f_write, indent=2)

    except FileNotFoundError:
        return 'Файл не найден'


if __name__ == '__main__':
    csv_to_json(Path('users.csv'), Path('new_users.json'))