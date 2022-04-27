# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:

    def __str__(self) -> str:
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()


class Air:

    def __str__(self) -> str:
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()


class Fire:

    def __str__(self) -> str:
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()


class Earth:

    def __str__(self) -> str:
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()


class Storm:

    def __str__(self) -> str:
        return 'Шторм'


class Steam:

    def __str__(self) -> str:
        return 'Пар'


class Dirt:

    def __str__(self) -> str:
        return 'Грязь'


class Lightning:

    def __str__(self) -> str:
        return 'Молния'


class Dust:

    def __str__(self) -> str:
        return 'Пыль'


class Lava:

    def __str__(self) -> str:
        return 'Лава'


if __name__ == '__main__':
    # TODO можно немного упросить
    #  air = Air()
    #  water = Water()
    #  сути это не поменяет, но будет читаемее, как по мне
    print(Air(), '+', Water(), '=', Air() + Water())
    print(Water(), '+', Air(), '=', Water() + Air())
    print(Air(), '+', Fire(), '=', Air() + Fire())
    print(Fire(), '+', Air(), '=', Fire() + Air())
    print(Air(), '+', Earth(), '=', Air() + Earth())
    print(Earth(), '+', Air(), '=', Earth() + Air())
    print(Water(), '+', Fire(), '=', Water() + Fire())
    print(Fire(), '+', Water(), '=', Fire() + Water())
    print(Water(), '+', Earth(), '=', Water() + Earth())
    print(Earth(), '+', Water(), '=', Earth() + Water())
    print(Earth(), '+', Fire(), '=', Earth() + Fire())
    print(Fire(), '+', Earth(), '=', Fire() + Earth())


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.


class Sanechek:

    def __str__(self) -> str:
        return 'Санечек'

    def __add__(self, other) -> str:
        if isinstance(other, Water):
            return 'Влажный Санечек'
        elif isinstance(other, Air):
            return 'Воздушный Санечек'
        elif isinstance(other, Fire):
            return 'Горящий Санечек'
        elif isinstance(other, Earth):
            return 'Грязный Санечек'


if __name__ == '__main__':
    print(Sanechek(), '+', Water(), '=', Sanechek() + Water())
    print(Sanechek(), '+', Air(), '=', Sanechek() + Air())
    print(Sanechek(), '+', Fire(), '=', Sanechek() + Fire())
    print(Sanechek(), '+', Earth(), '=', Sanechek() + Earth())
    print(Earth(), '+', Sanechek(), '=', Earth() + Sanechek())  # Проверка возвращения None
