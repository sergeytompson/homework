# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

import simple_draw as sd

from morning_in_the_village import GROUND_LEVEL
from morning_in_the_village import house as h
from morning_in_the_village import nature as n
from morning_in_the_village import weather as w

sd.resolution = (1200, 600)

tree_params = n.tree(GROUND_LEVEL)
SNOWFLAKES_AMOUNT = 20
snowflakes_params = [[sd.random_number(50, 1150), 600, sd.random_number(10, 30)]
                     for _ in range(SNOWFLAKES_AMOUNT)]
dropped_out_snowflakes = []
rays_list = []
angle = 0
rainbow_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]
wink_cnt = 0

if __name__ == '__main__':
    while True:
        sd.start_drawing()
        w.snow_delete(snowflakes_params)
        w.delete_rays(rays_list)
        h.wall(GROUND_LEVEL)
        h.roof(GROUND_LEVEL)
        for branch in tree_params:
            branch[0].draw(color=branch[1])
        n.ground(GROUND_LEVEL)
        h.window()
        w.rainbow(rainbow_colors)
        w.sun(angle, rays_list)
        n.smile(wink_cnt)
        w.snow(snowflakes_params, dropped_out_snowflakes, GROUND_LEVEL)
        angle += 5
        wink_cnt += 1
        wink_cnt %= 10
        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

# good
