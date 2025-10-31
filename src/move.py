import os
import shutil
# from src.constants import WRONG_SYMBOLS
from logging import getLogger

logger = getLogger(__name__)


def do_move(file_to_move: str, target_dir: str) -> None:
    """move file from current dir to target dir

    Args:
        file_to_move (str): file user want to move
        target_dir (str): dir user want to move in file

    Raises:
        FileNotFoundError: no such file
        FileNotFoundError: no such dir
        ValueError : non correct name of dir
    """

    if not os.path.exists(file_to_move):
        logger.error("Ошибка: такого %s файла не существует", file_to_move)
        raise FileNotFoundError(f"Такого {file_to_move} файла не существует")
    elif not os.path.exists(target_dir):
        logger.error("Ошибка: такого %s каталога не существует", target_dir)
        raise FileNotFoundError(f"Такой директории {target_dir} не существует")
    else:

        logger.info("mv %s %s", file_to_move, target_dir)
        shutil.move(file_to_move, target_dir)


if __name__ == '__main__':
    pass
