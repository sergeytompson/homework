# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
from abc import ABCMeta, abstractmethod


class LogParser(metaclass=ABCMeta):

    def __init__(self, file_in: str, file_out: str) -> None:
        self.file_in = file_in
        self.file_out = file_out
        self.time_dict = {}

    def read_and_write(self) -> None:
        self._read()
        self._write()

    def _read(self) -> None:
        with open(self.file_in, 'r') as text:
            for line in text:
                line = line.strip()
                self._get_stat(line=line)

    @abstractmethod
    def _get_stat(self, line: str) -> None:
        pass

    def _write(self):
        with open(self.file_out, 'w') as file_out:
            for time, count in self.time_dict.items():
                count = str(count)
                file_out.write(time + ' ' + count + '\n')


class SorterByMinutes(LogParser):

    def _get_stat(self, line: str) -> None:
        time = line[:17] + ']'
        if time in self.time_dict:
            self.time_dict[time] += 1
        else:
            self.time_dict[time] = 1


class SorterByHour(LogParser):

    def _get_stat(self, line: str) -> None:
        time = line[:14] + ']'
        if time in self.time_dict:
            self.time_dict[time] += 1
        else:
            self.time_dict[time] = 1


class SorterByMonth(LogParser):

    def _get_stat(self, line: str) -> None:
        time = line[:8] + ']'
        if time in self.time_dict:
            self.time_dict[time] += 1
        else:
            self.time_dict[time] = 1


class SorterByYears(LogParser):

    def _get_stat(self, line: str) -> None:
        time = line[:5] + ']'
        if time in self.time_dict:
            self.time_dict[time] += 1
        else:
            self.time_dict[time] = 1


if __name__ == '__main__':
    log_parser = SorterByMinutes('events.txt', 'events_by_minutes.txt')
    log_parser.read_and_write()
    log_parser = SorterByHour('events.txt', 'events_by_hour.txt')
    log_parser.read_and_write()
    log_parser = SorterByMonth('events.txt', 'events_by_month.txt')
    log_parser.read_and_write()
    log_parser = SorterByYears('events.txt', 'events_by_years.txt')
    log_parser.read_and_write()


# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
