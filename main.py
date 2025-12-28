from exchange_rate import ExchangeRatesAPI

er = ExchangeRatesAPI()
rate = er.get_rates(1, "EUR", "COP")

print(rate)