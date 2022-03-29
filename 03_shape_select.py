# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


def figure(vector, injection, deviation, repeat, long, figure_color):
    end = vector.start_point
    point = vector.end_point
    for _ in range(repeat):
        vector.draw(color=figure_color)
        point = vector.end_point
        injection += deviation
        vector = sd.get_vector(point, injection, long, width=3)
    sd.line(point, end, width=3, color=figure_color)


def triangle(point, injection, long, color):
    vector = sd.get_vector(point, injection, long, width=3)
    figure(vector, injection, 120, 2, long, figure_color=color)


def square(point, injection, long, color):
    vector = sd.get_vector(point, injection, long, width=3)
    figure(vector, injection, 90, 3, long, figure_color=color)


def pentagon(point, injection, long, color):
    vector = sd.get_vector(point, injection, long, width=3)
    figure(vector, injection, long, 72.1, 4, figure_color=color)


def hexagon(point, injection, long, color):
    vector = sd.get_vector(point, injection, long, width=3)
    figure(vector, injection, 60, 5, long, figure_color=color)


colors = [('red', sd.COLOR_RED), ('orange', sd.COLOR_ORANGE), ('yellow', sd.COLOR_YELLOW),
          ('green', sd.COLOR_GREEN), ('cyan', sd.COLOR_CYAN), ('blue', sd.COLOR_BLUE),
          ('purple', sd.COLOR_PURPLE)]

figures = [('triangle', triangle), ('square', square), ('pentagon', pentagon), ('hexagon', hexagon)]

print('Возможные фигуры:')
for num, figure in enumerate(figures):
    print(f'{num}: {figure[0]}')

print('Возможные цвета:')
for num, color_from_colors in enumerate(colors):
    print(f'{num}: {color_from_colors[0]}')


def check_input_figure():
    while True:
        figure_num = input('Введите число от 0 до 3, соответствующее нужной фигуре: ')
        if not figure_num.isdigit():
            print('Ошибка')
            continue
        figure_num = int(figure_num)
        if not 0 <= figure_num <= 3:
            print('Ошибка')
            continue
        else:
            break
    return figure_num


def check_input_color():
    while True:
        color_num = input('Введите число от 0 до 6, соответствующее нужному цвету: ')
        if not color_num.isdigit():
            print('Ошибка')
            continue
        color_num = int(color_num)
        if not 0 <= color_num <= 6:
            print('Ошибка')
            continue
        else:
            break
    return color_num


if __name__ == '__main__':
    figure_number = check_input_figure()
    chosen_figure = figures[figure_number][1]
    color_number = check_input_color()
    chosen_color = colors[color_number][1]
    figure_point = sd.get_point(300, 300)
    chosen_figure(point=figure_point, injection=30, long=100, color=chosen_color)
    sd.pause()
