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
import zipfile
from abc import ABCMeta, abstractmethod


# TODO Абстрактные методы принято называть Abstract{имя класса} - AbstractStatistician
class Statistician(metaclass=ABCMeta):

    def __init__(self, file: str, ascending: bool = False) -> None:
        self.file = file
        self.ascending = ascending
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
        # TODO cp1251 - кодировка windows, без явного указания на линуксе падает с ошибкой, в линукс по умолчанию utf-8
        with open(self.file, 'r', encoding='cp1251') as file:
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

    @abstractmethod
    def _sort(self):
        pass

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


class SortByPeriodicity(Statistician):

    def _sort(self):
        # TODO обрати внимание на чудесную функцию sorted
        #  https://tproger.ru/translations/python-sorting/
        #  для сортировки по символам или их частоте потребуется поменять лишь один параметр в классе
        #  для этого используй переменные класса
        """
        Отличия переменных класса от переменных экземпляра:

          class MainClass:
             variable1 = 0  # Это переменная класса

              def __init__():
                   variable2 = 1  #  Это переменная экземпляра.
        """

        """
        sorted(
            [(char, counts) for char, counts in self.stat.items()],
            key=operator.itemgetter(здесь индекс по чему хочешь сортировать из (char, counts)),
            reverse={bool}
        )
        """
        for char, count in self.stat.items():
            self.sort_stat.append([count, char])
            # TODO self.ascending же булева, зачем проверка, если ее можно подставить в reverse?
            if self.ascending:
                self.sort_stat.sort()
            else:
                self.sort_stat.sort(reverse=True)
        for value in self.sort_stat:
            value[0], value[1] = value[1], value[0]


class SortByAlphabet(Statistician):

    def _sort(self):
        for char, count in self.stat.items():
            self.sort_stat.append([char, count])
            self.sort_stat.sort(reverse=self.ascending)


if __name__ == '__main__':
    voyna_i_mir = SortByPeriodicity('voyna-i-mir.txt.zip')
    voyna_i_mir.give_stat()
    voyna_i_mir = SortByPeriodicity('voyna-i-mir.txt.zip', ascending=True)
    voyna_i_mir.give_stat()
    voyna_i_mir = SortByAlphabet('voyna-i-mir.txt.zip')
    voyna_i_mir.give_stat()
    voyna_i_mir = SortByAlphabet('voyna-i-mir.txt.zip', ascending=True)
    voyna_i_mir.give_stat()
# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
