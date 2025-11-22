import os
import shutil
from logging import getLogger
from src.cp import do_cp

logger = getLogger()


def do_rm(file_to_remove: str, option: str = '') -> None:
    """remove file or dir

    Args:
        file_to_remove (str): file user wants to remove
        option (str, optional) defaults to ''.

    Raises:
        ValueError: user cant del .. dir
        ValueError: user cant del root
        FileNotFoundError: no such file
        ValueError: unexpected option
        ValueError: unable ro remove dir with no '-r' option
    """
    if file_to_remove == '..':
        logger.error(
            'Ошибка: запрещена операция удаления родительского каталога')
        raise ValueError("Запрещена операция удаления родительского каталога")
    if file_to_remove == '/':
        logger.error(
            'Ошибка: запрещена операция удаления корневого каталога')
        raise ValueError("Запрещена операция удаления корневого каталога")

    if not os.path.exists(file_to_remove):
        logger.error("Ошибка: файла %s не существует", file_to_remove)
        raise FileNotFoundError(
            f"Файл {file_to_remove} невозможно удалить так как его не удалось найти")

    if option:
        if option == '-r':
            answer = verification_remove(
                input("Вы точно хотите удалить каталог со всеми файлами? (y/n)"))
            if answer:
                logger.info("rm -r %s", file_to_remove)
                write_trash_file(file_to_remove, option)
                shutil.rmtree(file_to_remove)
        else:
            logger.error("Ошибка: неизвестная опция %s", option)
            raise ValueError(f'Неизветсная опция {option}')

    else:
        if os.path.isfile(file_to_remove):
            logger.info("rm %s", file_to_remove)
            write_trash_file(file_to_remove)
            os.remove(file_to_remove)
        else:
            logger.error("Ошибка: %s является директорией", file_to_remove)
            raise TypeError(
                f"{file_to_remove} является директорией")


def verification_remove(answer: str) -> bool:
    """True if answer is y else False

    Args:
        answer (str): users answer

    Returns:
        bool: True if answer is y else False
    """
    if answer.replace(' ', '') == 'y':
        return True
    else:
        return False


def write_trash_file(path_to_file_to_remove: str, option: str = ''):
    """copy file to rm in .trash and remove it from cur dir

    Args:
        path_to_file_to_remove (str): file user wants to remove
        option (str, optional): if user wants to remove whole dir he uses '-r' option. Defaults to ''.
    """
    try:
        if os.path.exists('src/.trash'):
            do_cp(path_to_file_to_remove, 'src/.trash', option)
        else:
            os.mkdir('src/.trash')
            do_cp(path_to_file_to_remove, 'src/.trash', option)
    except FileExistsError:
        if '/' in path_to_file_to_remove:
            filename = path_to_file_to_remove.split('/')[-1]
        else:
            filename = path_to_file_to_remove
        if option:
            shutil.rmtree(f'src/.trash/{filename}')
        else:
            os.remove(f'src/.trash/{filename}')
        do_cp(path_to_file_to_remove, 'src/.trash', option)
