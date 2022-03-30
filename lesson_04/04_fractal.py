# -*- coding: utf-8 -*-

import simple_draw as sd
sd.set_screen_size(1200, 600)

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

DEVIATION = 30

'''решение первой части'''
# def draw_branches(start_point, angle, length):
#     if length < 10:
#         return
#     first_angle = angle + DEVIATION
#     second_angle = angle - DEVIATION
#     first_branch = sd.get_vector(start_point, first_angle, length)
#     first_branch.draw()
#     second_branch = sd.get_vector(start_point, second_angle, length)
#     second_branch.draw()
#     first_end = first_branch.end_point
#     second_end = second_branch.end_point
#     length *= 0.75
#     draw_branches(first_end, first_angle, length)
#     draw_branches(second_end, second_angle, length)


'''решение усложненной части'''


def draw_branches(start_point, angle, length):
    if length < 10:
        return
    angle_deviation = sd.random_number(0, 40) / 100
    length_deviation = sd.random_number(0, 20) / 100
    first_angle = angle + DEVIATION + (DEVIATION * angle_deviation)
    second_angle = angle - DEVIATION + (DEVIATION * angle_deviation)
    first_branch = sd.get_vector(start_point, first_angle, length)
    first_branch.draw()
    second_branch = sd.get_vector(start_point, second_angle, length)
    second_branch.draw()
    first_end = first_branch.end_point
    second_end = second_branch.end_point
    length *= 0.75 + (0.75 * length_deviation)
    draw_branches(first_end, first_angle, length)
    draw_branches(second_end, second_angle, length)


if __name__ == '__main__':
    root_point = sd.get_point(600, 30)
    trunk = sd.get_vector(root_point, 270, 30)
    trunk.draw()
    draw_branches(start_point=root_point, angle=90, length=100)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()
