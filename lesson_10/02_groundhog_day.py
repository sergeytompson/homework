# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

from random import randint, choice
from termcolor import cprint

ENLIGHTENMENT_CARMA_LEVEL = 777


class MurrayError(Exception):
    pass


class IamGodError(MurrayError):

    def __str__(self) -> str:
        return 'считал себя богом'


class DrunkError(MurrayError):

    def __str__(self) -> str:
        return 'напился'


class CarCrashError(MurrayError):

    def __str__(self) -> str:
        return 'попал в аварию'


class GluttonyError(MurrayError):

    def __str__(self) -> str:
        return 'обжирался'


class DepressionError(MurrayError):

    def __str__(self) -> str:
        return 'впал в депрессию'


class SuicideError(MurrayError):

    def __str__(self) -> str:
        return 'покончил жизнь самоубийством'


def one_day(possible_errors: list) -> int:
    error_cube = randint(1, 13)
    if error_cube == 7:
        raise choice(possible_errors)
    else:
        return randint(1, 7)


if __name__ == '__main__':
    murray_carma = 0
    hero = 'Билл Мюррей'
    day = 1
    i_am_good_total, drunk_total, car_crash_total, gluttony_total, depression_total, suicide_total = 0, 0, 0, 0, 0, 0
    errors = [IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError]
    while murray_carma < ENLIGHTENMENT_CARMA_LEVEL:
        cprint(f'================== День {day} ==================', color='yellow')
        try:
            murray_carma += one_day(errors)
        except MurrayError as exc:
            incident = str(exc)
            what_happened_to_billy = hero + ' ' + incident
            cprint(what_happened_to_billy, color='red')
            if incident == 'считал себя богом':
                i_am_good_total += 1
            elif incident == 'напился':
                drunk_total += 1
            elif incident == 'попал в аварию':
                car_crash_total += 1
            elif incident == 'обжирался':
                gluttony_total += 1
            elif incident == 'впал в депрессию':
                depression_total += 1
            elif incident == 'покончил жизнь самоубийством':
                suicide_total += 1
        else:
            cprint(f'{hero} стал чуточку лучше, его карма достигла {murray_carma}', color='green')
        finally:
            day += 1
    cprint(f'{hero} достиг просветления и сумел выбраться из дня сурка, проведя там {day} дней. За это время он:',
           color='blue')
    errors_total = [i_am_good_total, drunk_total, car_crash_total, gluttony_total, depression_total, suicide_total]
    for error, total in zip(errors, errors_total):
        cprint(f'    {error()} {total} {"раза" if 1 < total < 5 else "раз"}', color='blue')

# https://goo.gl/JnsDqu
