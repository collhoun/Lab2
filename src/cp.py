import shutil
import os
from logging import getLogger

logger = getLogger(__name__)


def do_cp(file_for_copy: str, target_dir: str, option: str = '') -> None:
    """copy file from current dir to target

    Args:
        file_for_copy (str): file user wants to copy
        target_dir (str): dir user wants to copy in file for copy
        option (str): option to copy

    Raises:
        FileNotFoundError: no such file
        ValueError: impossible to copy with '-r' option file, not dir
        ValueError: unexpected option
        ValueError: unable to copy dit with no 'r'
    """

    if not os.path.exists(file_for_copy):
        logger.error("Ошибка: файла %s не существует", file_for_copy)
        raise FileNotFoundError(
            f'Такого {file_for_copy} файла не существует')

    if not os.path.exists(target_dir):
        logger.error("Ошибка: каталога %s не существует", target_dir)
        raise FileNotFoundError(
            f'Такого {target_dir} каталога не существует')

    if option:
        if option == '-r':
            if os.path.isdir(file_for_copy):
                if '/' in file_for_copy:
                    dir_name = file_for_copy.split('/')[-1]
                else:
                    dir_name = file_for_copy
                logger.info("cp -r %s %s", file_for_copy, target_dir)
                shutil.copytree(
                    file_for_copy, f'{target_dir}/{dir_name}')
            else:
                logger.error(
                    "Ошибка: Невозможно применить рекурсивное копирование к файлу %s", file_for_copy)
                raise TypeError(
                    f"Невозможно применить рекурсивное копирование к файлу {file_for_copy}, а не каталогу")
        else:
            logger.error("Ошибка: неизвестная опция %s для команды cp", option)
            raise ValueError(f"Неизвестная опция {option} для команды cp")
    else:
        if os.path.isfile(file_for_copy):
            logger.info("cd %s %s", file_for_copy, target_dir)
            shutil.copy(file_for_copy, target_dir)
        else:
            logger.error(
                "Ошибка: невозможно нерекурсивно скопировать папку %s", file_for_copy)
            raise TypeError(
                f'Невозможно нерекурсивно скопировать папку {file_for_copy}')
