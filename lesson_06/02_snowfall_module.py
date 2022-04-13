# -*- coding: utf-8 -*-

import simple_draw as sd
import snowfall as sf
sd.resolution = (1200, 600)

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

if __name__ == '__main__':
    sf.snowflakes_creation(20)  # создать_снежинки(N)
    while True:
        sd.start_drawing()
        sf.draw_snowflakes(color=sd.background_color)  # нарисовать_снежинки_цветом(color=sd.background_color)
        sf.move_snowflakes()  # сдвинуть_снежинки()
        sf.draw_snowflakes()  # нарисовать_снежинки_цветом(color)
        dropped_set = sf.went_abroad()
        if dropped_set:  # если есть номера_достигших_низа_экрана() то
            sf.delete_snowflakes(dropped_set)  # удалить_снежинки(номера)
            sf.snowflakes_creation(len(dropped_set))  # создать_снежинки(count)
        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break

sd.pause()
