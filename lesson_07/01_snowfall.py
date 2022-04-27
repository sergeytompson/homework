# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self) -> None:
        self.point = [sd.random_number(0, sd.resolution[0]), sd.resolution[1] + 15]
        self.size = sd.random_number(10, 30)

    def clear_previous_picture(self) -> None:
        point = sd.get_point(*self.point)
        sd.snowflake(point, self.size, color=sd.background_color)

    def move(self) -> None:
        self.point[0] += sd.random_number(-15, 15)
        self.point[1] -= sd.random_number(1, 15)

    def draw(self) -> None:
        point = sd.get_point(*self.point)
        sd.snowflake(point, self.size)

    def can_fall(self) -> bool:
        return self.point[1] > 0 - self.size


'''первая часть'''
# if __name__ == '__main__':
#     flake = Snowflake()
#
#     while True:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#         if not flake.can_fall():
#             break
#         sd.sleep(0.1)
#         if sd.user_want_exit():
#             break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

'''вторая часть'''


def get_flakes(count: int) -> list:
    flakes_list = []
    for _ in range(count):
        snowflake = Snowflake()
        flakes_list.append(snowflake)
    return flakes_list


def get_fallen_flakes(flakes_list: list) -> int:
    cnt = 0
    for snowflake in flakes_list:
        if snowflake.point[1] < 0 - snowflake.size:
            flakes_list.remove(snowflake)
            cnt += 1
    return cnt


def append_flakes(count: int, flakes_list: list) -> None:
    for _ in range(count):
        snowflake = Snowflake()
        flakes_list.append(snowflake)


if __name__ == '__main__':
    N = 20
    flakes = get_flakes(count=N)
    while True:
        for flake in flakes:
            flake.clear_previous_picture()
            flake.move()
            flake.draw()
        fallen_flakes = get_fallen_flakes(flakes)
        if fallen_flakes:
            append_flakes(count=fallen_flakes, flakes_list=flakes)
        sd.sleep(0.1)
        if sd.user_want_exit():
            break

sd.pause()
