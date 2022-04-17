from random import randint, sample, choice

_num = ''


def generate_number(digits_count: int = 4) -> str:
    result = "".join(map(str, sample(range(0, 10), digits_count - 1)))
    first_char = str(randint(1, 9))
    while first_char in result:
        first_char = str(randint(1, 9))
    return first_char + result


# Попробовал реализовать более простой вариант по-своему
def think_of_a_number() -> str:
    global _num
    _num = ''
    numbers = [str(i) for i in range(10)]
    first_num = choice(numbers[1:])
    numbers.remove(first_num)
    _num += first_num
    for _ in range(3):
        second_num = first_num = choice(numbers)
        numbers.remove(second_num)
        _num += first_num
    return _num


def bulls_cows(user_num: str, hidden_num: str) -> (int, int):
    bulls, cows = 0, 0
    for user_char, control_char in zip(user_num, hidden_num):
        if user_char == control_char:
            bulls += 1
        elif user_char in hidden_num:
            cows += 1
    return bulls, cows


def check_answer(user_num: str) -> bool:
    for i in range(len(user_num) - 1):
        if user_num.count(user_num[i], i) > 1:
            return False
    if user_num.isdigit() and len(user_num) == 4 and user_num[0] != '0':
        return True
    else:
        return False
