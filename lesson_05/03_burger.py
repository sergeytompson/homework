# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

import my_burger


def double_cheeseburger():
    print('Рецепт двойного чизбургера:')
    my_burger.bun()
    my_burger.cutler()
    my_burger.cheese()
    my_burger.cutler()
    my_burger.cheese()
    my_burger.ketchup()
    my_burger.mustard()
    my_burger.onion()
    my_burger.cucumber()
    my_burger.cucumber()
    my_burger.bun()
    print()


def serega_burger():
    print('Рецепт бургера от Сереги:')
    my_burger.bun()
    my_burger.ketchup()
    my_burger.mustard()
    my_burger.tomato()
    my_burger.bacon()
    my_burger.scramble()
    my_burger.cheese()
    my_burger.bun()
    print()


if __name__ == '__main__':
    double_cheeseburger()
    serega_burger()

# good!
