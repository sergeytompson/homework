# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0

    def __str__(self):
        self.dirt += 5
        return f'В доме еды - {self.food}, денег - {self.money}, грязи - {self.dirt}'


class Human:

    def __init__(self, name: str, house: House):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = house

    def __str__(self) -> str:
        return f'Я {self.name}, сытость - {self.fullness}, счастье - {self.happiness}'

    def eat(self) -> None:
        if self.house.food == 0:
            self.fullness -= 10
        elif self.house.food >= 30:
            self.house.food -= 30
            self.fullness += 30
        else:
            self.fullness += self.house.food
            self.house.food = 0


class Husband(Human):

    def __str__(self):
        return super().__str__()

    def work(self):
        self.fullness -= 10
        self.happiness -= 5
        self.house.money += 150

    def gaming(self):
        self.happiness += 20
        self.fullness -= 10

    def act(self) -> bool:
        cube = randint(1, 2)
        if self.fullness == 10:
            self.eat()
            cprint(f'{self.name} поел', color='green')
        elif self.happiness <= 20:
            self.gaming()
            cprint(f'{self.name} играл в компьютер', color='yellow')
        elif self.house.money <= 50:
            self.work()
            cprint(f'{self.name} сходил на работу', color='grey')
        elif cube == 1:
            self.work()
            cprint(f'{self.name} сходил на работу', color='grey')
        else:
            self.gaming()
            cprint(f'{self.name} играл в компьютер', color='yellow')
        if self.house.dirt > 90:
            self.happiness -= 10
        if self.fullness < 0:
            cprint(f'{self.name} умер от голода, вы проиграли', color='red')
            return True
        elif self.happiness < 10:
            cprint(f'{self.name} умер от депрессии, вы проиграли', color='red')
            return True
        else:
            return False


class Wife(Human):

    def __str__(self):
        return super().__str__()

    def shopping(self):
        if self.house.money >= 200:
            self.house.money -= 200
            self.house.food += 200
        else:
            self.house.food = self.house.money
            self.house.money = 0
        self.fullness -= 10

    def buy_fur_coat(self):
        if self.house.money >= 350:
            self.house.money -= 350
            self.happiness += 60
            self.fullness -= 10

    def clean_house(self):
        if self.house.dirt >= 100:
            self.house.dirt -= 100
        else:
            self.house.dirt = 0
        self.fullness -= 10
        self.happiness -= 10

    def act(self) -> bool:
        cube = randint(1, 3)
        if self.fullness == 10:
            self.eat()
            cprint(f'{self.name} поела', color='green')
        elif self.house.food <= 30:
            self.shopping()
            cprint(f'{self.name} сходила в магазин', color='green')
        elif self.happiness <= 20:
            self.buy_fur_coat()
            cprint(f'{self.name} купила себе шубу', color='yellow')
        elif self.house.dirt <= 20:
            self.clean_house()
            cprint(f'{self.name} убиралась в доме', color='grey')
        elif cube == 1:
            self.eat()
            cprint(f'{self.name} поела', color='grey')
        elif cube == 2:
            self.shopping()
            cprint(f'{self.name} сходила в магазин', color='green')
        elif cube == 3:
            self.buy_fur_coat()
            cprint(f'{self.name} купила себе шубу', color='yellow')
        else:
            self.clean_house()
            cprint(f'{self.name} убиралась в доме', color='grey')
        if self.house.dirt > 90:
            self.happiness -= 10
        if self.fullness < 0:
            cprint(f'{self.name} умер от голода, вы проиграли', color='red')
            return True
        elif self.happiness < 10:
            cprint(f'{self.name} умер от депрессии, вы проиграли', color='red')
            return True
        else:
            return False


if __name__ == '__main__':
    home = House()
    danilka = Husband(name='Данилка', house=home)
    gulnaz = Wife(name='Гульназ', house=home)

    for day in range(1, 366):
        cprint(f'================== День {day} ==================', color='red')
        if danilka.act():
            break
        if gulnaz.act():
            break
        cprint(danilka, color='cyan')
        cprint(gulnaz, color='cyan')
        cprint(home, color='cyan')

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self):
        pass

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

