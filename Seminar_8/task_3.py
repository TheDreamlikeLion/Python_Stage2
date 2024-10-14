# напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.

import json
import csv
import os

__all__ = ['json_to_csv']


def json_to_csv(file: Path) -> None:
    with open(file, 'r', encoding='utf-8') as f_read:
        data = json.load(f_read)
        
    list_rows = []
    for level, id_name_dict in data.items():
        for id, name in id_name_dict.items():
            list_rows.append({'level': int(level), 'id': int(id), 'name': name})

    with open(f'{file.stem}.csw', 'w', newline='', encoding='utf-8') as f_write:
        csw_write = csv.DictWriter(f_write, fieldnames=['level', 'id', 'name'], dialect='excel-tab')
        csw_write.writeheader()
        csw_write.writerow(list_rows)
    except FileNotFoundError:
        return 'Файл не найден'


if __name__ == '__mani__':
    json_to_csv(Path('users.json'))