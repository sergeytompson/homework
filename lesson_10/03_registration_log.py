# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def check(test_line: str) -> None:
    test_list = test_line.split()
    if len(test_list) != 3:
        raise ValueError('Не присутствуют все 3 поля')
    elif not test_list[0].isalpha():
        raise NotNameError('Поле "Имя" содержит не только буквы')
    elif '@' not in test_list[1] or '.' not in test_list[1]:
        raise NotEmailError('Поле "Емейл" не содержит @ и/или . (точку)')
    try:
        age = int(test_list[2])
    except ValueError:
        raise ValueError('Поле "Возраст" не является числом')
    else:
        if not 10 <= age <= 99:
            raise ValueError('Поле "Возраст" не является числом от 10 до 99')


def write_error(file: str, error_line: str, error_description: str) -> None:
    with open(file, 'a', encoding='utf8') as error_file:
        error_file.write(error_line + ' ' + error_description + '\n')


if __name__ == '__main__':
    bad_file = 'registrations_bad.log'
    with open('registrations.txt', 'r', encoding='utf8') as text:
        for line in text:
            line = line.strip()
            try:
                check(line)
            except ValueError as exp:
                write_error(bad_file, line, str(exp))
            except NotNameError as exp:
                write_error(bad_file, line, str(exp))
            except NotEmailError as exp:
                write_error(bad_file, line, str(exp))
            else:
                with open('registrations_good.log', 'a', encoding='utf8') as good_file:
                    good_file.write(line + '\n')
