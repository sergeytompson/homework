# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


class Man:

    def __init__(self, name: str):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self) -> str:
        # TODO лучше использовать f строки, они работают быстрее и сообщение получается компактнее
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self) -> bool:
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.food -= 10
            return True
        else:
            cprint('{} нет еды'.format(self.name), color='red')
            return False

    def work(self) -> None:
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_tv(self) -> None:
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self) -> None:
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def buy_cat_food(self) -> None:
        if self.house.money >= 50:
            cprint('{} сходил в магазин за кошачьей едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cat_food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def cleaning(self) -> None:
        cprint('{} убрался дома'.format(self.name), color='blue')
        self.house.dirt -= 100
        self.fullness -= 20

    def go_to_the_house(self, house: 'House') -> None:
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def pic_up_a_cat(self, cat: 'Cat') -> None:
        cat.house = self.house
        cprint('{} подобрал кота {}'.format(self.name, cat.name), color='cyan')

    def act(self) -> None:
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 30:
            if self.eat():
                return
        if self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.cat_food < 20:
            self.buy_cat_food()
        elif self.house.dirt > 100:
            self.cleaning()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_tv()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cat_food = 0
        self.dirt = 0

    def __str__(self) -> str:
        return 'В доме еды осталось {}, денег осталось {}, кошачьей еды осталось {}, грязь - {}'.format(
            self.food, self.money, self.cat_food, self.dirt)


class Cat:

    def __init__(self, name: str):
        self.name = name
        self.fullness = 50
        self.house = None

    def sleep(self) -> None:
        cprint('{} проспал весь день'.format(self.name), color='green')
        self.fullness -= 10

    def eat(self) -> bool:
        if self.house.cat_food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.cat_food -= 10
            return True
        else:
            cprint('У кота {} нет еды'.format(self.name), color='red')
            return False

    def tear_wallpaper(self) -> None:
        cprint('{} драл обои'.format(self.name), color='blue')
        self.fullness -= 10
        self.house.dirt += 5

    def act(self) -> None:
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 2)
        if self.fullness < 20:
            if self.eat():
                return
        elif dice == 1:
            self.tear_wallpaper()
        else:
            self.sleep()

    def __str__(self) -> str:
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)


'''первая часть'''
# if __name__ == '__main__':
#     uchitelskya_6 = House()
#     odin = Cat('Один')
#     serega = Man('Серега')
#     serega.go_to_the_house(uchitelskya_6)
#     serega.pic_up_a_cat(odin)
#
#     for day in range(1, 366):
#         print('================ день {} =================='.format(day))
#         serega.act()
#         odin.act()
#         print('--- в конце дня ---')
#         print(serega)
#         print(odin)
#         print(uchitelskya_6)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)

'''вторая часть'''
if __name__ == '__main__':
    uchitelskya_6 = House()
    odin = Cat('Один')
    serega = Man('Серега')
    lila = Cat('Лила')
    serega.go_to_the_house(uchitelskya_6)
    serega.pic_up_a_cat(odin)
    serega.pic_up_a_cat(lila)

    for day in range(1, 366):
        print('================ день {} =================='.format(day))
        serega.act()
        odin.act()
        lila.act()
        print('--- в конце дня ---')
        print(serega)
        print(odin)
        print(lila)
        print(uchitelskya_6)
