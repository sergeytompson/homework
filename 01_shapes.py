# -*- coding: utf-8 -*-

import simple_draw as sd


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


def figure(vector, injection, deviation, repeat, long):
    end = vector.start_point
    point = vector.end_point
    for _ in range(repeat):
        vector.draw()
        point = vector.end_point
        injection += deviation
        vector = sd.get_vector(point, injection, long, width=3)
    sd.line(point, end, width=3)


def triangle(point, injection, long):
    vector = sd.get_vector(point, injection, long, width=3)
    figure(vector, injection, 120, 2, long)


def square(point, injection, long):
    vector = sd.get_vector(point, injection, long, width=3)
    figure(vector, injection, 90, 3, long)


def pentagon(point, injection, long):
    vector = sd.get_vector(point, injection, long, width=3)
    figure(vector, injection, 72.1, 4, long)


def hexagon(point, injection, long):
    vector = sd.get_vector(point, injection, long, width=3)
    figure(vector, injection, 60, 5, long)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


if __name__ == '__main__':
    point_1 = sd.get_point(500, 500)
    triangle(point_1, 40, 50)
    point_2 = sd.get_point(500, 100)
    square(point_2, 20, 50)
    point_3 = sd.get_point(100, 100)
    pentagon(point_3, 60, 50)
    point_4 = sd.get_point(100, 500)
    hexagon(point_4, 120, 50)
    sd.pause()
