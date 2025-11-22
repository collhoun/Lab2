from src.hepl_func import create_folder_for_tests, delete_folder_for_tests
from src.move import do_move
import pytest
import os


@pytest.fixture(scope="function", autouse=True)
def test_lifecycle():
    create_folder_for_tests()
    yield
    delete_folder_for_tests()


def test_move_filenotfound1():
    with pytest.raises(FileNotFoundError) as e:
        do_move('src/some.py', 'tests')
    assert 'Такого src/some.py файла не существует' == e.value.args[0]


def test_move_filenotfound2():
    with pytest.raises(FileNotFoundError) as e:
        do_move('src/move.py', 'testststststst')
    assert 'Такой директории testststststst не существует' == e.value.args[0]


def test_move_usual():
    before = os.path.exists('tests/folder_for_tests/folder_for_rm/some.txt')
    do_move('tests/folder_for_tests/some.txt',
            'tests/folder_for_tests/folder_for_rm')
    after = os.path.exists('tests/folder_for_tests/folder_for_rm/some.txt')
    assert (not before and after)


def test_move_dir():
    before = os.path.exists(
        'tests/folder_for_tests/folder_for_rm/folder_for_zip_and_tar')
    do_move('tests/folder_for_tests/folder_for_rm',
            'tests/folder_for_tests/folder_for_zip_and_tar')
    after = os.path.exists(
        'tests/folder_for_tests/folder_for_zip_and_tar/folder_for_rm')
    assert (not before and after)


if __name__ == '__main__':
    pytest.main()
