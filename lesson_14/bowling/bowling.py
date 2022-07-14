# -*- coding: utf-8 -*-
import bowling_errors


def get_score(game_result: str) -> int:
    score = first_throw = 0
    first_throw_flag = True
    symbol_meanings = {str(i): i for i in range(1, 10)}
    symbol_meanings['X'], symbol_meanings['/'], symbol_meanings['-'] = 20, 15, 0
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


def correct_type(variable):
    if not isinstance(variable, str):
        raise TypeError('Неподходящий тип данных, нужна строка')


def correct_symbol(symbol, flag, meanings_lst, ft):
    if symbol not in meanings_lst:
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
