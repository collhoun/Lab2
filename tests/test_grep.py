from src.hepl_func import create_folder_for_tests, delete_folder_for_tests
from src.grep import do_grep
import pytest


@pytest.fixture(scope="function", autouse=True)
def test_lifecycle():
    create_folder_for_tests()
    yield
    delete_folder_for_tests()


def test_filenotfound():
    with pytest.raises(FileNotFoundError) as e:
        do_grep('src\\cats.py', 'tests\\folder_fro')
    assert 'Файла tests\\folder_fro не существует в данной директории' == e.value.args[0]


def test_grep_usual(capsys):
    do_grep('some', 'tests\\folder_for_tests')
    capture = capsys.readouterr()
    assert capture.out == 'filename = some.txt, string number = 1, pattern = some\n'


def test_grep_no_register(capsys):
    do_grep('Some', 'tests\\folder_for_tests', '-i')
    capture = capsys.readouterr()
    assert capture.out == 'filename = some.txt, string number = 1, pattern = Some\n'


def test_grep_rec_search(capsys):
    do_grep('one txt lal', 'tests\\folder_for_tests\\folder_for_zip_and_tar', '-r')
    capture = capsys.readouterr()
    assert capture.out == 'filename = tests\\folder_for_tests\\folder_for_zip_and_tar\\one.txt, string number = 1, pattern = one txt lal\n'


if __name__ == '__main__':
    pytest.main()
