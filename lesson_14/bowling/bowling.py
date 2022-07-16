# -*- coding: utf-8 -*-
from lesson_14.bowling.handlers import handle_type, handle_symbol
from lesson_14.bowling.settings import symbol_meanings


def get_score(game_result: str) -> int:
    score = first_throw = 0
    first_throw_flag = True

    handle_type(game_result)

    for i in game_result:
        handle_symbol(i, first_throw_flag, symbol_meanings, first_throw)
        if first_throw_flag and i != 'X':
            first_throw += symbol_meanings[i]
            first_throw_flag = False
        else:
            score += symbol_meanings[i] + first_throw if i != '/' else symbol_meanings[i]
            first_throw_flag = True
            first_throw = 0
    return score
