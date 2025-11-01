from src.hepl_func import create_folder_for_tests, delete_folder_for_tests
from src.undo import do_undo
from src.rm import do_rm
from src.cp import do_cp
from src.move import do_move
import pytest
import os
import shutil


@pytest.fixture(scope="function", autouse=True)
def test_lifecycle():
    create_folder_for_tests()
    yield
    delete_folder_for_tests()
    if os.path.exists('src\\.trash'):
        shutil.rmtree('src\\.trash')


def test_undo_valuerr():
    with pytest.raises(ValueError) as e:
        do_undo('grep', ['lala'])
    assert 'Невозможно отменить действие команды grep' == e.value.args[0]


def test_undo_rm_rec(monkeypatch):
    # мокируем ввод на y
    monkeypatch.setattr("builtins.input", lambda _: "y")
    do_rm('tests\\folder_for_tests\\folder_for_rm', '-r')
    before = not os.path.exists('tests\\folder_for_tests\\folder_for_rm')
    do_undo(
        'rm', ['-r', 'tests\\folder_for_tests\\folder_for_rm', 'C:\\Users\\Huawei\\python_programming\\python_labs\\Lab2'])
    after = os.path.exists('tests\\folder_for_tests\\folder_for_rm')
    assert (before and after)


def test_undo_cp_rec(monkeypatch):
    do_cp('tests\\folder_for_tests\\folder_for_rm',
          'tests\\folder_for_tests\\folder_for_zip_and_tar', '-r')
    before = os.path.exists(
        'tests\\folder_for_tests\\folder_for_zip_and_tar\\folder_for_rm')
    # мокируем ввод на y
    monkeypatch.setattr("builtins.input", lambda _: "y")
    do_undo(
        'cp', ['-r', 'tests\\folder_for_tests\\folder_for_rm', 'tests\\folder_for_tests\\folder_for_zip_and_tar', 'C:\\Users\\Huawei\\python_programming\\python_labs\\Lab2'])
    after = not os.path.exists(
        'tests\\folder_for_tests\\folder_for_zip_and_tar\\folder_for_rm')
    assert before and after


def test_undo_cp_non_rec():
    do_cp('tests\\folder_for_tests\\some.txt',
          'tests\\folder_for_tests\\folder_for_zip_and_tar')
    before = os.path.exists(
        'tests\\folder_for_tests\\folder_for_zip_and_tar\\some.txt')
    do_undo(
        'cp', ['tests\\folder_for_tests\\some.txt', 'tests\\folder_for_tests\\folder_for_zip_and_tar', 'C:\\Users\\Huawei\\python_programming\\python_labs\\Lab2'])
    after = not os.path.exists(
        'tests\\folder_for_tests\\folder_for_zip_and_tar\\some.txt')
    assert before and after


def test_undo_mv():
    do_move('tests\\folder_for_tests\\folder_for_rm',
            'tests\\folder_for_tests\\folder_for_zip_and_tar')
    before = os.path.exists(
        'tests\\folder_for_tests\\folder_for_zip_and_tar\\folder_for_rm')
    do_undo(
        'mv', ['tests\\folder_for_tests\\folder_for_rm', 'tests\\folder_for_tests\\folder_for_zip_and_tar', 'C:\\Users\\Huawei\\python_programming\\python_labs\\Lab2'])
    after = not os.path.exists(
        'tests\\folder_for_tests\\folder_for_zip_and_tar\\folder_for_rm')
    assert before and after


if __name__ == '__main__':
    pytest.main()
