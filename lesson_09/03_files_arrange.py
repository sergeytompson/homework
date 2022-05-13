# -*- coding: utf-8 -*-

import os
import shutil
import time
import zipfile
import pathlib
from abc import ABCMeta, abstractmethod

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class FileSort(metaclass=ABCMeta):

    def __init__(self, folder_in: str, folder_out: str):
        self.folder_in = folder_in
        self.folder_out = folder_out

    def _unzip(self) -> None:
        with zipfile.ZipFile(self.folder_in, 'r') as zf:
            for zi in zf.infolist():
                zf.extract(zi)
                date_time = time.mktime(zi.date_time + (0, 0, -1))
                os.utime(zi.filename, (date_time, date_time))
        self.folder_in = self.folder_in[:-4]

    @abstractmethod
    def sort_by_month(self) -> None:
        pass


class SortFromFolder(FileSort):

    def sort_by_month(self) -> None:
        if self.folder_in.endswith('.zip'):
            self._unzip()
        for dir_path, dir_names, filenames in os.walk(self.folder_in):
            for file in filenames:
                file_name = os.path.join(dir_path, file)
                sec = os.path.getmtime(file_name)
                year, month, *_ = map(str, time.gmtime(sec))
                month = '0' + month if len(month) == 1 else month
                file_direct = os.path.join(self.folder_out, year, month)
                pathlib.Path(file_direct).mkdir(parents=True, exist_ok=True)
                shutil.copy2(file_name, file_direct)


class SortFromZip(FileSort):

    def sort_by_month(self) -> None:
        with zipfile.ZipFile(self.folder_in, 'r') as zf:
            for zi in zf.infolist():
                if not zi.filename.endswith('/'):
                    year = str(zi.date_time[0])
                    month = str(zi.date_time[1])
                    month = '0' + month if len(month) == 1 else month
                    file_direct = os.path.join(self.folder_out, year, month)
                    pathlib.Path(file_direct).mkdir(parents=True, exist_ok=True)
                    filename_list = zi.filename.split('/')
                    zi.filename = filename_list[-1]
                    zf.extract(zi, file_direct)


'''проверка первой части'''
# if __name__ == '__main__':
#     sort_foto = SortFromFolder('icons.zip', 'icons_by_year')
#     sort_foto.sort_by_month()

'''проверка второй части'''
if __name__ == '__main__':
    sort_foto = SortFromZip('icons.zip', 'icons_by_year')
    sort_foto.sort_by_month()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
