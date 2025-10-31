import zipfile
import tarfile
import os
from logging import getLogger
logger = getLogger(__name__)


def do_zip(folder: str, zip_file_name: str) -> None:
    """ create zipped folder with name zip_file_name

    Args:
        folder (str): folder user wants to zip
        zip_file_name (str): new name of zipped folder

    Raises:
        FileNotFoundError: erorr if there is no such file
        TypeError: erorr if user wants to zip file not folder
        ValueError: erorr if there is no '.zip' in zip_file_name
    """
    if not os.path.exists(folder):
        logger.error('Ошибка: не существует папки %s', folder)
        raise FileNotFoundError(f'Папки {folder} не существует')

    if os.path.isfile(folder):
        logger.error('Ошибка: невозможно архивировать %s, а не папку', folder)
        raise TypeError(f"Невозможно архивировать файл {folder}, а не папку")

    if '.zip' not in zip_file_name:
        logger.error(
            'Название архива %s должно содержать расширение .zip', zip_file_name)
        raise ValueError(
            f'Название архива {zip_file_name} должно содержать расширение .zip')

    with zipfile.ZipFile(zip_file_name, 'w') as zf:
        for root, _, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder)
                logger.info('Создан архив %s', zip_file_name)
                zf.write(file_path, arcname)


def do_unzip(zip_folder: str, path_to_unpack: str = '.') -> None:
    """unzip zip_folder to dir with name path_to_unpack

    Args:
        zip_folder (str): folder user wants to unzip
        path_to_unpack (str, optional): dir user wants to unzip in folder. Defaults to '.'.

    Raises:
        FileNotFoundError: erorr if there is no such zip_folder
        ValueError: erorr if there is no '.zip' in zip_folder name
    """

    if not os.path.exists(zip_folder):
        logger.error('Ошибка: не существует папки %s', zip_folder)
        raise FileNotFoundError(
            f'Файла {zip_folder} не существует в данной директории')

    if '.zip' not in zip_folder:
        logger.error(
            'Название архива %s должно содержать расширение .zip', zip_folder)
        raise ValueError(
            f'Название архива {zip_folder} должно содержать расширение .zip')

    with zipfile.ZipFile(zip_folder, 'r') as zf:
        logger.info('Архив %s распакован в папку %s',
                    zip_folder, path_to_unpack)
        zf.extractall(path=path_to_unpack)


def do_tar(folder: str, tar_file_name: str) -> None:
    """ create tarred folder with name tar_file_name

    Args:
        folder (str): folder user wants to tar
        tar_file_name (str): new name of tarred folder

    Raises:
        FileNotFoundError: erorr if there is no such file
        TypeError: erorr if user wants to tar file not folder
        ValueError: erorr if there is no '.tar.gz' in tar_file_name
    """
    if not os.path.exists(folder):
        logger.error('Ошибка: не существует папки %s', folder)
        raise FileNotFoundError(f'Папки {folder} не существует')

    if os.path.isfile(folder):
        logger.error('Ошибка: невозможно архивировать %s, а не папку', folder)
        raise TypeError(f"Невозможно архивировать файл {folder}, а не папку")

    if '.tar.gz' not in tar_file_name:
        logger.error(
            'Название архива %s должно содержать расширение .tar.gz', tar_file_name)
        raise ValueError(
            f'Название архива {tar_file_name} должно содержать расширение .tar.gz')

    with tarfile.open(tar_file_name, 'w:gz') as tar:
        logger.info('Создан архив %s', tar_file_name)
        tar.add(folder, arcname=os.path.basename(folder))


def do_untar(tar_folder: str, path_to_unpack: str = '.') -> None:
    """untar tar_folder to dir with name path_to_unpack

    Args:
        tar_folder (str): folder user wants to untar
        path_to_unpack (str, optional): dir user wants to untar in folder. Defaults to '.'.

    Raises:
        FileNotFoundError: erorr if there is no such tar_folder
        ValueError: erorr if there is no '.tar.gz' in tar_folder name
    """

    if not os.path.exists(tar_folder):
        logger.error('Ошибка: не существует папки %s', tar_folder)
        raise FileNotFoundError(
            f'Файла {tar_folder} не существует в данной директории')

    if '.tar.gz' not in tar_folder:
        logger.error(
            'Название архива %s должно содержать расширение .tar.gz', tar_folder)
        raise ValueError(
            f'Название архива {tar_folder} должно содержать расширение .tar.gz')

    with tarfile.open(tar_folder, 'r:gz') as tar:
        logger.info('Архив %s распакован в папку %s',
                    tar_folder, path_to_unpack)
        tar.extractall(path=path_to_unpack, filter='fully_trusted')


if __name__ == '__main__':
    # do_zip('some', 'some.zip')
    # do_unzip('some.zip')
    # do_tar(r'C:\Users\Huawei\python_programming\python_labs\Lab2\some', 'some.tar.gz')
    # do_unzip('some.zip', 'src')
    pass
