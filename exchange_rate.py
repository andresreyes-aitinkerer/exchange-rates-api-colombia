import json
from requests import get
from datetime import datetime


class ExchangeRatesAPI:

	def __init__(self):

		self.api_url = "https://www.exchange-rates.org"
		self.api_version = "v2"
		self.headers = {
			'authority': 'www.exchange-rates.org',
			'accept': '*/*',
			'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6',
			'referer': 'https://www.exchange-rates.org/it/',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
		}

	def convert_date(self, original_date: str) -> str:
		"""

		:param original_date:
		:return:
		"""
		converted_date = datetime.strptime(original_date, "%Y-%m-%dT%H:%M:%S").strftime("%d/%m/%y %H:%M")
		return converted_date

	def processing_res(self, res: dict) -> dict:
		"""
		Elabora la risposta dell'API,
		eliminando chiavi indesiderate e convertendo le chiavi in minuscolo.
		"""
		res['daterate'] = self.convert_date(res['UpdatedDateTimeUTC'])

		# Chiavi da eliminare
		keys_to_remove = ["ConverterResult", "FromLine1",
		                  "FromLine2", "ToLine1", "ToLine2",
		                  "FormattedResult", "BottomDirectDesc",
		                  "BottomIndirectDesc", "FormattedDateTime",
		                  "UpdatedDateTimeUTC"]

		res = {k.lower(): v for k, v in res.items() if k not in keys_to_remove}
		return res

	def get_rates(self, amount: int, from_currency: str, to_currency:str):
		"""

		:param amount:
		:param from_currency:
		:param to_currency:
		:return:
		"""
		url = f"{self.api_url}/it/api/{self.api_version}/rates/lookup?isoTo={to_currency}&isoFrom={from_currency}&amount={amount}"
		response = get(url, headers=self.headers)
		res = json.loads(response.text)
		res = self.processing_res(res)
		return res