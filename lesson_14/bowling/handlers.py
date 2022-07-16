# -*- coding: utf-8 -*-
from lesson_14.bowling import exceptions


def handle_type(variable):
    if not isinstance(variable, str):
        raise TypeError('Неподходящий тип данных, нужна строка')


def handle_symbol(symbol, flag, meanings_lst, ft):
    if symbol not in meanings_lst:
        raise exceptions.IncorrectSymbolException
    if flag:
        if symbol == '/':
            raise exceptions.BackSlashInFirstThrowException
    else:
        if symbol == 'X':
            raise exceptions.XInSecondThrowException
        elif symbol != '/' and meanings_lst[symbol] + ft > 9:
            raise exceptions.ExcessSkittlesException
