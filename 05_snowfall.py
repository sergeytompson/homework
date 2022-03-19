# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

'''Короч с "сугробом" (часть 4 - усложненное задание) возникла проблема, что рисование зветом sd.background_color
стирает не только действующую снежинку, но и снежинки, которые уже выпали и опустились. Как эту проблему решить я не 
понял. Чтобы посмотреть решение с "сугробом" раскоменть 26, 32 и 33 строчки и закоменть 27'''

snowflakes_params = [[sd.random_number(0, 1200), 600, sd.random_number(10, 60)] for _ in range(N)]
while True:
    # sd.start_drawing()
    sd.clear_screen()
    for snowflake in snowflakes_params:
        if snowflake[1] <= snowflake[2]:
            index = snowflakes_params.index(snowflake)
            snowflakes_params[index] = [sd.random_number(0, 1200), 600, sd.random_number(10, 60)]
        # current_point = sd.get_point(snowflake[0], snowflake[1])
        # sd.snowflake(current_point, snowflake[2], sd.background_color)
        snowflake[1] -= sd.random_number(1, 15)
        snowflake[0] += sd.random_number(-15, 15)
        current_point = sd.get_point(snowflake[0], snowflake[1])
        sd.snowflake(current_point, snowflake[2])
    # sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
