import pytest
from src.ls import do_ls
from src.hepl_func import create_folder_for_tests, delete_folder_for_tests


@pytest.fixture(scope="function", autouse=True)
def test_lifecycle():
    create_folder_for_tests()
    yield
    delete_folder_for_tests()


def test_ls_filenotfound():
    with pytest.raises(FileNotFoundError) as e:
        do_ls('srcced')
    assert 'Директории srcced не существует' == e.value.args[0]


def test_ls_valueerr():
    with pytest.raises(ValueError) as e:
        do_ls('src', '-r')
    assert 'Неизвестная опция -r' == e.value.args[0]


def test_ls_typeerr():
    with pytest.raises(TypeError) as e:
        do_ls('src\\main.py', '-l')
    assert 'Файл src\\main.py является файлом, а не каталогом' == e.value.args[0]


def test_ls_usual(capsys):
    do_ls('tests\\folder_for_tests\\folder_for_rm')
    # перехват выходного потока в переменную capture
    capture = capsys.readouterr()
    assert capture.out == 'one_1.txt\ntwo_2.txt\n'


if __name__ == '__main__':
    pytest.main()
