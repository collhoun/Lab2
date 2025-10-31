from src.hepl_func import create_folder_for_tests, delete_folder_for_tests
from src.rm import do_rm
import pytest
import os


@pytest.fixture(scope="function", autouse=True)
def test_lifecycle():
    create_folder_for_tests()
    yield
    delete_folder_for_tests()


def test_ls_valuerr_1():
    with pytest.raises(ValueError) as e:
        do_rm('..')
    assert 'Запрещена операция удаления родительского каталога' == e.value.args[0]


def test_ls_valuerr_2():
    with pytest.raises(ValueError) as e:
        do_rm('/')
    assert 'Запрещена операция удаления корневого каталога' == e.value.args[0]


def test_ls_valuerr_3():
    with pytest.raises(ValueError) as e:
        do_rm('.ruff_cache', '-l')
    assert 'Неизветсная опция -l' == e.value.args[0]


def test_ls_filenotfound():
    with pytest.raises(FileNotFoundError) as e:
        do_rm('srccc')
    assert "Файл srccc невозможно удалить так как его не удалось найти" == e.value.args[0]


def test_ls_typeerr():
    with pytest.raises(TypeError) as e:
        do_rm('.ruff_cache')
    assert ".ruff_cache является директорией" == e.value.args[0]


def test_rm_file():
    before = os.path.exists('tests\\folder_for_tests\\some.txt')
    do_rm('tests\\folder_for_tests\\some.txt')
    after = not os.path.exists('tests\\folder_for_tests\\some.txt')
    assert (before and after)


def test_rm_dir(monkeypatch):
    before = os.path.exists('tests\\folder_for_tests\\folder_for_rm')
    # мокируем ввод на y
    monkeypatch.setattr("builtins.input", lambda _: "y")
    do_rm('tests\\folder_for_tests\\folder_for_rm', '-r')
    after = not os.path.exists('tests\\folder_for_tests\\folder_for_rm')
    assert (before and after)


if __name__ == '__main__':
    pytest.main()
