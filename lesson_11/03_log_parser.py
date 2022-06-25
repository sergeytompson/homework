# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

# итератор
class LogParser:

    def __init__(self, file_in: str) -> None:
        self.file_in = file_in
        self.time_dict = {}

    def _read(self) -> None:
        with open(self.file_in, 'r') as text:
            for line in text:
                line = line.strip()
                self._get_stat(line=line)

    def _get_stat(self, line: str) -> None:
        if line[-3:] == 'NOK':
            return
        else:
            time = line[:17] + ']'
            if time in self.time_dict:
                self.time_dict[time] += 1
            else:
                self.time_dict[time] = 1

    def __iter__(self):
        self._read()
        self.i = -1
        self.time_list = [[k, v] for k, v in self.time_dict.items()]
        return self

    def __next__(self) -> list:
        self.i += 1
        try:
            return self.time_list[self.i]
        except IndexError:
            raise StopIteration


if __name__ == '__main__':
    grouped_events = LogParser('events.txt')
    for group_time, event_count in grouped_events:
        print(f'{group_time} {event_count}')


# генератор
def log_parser(file: str) -> tuple:
    time_dict = {}
    with open(file, 'r') as text:
        for line in text:
            line = line.strip()
            if line[-3:] == 'NOK':
                continue
            time = line[:17] + ']'
            if time in time_dict:
                time_dict[time] += 1
            else:
                time_dict[time] = 1
    for k, v in time_dict.items():
        yield k, v


if __name__ == '__main__':
    grouped_events = log_parser('events.txt')
    for group_time, event_count in grouped_events:
        print(f'{group_time} {event_count}')
