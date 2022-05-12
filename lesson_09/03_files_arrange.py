# -*- coding: utf-8 -*-

import os
import shutil
import time
import zipfile
import pathlib

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


class FileSort:

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
                criation_time = time.gmtime(sec)
                year = str(criation_time[0])
                month = str(criation_time[1])
                if len(month) == 1:
                    month = '0' + month
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
                    if len(month) == 1:
                        month = '0' + month
                    file_direct = os.path.join(self.folder_out, year, month)
                    pathlib.Path(file_direct).mkdir(parents=True, exist_ok=True)
                    zf.extract(zi, file_direct)
        for dir_path, dir_names, filenames in os.walk(self.folder_out):
            for file in filenames:
                file_dir = os.path.join(dir_path, file)
                dir_lst = dir_path.split('\\')
                while not len(dir_lst[-1]) == 2 and not dir_lst[-1].isdigit():
                    dir_lst.pop()
                month_dir = os.path.join(*dir_lst)
                shutil.move(file_dir, month_dir)
        for dir_path, dir_names, filenames in os.walk(self.folder_out):
            if not dir_names and not filenames:
                os.removedirs(dir_path)


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
