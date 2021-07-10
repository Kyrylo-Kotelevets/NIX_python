"""
создайте тестовую директорию с несколькими файлами разных названий
при помощи модуля os создайте функцию для очистки директории от файлов определённого расширения, принимающую на вход:
путь к директории, где нужно удалить файлы
строку - формат файла, по которой будет определяться, нужно ли удалять файл
пример вызова:
delete_files_func(path='/path/to/folder', file_extension='.txt')
после удаления файлов функция должна вернуть список названий всех удалённых файлов

результат - в директории /path/to/folder удалены все файлы, расширение которых == .txt
"""

import os


def delete_files_func(path, file_extension):
    """Function cleans given directory from files with input extension

    :param path: path to directory with files to delete
    :param file_extension: extension of files to delete
    :return: deleted files
    """
    deleted_files = []
    for file in os.listdir(path):
        if file.endswith(file_extension):
            os.remove(path + os.sep + file)
            deleted_files.append(file)
    return deleted_files


print(delete_files_func(path='tmp', file_extension='.txt'))
