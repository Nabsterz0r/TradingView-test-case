from django.core.management.base import BaseCommand
from django.utils import timezone

from api.models import Symbol

import requests
import time

class Command(BaseCommand):
    def handle(self, *args, **options):
        stats_grabber = StatsGrabber()

class StatsGrabber():
    def __init__(self):
        print('im worked!')
        self.api_key = 'HNPFXIJ0XWY6Y92L'
        self.get_stats()

    def get_stats(self):
        self.get_symbols()

        for symbol in self._symbols:
            try:
                if symbol.type == 'DIGITAL_CURRENCY_DAILY':
                    url = self.get_url(symbol)
                    response = requests.get(url).json()
                    time_series = response['Time Series (Digital Currency Daily)']
                    self.set_symbol_values(symbol, time_series, '4a. close ({0})'.format(symbol.market))

                elif symbol.type == 'TIME_SERIES_DAILY':
                    url = self.get_url(symbol)
                    response = requests.get(url).json()
                    time_series = response['Time Series (Daily)']
                    self.set_symbol_values(symbol, time_series)
                time.sleep(20)
                print('successfull get stats for {0}'.format(symbol))
            except:
                print('error :(')

        time.sleep(600)
        self.get_stats()

    def get_url(self, symbol):
        url = 'https://www.alphavantage.co/query?function={0}&symbol={1}&market={2}&apikey={3}'.format(
            symbol.type,
            symbol.name,
            symbol.market,
            self.api_key)
        return url

    def set_symbol_values(self, symbol, time_series, close_key='4. close'):
        current_date, previous_date = list(time_series.keys())[0], list(time_series.keys())[1]
        current_price = time_series[current_date][close_key]
        previous_price = time_series[previous_date][close_key]
        symbol.price = float(current_price)
        symbol.close = float(previous_price)
        symbol.precent = self.get_symbol_precent(symbol)
        symbol.delta = self.get_symbol_delta(symbol)
        symbol.save()

    def get_symbol_precent(self, symbol):
        precent =  100 - (symbol.price * 100 / symbol.close)
        precent = round(precent, 2)
        return precent

    def get_symbol_delta(self, symbol):
        delta = symbol.close - symbol.price
        delta = round(delta, 2)
        return delta

    def get_symbols(self):
        symbols = Symbol.objects.all()
        self._symbols = symbols


if __name__ == "__main__":
    s = StatsGrabber()
    print('main')