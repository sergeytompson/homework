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


def triangle(point, injection, long, triangle_color):
    vector = sd.get_vector(point, injection, long, width=3)
    figure(vector, injection, 120, 2, long, figure_color=triangle_color)


def square(point, injection, long, square_color):
    vector = sd.get_vector(point, injection, long, width=3)
    figure(vector, injection, 90, 3, long, figure_color=square_color)


def pentagon(point, injection, long, pentagon_color):
    vector = sd.get_vector(point, injection, long, width=3)
    figure(vector, injection, 72.1, 4, long, figure_color=pentagon_color)


def hexagon(point, injection, long, hexagon_color):
    vector = sd.get_vector(point, injection, long, width=3)
    figure(vector, injection, 60, 5, long, figure_color=hexagon_color)


colors = [('red', sd.COLOR_RED), ('orange', sd.COLOR_ORANGE), ('yellow', sd.COLOR_YELLOW),
          ('green', sd.COLOR_GREEN), ('cyan', sd.COLOR_CYAN), ('blue', sd.COLOR_BLUE),
          ('purple', sd.COLOR_PURPLE)]



print('Возможные цвета:')
for num, color in enumerate(colors):
    print(f'{num}: {color[0]}')


def check_input():
    while True:
        # TODO где то здесь должен быть выбор фигур
        """
        в списке ты можешь так же хранить функции, например
        figures = [
            ('triangle', triangle), ('hexagon', hexagon)
]
        ты можешь получить аналогично цвету нужную тебе функцию и записать ее в переменную и вызвать:
        
        def get_func_from_input():
            ...
            return func
        
        shape_func = get_func_from_input()
        shape_func()
        
        """
        num = input('Введите число от 0 до 6, соответствующее нужному цвету: ')
        if not num.isdigit():
            print('Ошибка')
            continue
        num = int(num)
        if not 0 <= num <= 6:
            print('Ошибка')
            continue
        else:
            break
    return num


if __name__ == '__main__':
    num = check_input()
    color = colors[num][1]
    point_4 = sd.get_point(100, 500)
    hexagon(point_4, 120, 50, hexagon_color=color)
    point_3 = sd.get_point(100, 100)
    pentagon(point_3, 60, 50, pentagon_color=color)
    point_2 = sd.get_point(500, 100)
    square(point_2, 20, 50, square_color=color)
    point_1 = sd.get_point(500, 500)
    triangle(point_1, 40, 50, triangle_color=color)
    sd.pause()
