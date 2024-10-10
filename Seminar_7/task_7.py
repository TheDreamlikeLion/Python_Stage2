# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

from pathlib import Path
import os
#from task_6_hw import generate_files
import task_6_hw as generator

__all__ = ['sort_files']


def sort_files(directory: str) -> None:
    extensions = {
        'video': ['mp4', 'mov', 'avi', 'mpg', 'mpeg'],

        'data': ['csv', 'db', 'log', 'mdb', 'xml'],

        'audio': ['mp3', 'wav', 'midi', 'wma', 'cda'],

        'image': ['jpg', 'jpeg', 'png', 'bmp', 'ps'],
        
        'text': ['txt', 'doc', 'docx', 'log'],

        'programs': ['exe', 'vbs', 'bat'],
    }
    if not Path(directory).is_dir():
        directory = Path().cwd() / directory
        Path(directory).mkdir(parents=True)
        generator.generate_files(['txt', 'mp4', 'avi', 'csv', 'mp3', 'wav', 'pdf', 'txt', 'doc'], 10, directory)
        
    files_to_sort = [file.split('.') for dirs, folders, files in os.walk(directory) for file in files]
    
    print('\nНачинаем сортировку.\n')

    for (name, ext) in files_to_sort:
        for k, v in extensions.items():
            if ext in v:
                new_dir = Path().cwd() / directory / k
                if new_dir.is_dir():
                    old_dir = Path(directory) / f'{name}.{ext}'
                    old_dir = old_dir.replace(new_dir / f'{name}.{ext}')
                else:
                    Path(new_dir).mkdir(parents=True)
                    old_dir = Path(directory) / f'{name}.{ext}'
                    old_dir = old_dir.replace(new_dir / f'{name}.{ext}')
                print(f'{new_dir}\{name}.{ext}')


if __name__ == '__main__':
    os.chdir('./Seminar_7')
    sort_files('Test_folder')