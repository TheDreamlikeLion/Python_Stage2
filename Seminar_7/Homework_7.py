# Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.


from pathlib import Path
import os


def rename_files(current_extension: str, desired_extension: str, count_nums: int = 3, range_min: int = 0, range_max: int = 5, disered_name: Path = '') -> None:
    filepath = Path(Path().cwd())
    serial_num = 1
    try:
        for obj in filepath.iterdir():
            if count_nums > 0:
                param="%0"+str(count_nums)+"d"
                serial_number = param % serial_num
            else:
                serial_number = ''
            print(obj)
            full_name = str(obj).split('\\')[-1]
            file_name, file_extension = full_name.split('.')
            if file_extension == current_extension:
                Path(full_name).rename(f'{disered_name}{file_name_generator(file_name, range_min, range_max)}{serial_number}.{desired_extension}')
                serial_num += 1
    except:
        print('Не во всех файлах в директории есть расширение')


def file_name_generator(current_name: str, range_min: int, range_max: int) -> str:
    return current_name[range_min:range_max]


if __name__ == '__main__':
    os.chdir('./Seminar_7/new_dir')
    rename_files(current_extension='txt', desired_extension='doc', disered_name='filename_')
    rename_files(current_extension='bin', desired_extension='log', count_nums = 4, range_min = 0, range_max = 5)