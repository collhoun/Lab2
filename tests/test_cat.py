import pytest
from src.cat import do_cat
from src.hepl_func import create_folder_for_tests, delete_folder_for_tests
import os


@pytest.fixture(scope="function", autouse=True)
def test_lifecycle():
    create_folder_for_tests()
    yield
    delete_folder_for_tests()


def test_cat_filenotfound():
    with pytest.raises(FileNotFoundError) as e:
        do_cat('tests/double.py')
    assert "Файла tests/double.py не существует в текущем каталоге" == e.value.args[
        0]


def test_cat_valuserr():
    with pytest.raises(ValueError) as e:
        do_cat('src')
    assert "Имя src не является файлом. Невозможно отобразить информацию" == e.value.args[
        0]


def test_do_cat_1(capsys):
    do_cat('tests/folder_for_tests/some.txt')
    # перехват выходного потока в переменную capture
    capture = capsys.readouterr()
    assert capture.out == 'something\n'


def test_do_cat_2(capsys):
    do_cat('tests/folder_for_tests/folder_for_rm/one_1.txt')
    # перехват выходного потока в переменную capture
    capture = capsys.readouterr()
    assert capture.out == 'another one\n'


def test_do_cat_3(capsys):
    cur_dir = os.getcwd()
    do_cat(f'{cur_dir}/tests/folder_for_tests/folder_for_rm/one_1.txt')
    # перехват выходного потока в переменную capture
    capture = capsys.readouterr()
    assert capture.out == 'another one\n'


if __name__ == '__main__':

    pytest.main()
