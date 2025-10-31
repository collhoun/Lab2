import os
from logging import getLogger

logger = getLogger(__name__)


def do_cat(filename: str) -> str:  # type: ignore
    """push the file content to the powershell

    Args:
        filename (str): name of the file user wants to check

    Raises:
        FileNotFoundError: there is no such file, so it's an exception
        ValueError: the filename is a folder name or something else which is not a file

    Returns:
        str: text from the file
    """
    if os.path.exists(filename) and os.path.isfile(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            logger.info("cat %s", filename)
            print(file.read())

    else:
        if not os.path.exists(filename):
            logger.error(
                'Ошибка: файла %s не существует в текущем каталоге', filename)
            raise FileNotFoundError(
                f"Файла {filename} не существует в текущем каталоге")
        if not os.path.isfile(filename):
            logger.error(
                'Ошибка: имя %s не является файлом. Невозможно отобразить информацию', filename)
            raise ValueError(
                f"Имя {filename} не является файлом. Невозможно отобразить информацию")


if __name__ == '__main__':
    print(do_cat('src\\main.py'))
