# -*- coding: utf-8 -*-

import simple_draw as sd

shapes = __import__('01_shapes')

point_1 = sd.get_point(200, 300)  # Не понял, что делают эти 2 строчки. По контексту ясно, что они должны отрисовать
shapes.triangle(point_1, 10, 70)  # еще один треугольник, но у меня он не рисуется.
sd.pause()
