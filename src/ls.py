import os
import datetime  # преобразование времени в читабельный вид
import stat  # интерпретация результата для os.stat
from logging import getLogger
logger = getLogger(__name__)


def make_ls(option: str = '', directory_path: str = '.') -> list:
    """create a list of all folders and files in dir with files features

    Args:
        option str: allows user to use some options (e.g -l that show size of file in bytes, time of last change and). Defaults to ''.
        directory_path str: allows user to check any dyrectory he wants to see. Defaults to '.' - current dir.

    Raises:
        ValueError: if options is not avaliable
        FileNotFoundError: if there is no such (directory_path) dir
    Returns:
        list[str]: list of files (include folders) in current dir with some features
    """
    if os.path.exists(directory_path):
        if not os.path.isdir(directory_path):
            raise TypeError(
                f'Файл {directory_path} является файлом, а не каталогом')
        result = []
        if not option:
            logger.info('Сформирован список файлов директории %s',
                        directory_path)
            return os.listdir(path=directory_path)

        elif option == '-l':
            for file in os.listdir(path=directory_path):

                if os.path.isfile(file):
                    file_size = os.path.getsize(file)
                    time_of_last_change = datetime.datetime.fromtimestamp(
                        os.path.getmtime(file))
                    file_rules = stat.filemode(os.stat(file).st_mode)

                    result.append(
                        (file, f'{file_size} bytes', time_of_last_change.strftime(r'%Y-%m-%d %H:%M:%S'), file_rules))
                else:
                    result.append(file)

        else:
            logger.error('Использование неизвестной опции %s', option)
            raise ValueError(f"Неизвестная опция {option}")
        logger.info(
            'Сформированн список файлов директории %s с метаданными', directory_path)
        return result
    else:
        logger.error("Обращение к неизвестной директории %s", directory_path)
        raise FileNotFoundError(f'Директории {directory_path} не существует')


def show_ls(list_of_files: list, option: str = '', directory_path: str = '.') -> None:
    """shows list of files and folders in current dir in console

    Args:
        list_of_files (list): list of files with features
    """
    if list_of_files:
        for elem in list_of_files:
            if type(elem) is tuple:  # type: ignore
                print(
                    f'filename = {elem[0]}, size = {elem[1]}, last change = {elem[2]}, rules = {elem[3]}')
            else:
                print(elem)
        logger.info('ls %s %s', option, directory_path)
    else:
        logger.info('ls %s %s empty dir', option, directory_path)
        print("")


def do_ls(directory_path: str = '.', option: str = '') -> None:
    show_ls(make_ls(option, directory_path))


if __name__ == '__main__':
    do_ls('folder_for_tests\\folder_for_rm')
    pass
