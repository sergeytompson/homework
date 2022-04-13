from random import randint, sample
_num = ''


def generate_number(digits_count: int = 4) -> str:
    result = "".join(map(str, sample(range(0, 10), digits_count-1)))
    first_char = str(randint(1, 9))
    while first_char in result:
        first_char = str(randint(1, 9))
    return first_char + result

# TODO генерировать 4х значное число и надеяться, что в все цифры будут уникальными такая себе идея
#  куда быстрее будет генерировать числа по одному и проверять на уникальность
#  если речь идет о рандомной генерации, то можно поискать более подходящий инструмент в модуле random
#  как вариант sample, например так:
#  sample(range(0, 10), 3) - вернет список из трех уникальных элементов в промежутке от 0 до 9
#  а первый элемент можно сгененрировать уже глядя на них
#  вообще не стесняйся гуглить, желательно на англ


def think_of_a_number() -> str:
    global _num
    _num = ''
    while True:
        _num = str(randint(1000, 9999))
        for i in range(len(_num) - 1):
            if _num.count(_num[i], i) > 1:
                continue
        else:
            break
    return _num


# TODO можно итерироваться по нескольким коллекциям одновременно с помощью zip
#  for user_char, control_char in zip(user_num, hidden_num):
#  цикл закончится, когда кончится любая коллекция, если они имеют разную длинну
#  какие типы называют коллекциями: https://ru.hexlet.io/courses/python_101/lessons/python-collections/theory_unit
#  + к коллекциям относятся еще и строки
def bulls_cows(user_num: str, hidden_num: str) -> (int, int):
    bulls, cows = 0, 0
    for i in range(len(user_num)):
        if user_num[i] == hidden_num[i]:
            bulls += 1
        elif user_num[i] in hidden_num:
            cows += 1
    # TODO  лучше сделать функцию более абстрактной, она просто получает 2 строки и сравнивает их опр. образом
    #  убрав проверку ты будешь гарантировать, что функция всегда возвращает один тип данных tuple(int, int)
    #  + не нужно будет проверять isinstanse в основном скрипте
    #  проверку на количество быков лучше вывести в основной блок
    if bulls == 4:
        return 'Поздравляем, вы победили'
    return bulls, cows


def check_answer(user_num: str) -> bool:
    for i in range(len(user_num) - 1):
        if user_num.count(user_num[i], i) > 1:
            return False
    if user_num.isdigit() and len(user_num) == 4 and user_num[0] != '0':
        return True
    else:
        return False
