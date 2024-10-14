# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.


import pickle
import csv
from pathlib import Path


__all__ = ['csv_to_pickle']


def csv_to_pickle(file: Path) -> None:
    pickle_list = []
    with open(file, 'r', encoding='utf-8', newline='') as f_read:
        csv_file = csv.reader(f_read, dialect='excel-tab')
        for i, line in enumerate(csv_file):
            #print(i, line)
            if i == 0:
                pickle_keys = line
            else:
                pickle_dict = {k: v for k, vin zip(pickle_keys, line)}
        pickle_list.append(pickle_dict)
    print(pickle.dump(pickle_list))


if __name__ == '__main__':
    csv_to_pickle(Path('new_users.csv'))