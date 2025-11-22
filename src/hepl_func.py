import os
import shutil
import pathlib


def tokenizator(expr: str) -> list:
    """make semantic parts of expression

    Args:
        expr (str): user's command

    Returns:
        list: return string that has been splited by whitespace
    """
    while '  ' in expr:
        expr = expr.replace('  ', ' ')
    if '"' in expr or "'" in expr:
        l_expr = list(expr)
        expr = expr.replace('"', "'")  # будем работать с одинарными кавычками
        is_kavichka_open = False
        is_kavichka_close = False
        for ind, char in enumerate(expr):
            if char == "'" and not is_kavichka_close and is_kavichka_open:
                is_kavichka_close = True
            if char == "'" and not is_kavichka_open:
                is_kavichka_open = True

            if is_kavichka_open and not is_kavichka_close and char == ' ':
                l_expr[ind] = '!'

        expr = ''.join(l_expr).split()  # type: ignore

        for ind, cur_val in enumerate(expr):
            if '!' in cur_val:
                expr[ind] = expr[ind].replace('!', ' ')  # type: ignore

        return expr  # type: ignore

    else:
        tokens = expr.split()

        return tokens


def create_folder_for_tests():

    os.mkdir('tests/folder_for_tests')
    file = pathlib.Path('tests/folder_for_tests/some.txt')
    file.touch(exist_ok=True)
    with open('tests/folder_for_tests/some.txt', 'w') as file:
        file.write('something')

    # zipper
    os.mkdir('tests/folder_for_tests/folder_for_zip_and_tar')
    file = pathlib.Path(
        'tests/folder_for_tests/folder_for_zip_and_tar/one.txt')
    file.touch(exist_ok=True)
    with open('tests/folder_for_tests/folder_for_zip_and_tar/one.txt', 'w') as file:
        file.write('one txt lalalala')
    file = pathlib.Path(
        'tests/folder_for_tests/folder_for_zip_and_tar/two.txt')
    file.touch(exist_ok=True)
    with open('tests/folder_for_tests/folder_for_zip_and_tar/two.txt', 'w') as file:
        file.write('two txt lalalla')
    # rm
    os.mkdir('tests/folder_for_tests/folder_for_rm')
    file = pathlib.Path('tests/folder_for_tests/folder_for_rm/one_1.txt')
    file.touch(exist_ok=True)
    with open('tests/folder_for_tests/folder_for_rm/one_1.txt', 'w') as file:
        file.write('another one')
    file = pathlib.Path('tests/folder_for_tests/folder_for_rm/two_2.txt')
    file.touch(exist_ok=True)
    with open('tests/folder_for_tests/folder_for_rm/two_2.txt', 'w') as file:
        file.write('antorher two')


def delete_folder_for_tests():
    shutil.rmtree('tests/folder_for_tests')
