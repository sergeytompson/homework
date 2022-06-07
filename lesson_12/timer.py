import time


def func_timer(func):
    def surrogate(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        work_time = end_time - start_time
        print(f'������� �������� {work_time}'
              f'{"�������" if work_time % 10 == 1 else "�������" if work_time % 10 in (2, 3, 4) else "������"}')
        return result
    return surrogate
