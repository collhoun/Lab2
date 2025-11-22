from logging import getLogger

logger = getLogger(__name__)


def do_history(number_of_commands: int) -> None:
    """print last number_of_commands commands

    Args:
        number_of_commands (int): number of commands user wants to check
    """
    with open('src/.history', 'r', encoding='utf-8') as file:
        i = 0
        for string in file.readlines()[::-1]:
            if i == int(number_of_commands):
                break
            print(f'{i+1}) {string}')
            i += 1
    logger.info('history %d', number_of_commands)


def write_history_file(command: str, path_to_history: str) -> None:
    """write command user uses in file src/.history

    Args:
        command (str): command user uses
    """
    with open(f'{path_to_history}/src/.history', 'a', encoding='utf-8') as file:
        file.write(f'{command}\n')
    logger.info('записана команда %s в src/.history', command)
