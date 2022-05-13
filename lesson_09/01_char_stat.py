# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import operator
import zipfile
from abc import ABCMeta
from sys import platform


class AbstractStatistician(metaclass=ABCMeta):
    sort_index = None

    def __init__(self, file: str, revers: bool = False) -> None:
        self.file = file
        self.revers = revers
        self.stat = {}
        self.sort_stat = []

    def give_stat(self) -> None:
        self._read_lines()
        self._sort()
        self._print_sort_stat()

    def _unzip(self) -> None:
        filename = self.file
        zfile = zipfile.ZipFile(self.file, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file = filename

    def _read_lines(self) -> None:
        if self.file.endswith('.zip'):
            self._unzip()
        if platform == 'win32':
            encoding = 'cp1251'
        else:
            encoding = 'utf8'
        with open(self.file, 'r', encoding=encoding) as file:
            for line in file:
                line = line.strip()
                self._collect_stat(line)

    def _collect_stat(self, line: str) -> None:
        for char in line:
            if char.isalpha():
                if char in self.stat:
                    self.stat[char] += 1
                else:
                    self.stat[char] = 1

    def _sort(self):
        self.sort_stat = sorted([(char, counts) for char, counts in self.stat.items()],
                                key=operator.itemgetter(self.sort_index), reverse=self.revers)

    def _print_sort_stat(self) -> None:
        print('+{plus:-^21}+'.format(plus='+'))
        print('|{letter:^10}|'.format(letter='буква'), end='')
        print('{periodicity:^10}|'.format(periodicity='частота'))
        print('+{plus:-^21}+'.format(plus='+'))
        total_count = 0
        for char, count in self.sort_stat:
            total_count += count
            print(f'|{char:^10}|', end='')
            print(f'{count:^10}|')
        print('+{plus:-^21}+'.format(plus='+'))
        print('|{total:^10}|'.format(total='итог'), end='')
        print(f'{total_count:^10}|')
        print('+{plus:-^21}+'.format(plus='+'))


class SortByPeriodicity(AbstractStatistician):

    sort_index = 1


class SortByAlphabet(AbstractStatistician):

    sort_index = 0


if __name__ == '__main__':
    voyna_i_mir = SortByPeriodicity('voyna-i-mir.txt.zip')
    voyna_i_mir.give_stat()
    voyna_i_mir = SortByPeriodicity('voyna-i-mir.txt.zip', revers=True)
    voyna_i_mir.give_stat()
    voyna_i_mir = SortByAlphabet('voyna-i-mir.txt.zip')
    voyna_i_mir.give_stat()
    voyna_i_mir = SortByAlphabet('voyna-i-mir.txt.zip', revers=True)
    voyna_i_mir.give_stat()
# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
