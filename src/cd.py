import os
from logging import getLogger

logger = getLogger(__name__)


def do_cd(path_to: str) -> None:
    """allows user to go to another catalog "path_to"

    Args:
        path_to (str): catalog user wanted to visit

    Raises:
        FileNotFoundError: if there is no such dir user want to visit
        TypeError: if path_to is not dir
    """
    if path_to == '..':
        logger.info("cd ..")
        os.chdir('..')
    elif path_to == '~':
        # заменяет начальный компонент пути, начинающийся с символа '~', на полный путь к домашнему каталогу.
        home_dir = os.path.expanduser("~")
        logger.info("cd ~")
        os.chdir(home_dir)
    else:
        if os.path.exists(path_to):
            if os.path.isdir(path_to):
                logger.info("cd %s", path_to)
                os.chdir(path_to)
            else:
                logger.error(
                    "Ошибка: попытка перейти не в каталог")
                raise TypeError(f'Имя {path_to} не является каталогом')
        else:
            logger.error(
                "Ошибка: попытка перейти в несуществующий каталог")
            raise FileNotFoundError(
                'Попытка перейти в несуществующий каталог')
