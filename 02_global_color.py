# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


def figure(vector, injection, deviation, repeat, long, color):
    end = vector.start_point
    for _ in range(repeat):
        vector.draw(color=color)
        point = vector.end_point
        injection += deviation
        vector = sd.get_vector(point, injection, long, width=3)
    sd.line(point, end, width=3, color=color)


def triangle(point, injection, long, color):
    vector = sd.get_vector(point, injection, long, width=3)
    figure(vector, injection, 120, 2, long, color=color)


def square(point, injection, long, color):
    vector = sd.get_vector(point, injection, long, width=3)
    figure(vector, injection, 90, 3, long, color=color)


def pentagon(point, injection, long, color):
    vector = sd.get_vector(point, injection, long, width=3)
    figure(vector, injection, 72.1, 4, long, color=color)


def hexagon(point, injection, long, color):
    vector = sd.get_vector(point, injection, long, width=3)
    figure(vector, injection, 60, 5, long, color=color)


colors = [('red', sd.COLOR_RED), ('orange', sd.COLOR_ORANGE), ('yellow', sd.COLOR_YELLOW),
          ('green', sd.COLOR_GREEN), ('cyan', sd.COLOR_CYAN), ('blue', sd.COLOR_BLUE),
          ('purple', sd.COLOR_PURPLE)]

print('Возможные цвета:')
for num, color in enumerate(colors):
    print(f'{num}: {color[0]}')


def check_input():
    while True:
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


num = check_input()
color = colors[num][1]
point_4 = sd.get_point(100, 500)
hexagon(point_4, 120, 50, color=color)
point_3 = sd.get_point(100, 100)
pentagon(point_3, 60, 50, color=color)
point_2 = sd.get_point(500, 100)
square(point_2, 20, 50, color=color)
point_1 = sd.get_point(500, 500)
triangle(point_1, 40, 50, color=color)

sd.pause()
