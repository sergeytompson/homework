# -*- coding: utf-8 -*-

def get_score(game_result: str) -> int:
    score, first_throw = 0, 0
    first_throw_flag = True
    if not isinstance(game_result, str):
        raise TypeError('Неподходящий тип данных, нужна строка')
    for i in game_result:
        if i not in '123456789X/-':
            raise ValueError('Некорректные символы. Значение должно включать: 123456789, X (большая английская икс), '
                             '/ (обратный слеш) и - (тире).')
        if i == 'X':
            score += 20
        elif i.isdigit():
            if first_throw_flag:
                first_throw = int(i)
                first_throw_flag = False
            else:
                result = first_throw + int(i)
                if result > 9:
                    raise ValueError('Сумма очков за 2 броска не может быть больше 9')
                score += result
                first_throw_flag = True
                first_throw = 0
        elif i == '/':
            if first_throw_flag:
                raise ValueError('Символ / не может быть результатом первого броска в фрейме')
            else:
                score += 15
                first_throw_flag = True
                first_throw = 0
        else:
            if first_throw_flag:
                first_throw_flag = False
            else:
                first_throw_flag = True
                score += first_throw
                first_throw = 0
    return score
