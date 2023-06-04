import json
import requests


# Making a Get Request
def get_coin_tickers(url):
    req = requests.get(url)
    json_resp = json.loads(req.text)
    return json_resp


# Creating a List Valid Coins
def valid_coin_list():
    filtered_data = get_coin_tickers("https://api.poloniex.com/v2/currencies")
    coin_list = [item["coin"] for item in filtered_data]
    return coin_list


# Creating a List of Different Coin Exchange Possibilities
def possible_coins_for_arbitrage():
    coin_exchange_json = get_coin_tickers("https://api.poloniex.com/markets/price")
    coin_list = [item["symbol"] for item in coin_exchange_json]
    return coin_list

