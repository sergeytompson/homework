# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#

import os
from threading import Thread
from typing import List
# from timer import func_timer


class VolatilityEstimator(Thread):

    def __init__(self, file: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file = file
        self.volatility = None
        self.ticker = None

    def run(self) -> None:
        with open(self.file) as f:
            prices = []
            f.readline()
            self.ticker, _, current_price, _ = f.readline().split(',')
            self._get_price(current_price, prices)
            for line in f:
                _, _, current_price, _ = line.split(',')
                self._get_price(current_price, prices)
            max_price, min_price = max(prices), min(prices)
            mid_price = (max_price + min_price) / 2
            self.volatility = round((max_price - min_price) / mid_price * 100, 2)

    @staticmethod
    def _get_price(price: str, lst: List) -> None:
        price = float(price)
        lst.append(price)


# @func_timer
def main(path):
    tickers = []
    zero_volatility = []
    estimators = []
    for dir_path, _, filenames in os.walk(path):
        for file in filenames:
            file_name = os.path.join(dir_path, file)
            estimators.append(VolatilityEstimator(file_name))
    for estimator in estimators:
        estimator.start()
    for estimator in estimators:
        estimator.join()
        if not estimator.volatility:
            zero_volatility.append(estimator.ticker)
        else:
            tickers.append((estimator.ticker, estimator.volatility))
    tickers.sort(key=lambda lst: lst[1])
    zero_volatility.sort()
    print('Максимальная волатильность:')
    for ticker, volatility in tickers[:-4:-1]:
        print(f'    {ticker} - {volatility}')
    print('Минимальная волатильность:')
    for ticker, volatility in tickers[2::-1]:
        print(f'    {ticker} - {volatility}')
    print('Нулевая волатильность:')
    print('    ', ', '.join(zero_volatility))


if __name__ == '__main__':
    tickers_storage = os.path.normpath('trades')
    main(tickers_storage)
