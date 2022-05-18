# -*- coding: utf-8 -*-

from typing import Generator


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n+1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:

    def __init__(self, n: int):
        self.i = 1
        self.n = n
        self.prime_numbers = []

    def __iter__(self):
        self.i = 1
        self.prime_numbers = []
        return self

    def __next__(self) -> int:
        while self.i != self.n:
            self.i += 1
            for prime in self.prime_numbers:
                if self.i % prime == 0:
                    break
            else:
                self.prime_numbers.append(self.i)
                return self.i
        else:
            raise StopIteration


# TODO сделай один блок "if __name__ == '__main__'" и пиши все вызовы там, по кодлу не оч удобно вызовы искать
if __name__ == '__main__':
    prime_number_iterator = PrimeNumbers(n=10000)
    for number in prime_number_iterator:
        print(number)


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n: int) -> Generator:
    prime_numbers = []
    for num in range(2, n):
        for prime in prime_numbers:
            if num % prime == 0:
                break
        else:
            prime_numbers.append(num)
            yield num


if __name__ == '__main__':
    for number in prime_numbers_generator(n=10000):  # TODO по n включительно?
        print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.

def is_lucky_number(num: int) -> bool:
    str_num = str(num)
    length = len(str_num)
    if length == 1:
        return False
    half = length // 2
    # TODO можно обойтись без условного блока, если вспомнить срезы и как работают отрицательные числа внутри срезов
    if length % 2:
        # TODO можно сократить с помощью map
        return sum(int(i) for i in str_num[:half]) == sum(int(i) for i in str_num[half + 1:])
    else:
        return sum(int(i) for i in str_num[:half]) == sum(int(i) for i in str_num[half:])


if __name__ == '__main__':
    prime_number_iterator = PrimeNumbers(n=10000)
    '''Способ применения 1'''
    for value in filter(is_lucky_number, prime_number_iterator):
        print(value)

    '''Способ применения 2'''
    for value in prime_number_iterator:
        if is_lucky_number(value):
            print(value)


def is_palindrome(num: int) -> bool:
    # TODO функцию можно умесить буквально в одну-три строчки, если вспомнить срезы и их свойства
    str_num = str(num)
    length = len(str_num)
    if length == 1:
        return False
    half = length // 2
    for i in range(half):
        if str_num[i] != str_num[-i - 1]:
            return False
    else:
        return True


if __name__ == '__main__':
    '''Способ применения 1'''
    prime_number_iterator = PrimeNumbers(n=10000)
    for value in filter(is_palindrome, prime_number_iterator):
        print(value)

    '''Способ применения 2'''
    for value in prime_number_iterator:
        if is_palindrome(value):
            print(value)


if __name__ == '__main__':
    '''Смашанное применение'''
    prime_number_iterator = PrimeNumbers(n=10000)
    for value in filter(is_palindrome, filter(is_lucky_number, prime_number_iterator)):
        print(value)


'''моя функция-фильтр'''


def is_fibonachi(num: int) -> bool:
    a = 0
    b = 1
    while True:
        if a > num:
            return False
        a, b = b, a + b
        if a == num:
            return True


if __name__ == '__main__':
    prime_number_iterator = PrimeNumbers(n=10000)
    for value in filter(is_fibonachi, prime_number_iterator):
        print(value)
