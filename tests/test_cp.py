from src.hepl_func import create_folder_for_tests, delete_folder_for_tests
from src.cp import do_cp
import pytest
import os


@pytest.fixture(scope="function", autouse=True)
def test_lifecycle():
    create_folder_for_tests()
    yield
    delete_folder_for_tests()


def test_cp_filenotfound_1():
    with pytest.raises(FileNotFoundError) as e:
        do_cp('src\\cats.py', 'tests')
    assert 'Такого src\\cats.py файла не существует' == e.value.args[0]


def test_cp_filenotfound_2():
    with pytest.raises(FileNotFoundError) as e:
        do_cp('src\\cat.py', 'testes')
    assert 'Такого testes каталога не существует' == e.value.args[0]


def test_cp_typeerr1():
    with pytest.raises(TypeError) as e:
        do_cp('src\\cat.py', 'tests', '-r')
    assert 'Невозможно применить рекурсивное копирование к файлу src\\cat.py, а не каталогу' == e.value.args[
        0]


def test_cp_typeerr2():
    with pytest.raises(TypeError) as e:
        do_cp('src', 'tests')
    assert 'Невозможно нерекурсивно скопировать папку src' == e.value.args[
        0]


def test_cp_valueerr():
    with pytest.raises(ValueError) as e:
        do_cp('src', 'tests', '-a')
    assert 'Неизвестная опция -a для команды cp' == e.value.args[
        0]


def test_cp_rec():
    file_exists = os.path.exists('tests\\folder_for_tests\\folder_for_rm')
    do_cp('tests\\folder_for_tests\\folder_for_rm',
          'tests\\folder_for_tests\\folder_for_zip_and_tar', '-r')
    post_file_exists = os.path.exists(
        'tests\\folder_for_tests\\folder_for_zip_and_tar\\folder_for_rm')
    assert (file_exists and post_file_exists)


def test_cp_not_rec():
    file_exists = os.path.exists('tests\\folder_for_tests\\some.txt')
    do_cp('tests\\folder_for_tests\\some.txt',
          'tests\\folder_for_tests\\folder_for_zip_and_tar')
    post_file_exists = os.path.exists(
        'tests\\folder_for_tests\\folder_for_zip_and_tar\\some.txt')
    assert (file_exists and post_file_exists)


if __name__ == '__main__':
    pytest.main()
