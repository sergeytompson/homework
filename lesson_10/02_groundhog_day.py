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


class IamGodError(Exception):

    total: int = 0

    def __str__(self) -> str:
        return 'считал себя богом'


class DrunkError(Exception):

    total: int = 0

    def __str__(self) -> str:
        return 'напивался'


class CarCrashError(Exception):

    total: int = 0

    def __str__(self) -> str:
        return 'попадал в аварии'


class GluttonyError(Exception):

    total: int = 0

    def __str__(self) -> str:
        return 'обжирался'


class DepressionError(Exception):

    total: int = 0

    def __str__(self) -> str:
        return 'впадал в депрессию'


class SuicideError(Exception):

    total: int = 0

    def __str__(self) -> str:
        return 'кончал жизнь самоубийством'


def one_day(possible_errors: list) -> int:
    error_cube = randint(1, 13)
    if error_cube == 7:
        raise choice(possible_errors)
    else:
        return randint(1, 7)


if __name__ == '__main__':
    murray_carma = 0
    day = 1
    errors = [IamGodError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError(), SuicideError()]
    while murray_carma < ENLIGHTENMENT_CARMA_LEVEL:
        cprint(f'================== День {day} ==================', color='yellow')
        try:
            murray_carma += one_day(errors)
        except IamGodError:
            cprint('Билл Мюррей почувстовал себя богом', color='red')
            IamGodError.total += 1
        except DrunkError:
            cprint('Билл Мюррей напился как свинья', color='red')
            DrunkError.total += 1
        except CarCrashError:
            cprint('Билл Мюррей устроил автомобильную аварию', color='red')
            CarCrashError.total += 1
        except GluttonyError:
            cprint('Билл Мюррей весь день обжирался вкуснятиной', color='red')
            GluttonyError.total += 1
        except DepressionError:
            cprint('Билл Мюррей впал в депрессию', color='red')
            DepressionError.total += 1
        except SuicideError:
            cprint('Билл Мюррей покончил жизнь самоубийством, но это не помогло', color='red')
            SuicideError.total += 1
        else:
            cprint(f'Билл Мюррей стал чуточку лучше, его карма достигла {murray_carma}', color='green')
        finally:
            day += 1
    cprint(f'Билл Мюррей достиг просветления и сумел выбраться из дня сурка, проведя там {day} дней. За это время он:',
           color='blue')
    for error in errors:
        cprint(f'    {error} {error.total} {"раза" if 1 < error.total < 5 else "раз"}', color='blue')

# https://goo.gl/JnsDqu
