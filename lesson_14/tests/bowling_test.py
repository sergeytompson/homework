# -*- coding: utf-8 -*-

from homework.lesson_14.bowling import bowling, bowling_errors
import unittest


class BowlingTest(unittest.TestCase):

    def test_normal(self):
        result = bowling.get_score('X2/34-12---X5/72-6')
        self.assertEqual(result, 95, 'Функция некорректно подсчитывает очки')

    def test_strike(self):
        result = bowling.get_score('XXXXXXXXXX')
        self.assertEqual(result, 200, msg='Функция неправильно считает страйки')

    def test_finishing(self):
        result = bowling.get_score('1/2/3/4/5/6/7/8/9/1/')
        self.assertEqual(result, 150, msg='Функция неверно считает добивания')

    def test_miss(self):
        result = bowling.get_score('--------------------')
        self.assertEqual(result, 0, msg='Функция не может посчитать промахи')

    def test_wrong_type(self):
        self.assertRaises(TypeError, bowling.get_score, 1)

    def test_wrong_symbol(self):
        self.assertRaises(bowling_errors.IncorrectSymbolError, bowling.get_score, '%XXXXXXXXX')

    def test_too_mach(self):
        self.assertRaises(bowling_errors.ExcessSkittlesError, bowling.get_score, '99999999999999999999')

    def test_finishing_first(self):
        self.assertRaises(bowling_errors.BackSlashInFirstThrowError, bowling.get_score, '/')

    def test_second_X(self):
        self.assertRaises(bowling_errors.XInSecondThrowError, bowling.get_score, '1X')


if __name__ == '__main__':
    unittest.main()
