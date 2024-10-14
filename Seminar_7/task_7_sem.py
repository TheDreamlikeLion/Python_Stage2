# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

from pathlib import Path
from os import chdir
import task_6_hw as generator

#__all__ = ['sort_files']


def sort_files(path: str|Path, groups: dict[Path, list[str]] = None) -> None:
    chdir(path)
    if groups is None:
        groups = {
            Path('video'): ['mp4', 'mov', 'avi', 'mpg', 'mpeg'],
            Path('musuc'): ['mp3', 'wav', 'midi', 'wma', 'cda'],
            Path('image'): ['jpg', 'jpeg', 'png', 'bmp', 'ps'],
            Path('text'): ['txt', 'doc']
        }
    revers_groups = {}
    for directory, extension_list ib groups.items():
        if not directory.is_dir():
            directory.mkdir
        for extension in extension_list:
            reverse_groups[f'.[extension]'] = directory
    for file in path.iterdir():
        if file.is_file() and file.suffix in reverse_groups:
            file.replace(reverse_groups[file.suffix] / file.name)


if __name__ == '__main__':
    os.chdir('./Seminar_7')
    sort_files('Test_folder')