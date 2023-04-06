import requests

from config_bot import money

class APIException(Exception):
    def __init__(self, message):
        self.message = message

class CurrencyConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = money[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = money[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}\n Если дробное число, то записывается через точку')

        url = f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}'

        r = requests.request("GET", url)
        result = r.json()
        total_base = round(float(result[base_ticker]) * amount, 2)
        return total_base

