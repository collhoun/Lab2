import re
import os
from logging import getLogger, basicConfig, DEBUG
from src.hepl_func import tokenizator
from src.constants import COMMANDS_DICTIONARY, PATH_TO_HISTORY
from src.history import write_history_file


logger = getLogger()
format = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
basicConfig(filename='src/shell.log', encoding='utf-8',
            level=DEBUG, format=format, filemode='w')


def main() -> None:

    dict_of_commands_for_undo: dict = {'rm': None, 'cp': None, 'mv': None}

    print(os.getcwd())
    expression = input()
    while expression != 'q':

        try:
            match = re.search(r'-[a-zA-Z]', expression)
            command, *tokens_list = tokenizator(expression)
            if command in dict_of_commands_for_undo.keys():
                dict_of_commands_for_undo[command] = (
                    command, tokens_list+[os.getcwd()])
            if command not in COMMANDS_DICTIONARY:
                raise KeyError(f'Не существует команды {command}')
            if command == 'undo':
                COMMANDS_DICTIONARY[command](
                    dict_of_commands_for_undo[tokens_list[0]][0], dict_of_commands_for_undo[tokens_list[0]][1])
                print(os.getcwd())
                continue
            if match:
                option, *tokens_list = tokens_list
                COMMANDS_DICTIONARY[command](
                    *tokens_list, option=option)
                write_history_file(command, PATH_TO_HISTORY)
                print(os.getcwd())
                print('\n')
            else:
                COMMANDS_DICTIONARY[command](*tokens_list)
                write_history_file(command, PATH_TO_HISTORY)
                print(os.getcwd())
                print('\n')
        except ValueError as v:
            print(v)
        except FileNotFoundError as f:
            print(f)
        except TypeError as t:
            print(t)
        except KeyError as k:
            print(k)
        except Exception as e:
            print(e)
        finally:
            expression = input()


if __name__ == "__main__":
    main()
