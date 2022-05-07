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

    total_money = 0
    total_food = 0

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0
        self.cat_food = 30

    def __str__(self) -> str:
        self.dirt += 5
        return f'В доме еды - {self.food}, кошачьей еды - {self.cat_food}, денег - {self.money}, грязи - {self.dirt}'


class Human:

    def __init__(self, name: str, house: House):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = house

    def __str__(self) -> str:
        return f'Я {self.name}, сытость - {self.fullness}, счастье - {self.happiness}'

    def eat(self) -> bool:
        if self.house.food == 0:
            self.fullness -= 10
            cprint('В доме нет еды', color='red')
            return False
        elif self.house.food >= 30:
            self.house.food -= 30
            House.total_food += 30
            self.fullness += 30
        else:
            self.fullness += self.house.food
            House.total_food += self.house.food
            self.house.food = 0
        return True

    def pet_a_cat(self) -> None:
        self.happiness += 5
        self.fullness -= 10
        cprint(f'{self.name} гладил кота', color='yellow')


class Husband(Human):

    def __str__(self) -> str:
        return super().__str__()

    def eat(self) -> None:
        if super().eat():
            cprint(f'{self.name} поел', color='green')

    def work(self) -> None:
        self.fullness -= 10
        self.happiness -= 5
        self.house.money += 150
        House.total_money += 150
        cprint(f'{self.name} сходил на работу', color='grey')

    def gaming(self) -> None:
        self.happiness += 20
        self.fullness -= 10
        cprint(f'{self.name} играл в компьютер', color='yellow')

    def buy_cat_food(self) -> None:
        if self.house.money >= 30:
            self.house.money -= 30
            self.house.cat_food += 30
            self.fullness -= 10
            cprint(f'{self.name} купил еды для кота', color='blue')
        else:
            cprint('На кошачью еду не хватило денег', color='red')

    def act(self) -> bool:
        cube = randint(1, 6)
        if self.fullness == 10:
            self.eat()
        elif self.happiness <= 20:
            self.gaming()
        elif self.house.cat_food <= 20:
            self.buy_cat_food()
        elif self.house.money <= 50:
            self.work()
        elif cube == 1:
            self.work()
        elif cube == 3:
            self.buy_cat_food()
        elif cube == 2:
            self.pet_a_cat()
        elif cube == 5:
            self.eat()
        else:
            self.gaming()
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
    total_fur_coat = 0

    def __str__(self) -> str:
        return super().__str__()

    def eat(self) -> None:
        if super().eat():
            cprint(f'{self.name} поела', color='green')

    def shopping(self) -> None:
        if self.house.money >= 200:
            self.house.money -= 200
            self.house.food += 200
        elif self.house.money == 0:
            cprint('Нет денег на еду', color='red')
        else:
            self.house.food = self.house.money
            self.house.money = 0
        self.fullness -= 10
        cprint(f'{self.name} сходила в магазин', color='green')

    def buy_fur_coat(self) -> None:
        if self.house.money >= 350:
            self.house.money -= 350
            self.happiness += 60
            self.fullness -= 10
            self.total_fur_coat += 1
            cprint(f'{self.name} купила себе шубу', color='yellow')
        else:
            cprint('На шубу не хватило денег', color='red')

    def clean_house(self) -> None:
        if self.house.dirt >= 100:
            self.house.dirt -= 100
        else:
            self.house.dirt = 0
        self.fullness -= 10
        self.happiness -= 10
        cprint(f'{self.name} убиралась в доме', color='grey')

    def act(self) -> bool:
        cube = randint(1, 6)
        if self.fullness == 10:
            self.eat()
        elif self.house.food <= 30:
            self.shopping()
        elif self.happiness <= 20:
            self.buy_fur_coat()
        elif self.house.dirt >= 70:
            self.clean_house()
        elif cube == 1:
            self.eat()
        elif cube == 2:
            self.shopping()
        elif cube in (3, 6):
            self.buy_fur_coat()
        elif cube == 5:
            self.clean_house()
        else:
            self.pet_a_cat()
        if self.house.dirt > 90:
            self.happiness -= 10
        if self.fullness < 0:
            cprint(f'{self.name} умерла от голода, вы проиграли', color='red')
            return True
        elif self.happiness < 10:
            cprint(f'{self.name} умерла от депрессии, вы проиграли', color='red')
            return True
        else:
            return False


# if __name__ == '__main__':
#     home = House()
#     danilka = Husband(name='Данилка', house=home)
#     gulnaz = Wife(name='Гульназ', house=home)
#
#     for day in range(1, 366):
#         cprint(f'================== День {day} ==================', color='red')
#         if danilka.act():
#             break
#         if gulnaz.act():
#             break
#         cprint(danilka, color='cyan')
#         cprint(gulnaz, color='cyan')
#         cprint(home, color='cyan')

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

    def __init__(self, name: str, house: House):
        self.name = name
        self.house = house
        self.fullness = 30

    def __str__(self):
        return f'Я {self.name}, сытость - {self.fullness}'

    def eat(self) -> None:
        if self.house.food >= 10:
            self.house.food -= 10
            self.fullness += 20
            cprint(f'{self.name} поел', color='green')
        else:
            self.fullness -= 10
            cprint('В доме нет кошачьей еды')

    def sleep(self) -> None:
        self.fullness -= 10

    def tear_wallpaper(self) -> None:
        self.house.dirt += 5
        self.fullness -= 10
        cprint(f'{self.name} драл обои', color='blue')

    def act(self) -> bool:
        cube = randint(1, 5)
        if self.fullness >= 10:
            self.eat()
        elif cube in (1, 4):
            self.tear_wallpaper()
        elif cube == 3:
            self.eat()
        else:
            self.sleep()
        if self.fullness <= 0:
            cprint(f'{self.name} умер от голода, вы проиграли', color='red')
            return True
        else:
            return False


# if __name__ == '__main__':
#     home = House()
#     danilka = Husband(name='Данилка', house=home)
#     gulnaz = Wife(name='Гульназ', house=home)
#     murzic = Cat(name='Мурзик', house=home)
#
#     for day in range(1, 366):
#         cprint(f'================== День {day} ==================', color='red')
#         if danilka.act():
#             break
#         if gulnaz.act():
#             break
#         if murzic.act():
#             break
#         cprint(danilka, color='cyan')
#         cprint(gulnaz, color='cyan')
#         cprint(murzic, color='cyan')
#         cprint(home, color='cyan')
#     cprint(f'За год съедено еды - {House.total_food}, заработано денег - {House.total_money}, куплено шуб - '
#            f'{Wife.total_fur_coat}', color='magenta')

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

    def __str__(self) -> str:
        return super().__str__()

    def eat(self) -> None:
        if self.house.food == 0:
            self.fullness -= 10
            cprint('В доме нет еды', color='red')
        else:
            self.fullness += 10
            self.house.food -= 10
            cprint(f'{self.name} поела', color='green')

    def sleep(self) -> None:
        self.fullness -= 10
        cprint(f'{self.name} проспала весь день', color='yellow')

    def act(self) -> bool:
        cube = randint(1, 2)
        if self.fullness <= 20:
            self.eat()
        elif cube == 1:
            self.eat()
        else:
            self.sleep()
        if self.fullness < 0:
            cprint(f'{self.name} умерла от голода, вы проиграли', color='red')
            return True
        else:
            return False


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


if __name__ == '__main__':
    home = House()
    danilka = Husband(name='Данилка', house=home)
    gulnaz = Wife(name='Гульназ', house=home)
    francheska = Child(name='Франчкска', house=home)

    for day in range(1, 366):
        cprint(f'================== День {day} ==================', color='red')
        if danilka.act():
            break
        if gulnaz.act():
            break
        if francheska.act():
            break
        cprint(danilka, color='cyan')
        cprint(gulnaz, color='cyan')
        cprint(francheska, color='cyan')
        cprint(home, color='cyan')


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
