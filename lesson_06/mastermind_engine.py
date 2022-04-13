from random import randint
_num = ''


def think_of_a_number():
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


def bulls_cows(user_num, hidden_num):
    bulls, cows = 0, 0
    for i in range(len(user_num)):
        if user_num[i] == hidden_num[i]:
            bulls += 1
        elif user_num[i] in hidden_num:
            cows += 1
    if bulls == 4:
        return 'Поздравляем, вы победили'
    return bulls, cows


def check_answer(user_num):
    for i in range(len(user_num) - 1):
        if user_num.count(user_num[i], i) > 1:
            return False
    if user_num.isdigit() and len(user_num) == 4 and user_num[0] != '0':
        return True
    else:
        return False
