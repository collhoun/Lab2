import os
from logging import getLogger

logger = getLogger(__name__)


def do_grep(pattern: str, path: str, option: str = '') -> None:
    """find pattern in files of path dir
        print name of file where pattern was found, string number and the pattern

    Args:
        pattern (str): something user wants to find in files
        path (str): path of dir where user wants to search in
        option (str, optional): could be -r (recucrsion search in dir) and -i (search without register) Defaults to ''.

    Raises:
        FileNotFoundError: erorr if there is no such dir
    """
    if not os.path.exists(path):
        logger.error('Файла %s не существует в данной директории', path)
        raise FileNotFoundError(
            f'Файла {path} не существует в данной директории')

    if option:
        if option == '-r':
            for root, _, files in os.walk(path):
                for filename in files:
                    file_path = os.path.join(root, filename)
                    with open(file_path, 'r', encoding='utf-8') as file:
                        string_number = 0
                        for line in file.readlines():
                            string_number += 1
                            if pattern in line:
                                print(
                                    f'filename = {file_path}, string number = {string_number}, pattern = {pattern}')
                        logger.info("grep %s %s %s", pattern, path, option)

            pass
        elif option == '-i':
            for file in os.listdir(path):
                if os.path.isfile(f'{path}/{file}'):
                    with open(f'{path}/{file}', 'r', encoding='utf-8') as reading_file:
                        string_number = 0
                        for string in map(str.lower, reading_file.readlines()):
                            string_number += 1
                            if pattern.lower() in string:
                                print(
                                    f'filename = {file}, string number = {string_number}, pattern = {pattern}')
                        logger.info("grep %s %s %s", pattern, path, option)
    else:
        for file in os.listdir(path):
            if os.path.isfile(f'{path}/{file}'):
                with open(f'{path}/{file}', 'r', encoding='utf-8') as reading_file:
                    string_number = 0
                    for string in reading_file.readlines():
                        string_number += 1
                        if pattern in string:
                            print(
                                f'filename = {file}, string number = {string_number}, pattern = {pattern}')
                    logger.info("grep %s %s %s", pattern, path)
