from src.hepl_func import create_folder_for_tests, delete_folder_for_tests
from src.zipper import do_tar, do_untar, do_unzip, do_zip
import pytest
import os


@pytest.fixture(scope="function", autouse=True)
def test_lifecycle():
    create_folder_for_tests()
    yield
    delete_folder_for_tests()


def test_do_zip_filenotfound():
    with pytest.raises(FileNotFoundError) as e:
        do_zip('srccc', 'src.zip')
    assert "Папки srccc не существует" == e.value.args[0]


def test_do_zip_typeerr():
    with pytest.raises(TypeError) as e:
        do_zip('src\\zipper.py', 'szipper.zip')
    assert "Невозможно архивировать файл src\\zipper.py, а не папку" == e.value.args[0]


def test_do_zip_valuerr():
    with pytest.raises(ValueError) as e:
        do_zip('src', 'szipper')
    assert "Название архива szipper должно содержать расширение .zip" == e.value.args[0]


def test_do_unzip_filenotfound():
    with pytest.raises(FileNotFoundError) as e:
        do_unzip('main.zip', 'src')
    assert "Файла main.zip не существует в данной директории" == e.value.args[0]


def test_do_unzip_valueerr():
    with pytest.raises(ValueError) as e:
        do_unzip('src\\main.py', 'src')
    assert "Название архива src\\main.py должно содержать расширение .zip" == e.value.args[0]


def test_zip():
    before = not os.path.exists(
        'tests\\folder_for_tests\\folder_for_tests.zip')
    do_zip('tests\\folder_for_tests',
           'tests\\folder_for_tests\\folder_for_tests.zip')
    after = os.path.exists('tests\\folder_for_tests\\folder_for_tests.zip')
    assert (before and after)


def test_unzip():
    do_zip('tests\\folder_for_tests',
           'tests\\folder_for_tests\\folder_for_tests.zip')
    before = os.path.exists(
        'tests\\folder_for_tests\\folder_for_tests.zip')
    do_unzip('tests\\folder_for_tests\\folder_for_tests.zip',
             'tests\\folder_for_tests')
    after = os.path.exists('tests\\folder_for_tests\\folder_for_tests.zip')
    assert (after and before)

# --------


def test_do_tar_filenotfound():
    with pytest.raises(FileNotFoundError) as e:
        do_tar('srccc', 'src.tar.gz')
    assert "Папки srccc не существует" == e.value.args[0]


def test_do_tar_typeerr():
    with pytest.raises(TypeError) as e:
        do_tar('src\\zipper.py', 'szipper.tar.gz')
    assert "Невозможно архивировать файл src\\zipper.py, а не папку" == e.value.args[0]


def test_do_tar_valuerr():
    with pytest.raises(ValueError) as e:
        do_tar('src', 'szipper')
    assert "Название архива szipper должно содержать расширение .tar.gz" == e.value.args[0]


def test_do_untar_filenotfound():
    with pytest.raises(FileNotFoundError) as e:
        do_untar('main.tar.gz', 'src')
    assert "Файла main.tar.gz не существует в данной директории" == e.value.args[0]


def test_do_untar_valueerr():
    with pytest.raises(ValueError) as e:
        do_untar('src\\main.py', 'src')
    assert "Название архива src\\main.py должно содержать расширение .tar.gz" == e.value.args[0]


def test_tar():
    before = not os.path.exists(
        'tests\\folder_for_tests\\folder_for_tests.tar.gz')
    do_tar('tests\\folder_for_tests',
           'tests\\folder_for_tests\\folder_for_tests.tar.gz')
    after = os.path.exists('tests\\folder_for_tests\\folder_for_tests.tar.gz')
    assert (before and after)


def test_untar():
    do_tar('tests\\folder_for_tests',
           'tests\\folder_for_tests\\folder_for_tests.tar.gz')
    before = os.path.exists(
        'tests\\folder_for_tests\\folder_for_tests.tar.gz')
    do_untar('tests\\folder_for_tests\\folder_for_tests.tar.gz',
             'tests\\folder_for_tests')
    after = os.path.exists('tests\\folder_for_tests\\folder_for_tests.tar.gz')
    assert (after and before)


if __name__ == '__main__':
    pytest.main()
