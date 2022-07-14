# -*- coding: utf-8 -*-
# TODO используй полный путь при импортах, как в примере ниже
from homework.lesson_14.bowling import bowling_errors


def get_score(game_result: str) -> int:
    score = first_throw = 0
    first_throw_flag = True
    # TODO  цены бросков в теории могут легко поменяться и в более менее большом файле на 1000+ строк
    #  найти такую инфу будет очень проблематично
    #  предлагаю перенести это в отдельный файл модуля settings
    #  в файле настроек лучше прописывать словарь явно безе генераторов
    ####
    symbol_meanings = {str(i): i for i in range(1, 10)}
    symbol_meanings['X'], symbol_meanings['/'], symbol_meanings['-'] = 20, 15, 0
    ####

    correct_type(game_result)

    for i in game_result:
        correct_symbol(i, first_throw_flag, symbol_meanings, first_throw)
        if first_throw_flag and i != 'X':
            first_throw += symbol_meanings[i]
            first_throw_flag = False
        else:
            score += symbol_meanings[i] + first_throw if i != '/' else symbol_meanings[i]
            first_throw_flag = True
            first_throw = 0
    return score


# TODO 2 функции ниже - это обработчики - хэндлеры
#  создай для них отдельный файл в модуле handlers
#  есть это хэндлер, то и название должно быть говорящим handle_type, handle_symbol итд

def correct_type(variable):
    if not isinstance(variable, str):
        raise TypeError('Неподходящий тип данных, нужна строка')


def correct_symbol(symbol, flag, meanings_lst, ft):
    if symbol not in meanings_lst:
        # TODO сообщения должны быть в самих классах ошибок
        raise bowling_errors.IncorrectSymbolError('Некорректный символ. Значение должно включать: 123456789,'
                                                  'X (большая английская икс), / (обратный слеш) и - (тире).')
    if flag:
        if symbol == '/':
            raise bowling_errors.BackSlashInFirstThrowError('Символ / не может быть результатом первого броска'
                                                            'в фрейме')
    else:
        if symbol == 'X':
            raise bowling_errors.XInSecondThrowError('Символ X не может быть результатом второго броска в фрейме')
        elif symbol != '/' and meanings_lst[symbol] + ft > 9:
            raise bowling_errors.ExcessSkittlesError('Сумма очков за 2 броска не может быть больше 9')


####
"""
По итогу предлагаю сделать модуль след вида:
bowling
  -  __init__
  -  bowling
  -  exceptions
  -  handlers
  -  settings
"""
####
