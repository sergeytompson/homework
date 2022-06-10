import time
import typing


def get_suffix_by_amount(amount: typing.Union[int, float]) -> str:
    suffix = ''
    if amount % 10 == 1:
        suffix = 'у'
    elif amount % 10 in (2, 3, 4):
        suffix = 'ы'
    return suffix


def func_timer(func):
    def surrogate(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        work_time = end_time - start_time
        print(f'Функция отработала {work_time} секунд{get_suffix_by_amount(work_time)}')
        return result
    return surrogate
