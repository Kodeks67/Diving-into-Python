import os
import sys
from collections import namedtuple
import logging

# Настройка логирования
logging.basicConfig(filename="directory_contents.log", level=logging.INFO, format='%(message)s')

# Определение namedtuple для хранения информации о файлах и каталогах
FileInfo = namedtuple('FileInfo', 'name extension is_directory parent_directory')


def analyze_directory(directory_path):
    # Проверка существования директории
    if not os.path.exists(directory_path):
        logging.error(f"The directory {directory_path} does not exist.")
        return

    # Перебор всех файлов и каталогов в указанной директории
    for entry in os.listdir(directory_path):
        full_path = os.path.join(directory_path, entry)
        if os.path.isdir(full_path):
            # Это каталог
            info = FileInfo(name=entry, extension=None, is_directory=True,
                            parent_directory=os.path.basename(directory_path))
        else:
            # Это файл
            name, extension = os.path.splitext(entry)
            info = FileInfo(name=name, extension=extension, is_directory=False,
                            parent_directory=os.path.basename(directory_path))

        # Запись информации в лог
        logging.info(info)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    path = sys.argv[1]
    analyze_directory(path)