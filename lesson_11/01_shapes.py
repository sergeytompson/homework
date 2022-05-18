# -*- coding: utf-8 -*-

import simple_draw as sd
from typing import Callable

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n: int) -> Callable:
    deviations = {3: 120, 4: 90, 5: 72.5, 6: 60}
    deviation = deviations[n]

    def polygon(point: sd.Point, angle: int, length: int) -> None:
        vector = sd.get_vector(point, angle, length)
        end = vector.start_point
        point = vector.end_point
        for _ in range(n - 1):
            vector.draw()
            point = vector.end_point
            angle += deviation
            vector = sd.get_vector(point, angle, length)
        sd.line(point, end)

    return polygon


if __name__ == '__main__':
    draw_triangle = get_polygon(n=3)
    draw_triangle(point=sd.get_point(100, 100), angle=13, length=100)


sd.pause()
