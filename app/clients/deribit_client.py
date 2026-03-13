import aiohttp

class DeribitClient():
    def __init__(self):
        self.url = "https://www.deribit.com/api/v2/public/get_index_price"

    async def get_price(self, ticker: str) -> float:
        """Функция для получения цены валюты

        Args:
            ticker (str): тикер (btc_usd, eth_usd)

        Returns:
            float: цена валюты
        """
        param = {"index_name": ticker}

        async with aiohttp.ClientSession() as session:
            async with session.get(self.url, params=param) as response:
                # Проверяем, что запрос прошел успешно
                response.raise_for_status()

                # JSON ответ -> словарь
                data = await response.json()

                # Цена из структуры ответа Deribit
                price = data.get("result", {}).get("index_price")

                return float(price)

