from src.hepl_func import create_folder_for_tests, delete_folder_for_tests
from src.cd import do_cd
import pytest
import os


@pytest.fixture(scope="function", autouse=True)
def test_lifecycle():
    create_folder_for_tests()
    yield
    delete_folder_for_tests()


def test_cd_filenotfound():
    with pytest.raises(FileNotFoundError) as e:
        do_cd('tests/some')
    assert 'Попытка перейти в несуществующий каталог' == e.value.args[0]


def test_cd_typeerr():
    with pytest.raises(TypeError) as e:
        do_cd('src/cd.py')
    assert 'Имя src/cd.py не является каталогом' == e.value.args[0]


def test_cd_up():
    cur_dir = os.getcwd().split('/')[:-1]
    do_cd('..')
    new_dir = os.getcwd().split('/')
    os.chdir('Lab2')
    assert cur_dir == new_dir


def test_cd_home():
    cur_path = os.path.abspath('.')
    do_cd('~')
    home_dir = os.getcwd().split('/')[-2]
    os.chdir(cur_path)
    assert home_dir == 'Users'


def test_cd_usual():
    base_abs_path = os.path.abspath('.')
    do_cd('tests/folder_for_tests/folder_for_rm')
    target_abs_cur_path = f'{base_abs_path}/tests/folder_for_tests/folder_for_rm'
    cur_path = os.getcwd()
    os.chdir(base_abs_path)
    assert target_abs_cur_path == cur_path


if __name__ == '__main__':
    pytest.main()
