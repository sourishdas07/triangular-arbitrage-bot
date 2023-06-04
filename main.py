import arbitrage_calculations
import json
import requests
import time

"""
    Step 0: Finding Tradeable Coins
"""

# Getting the Valid Coins
currency_data_url = "https://api.poloniex.com/v2/currencies"
currency_data_req = requests.get(currency_data_url)
currency_data_json = json.loads(currency_data_req.text)

filtered_data = [item for item in currency_data_json if item["tradeEnable"]]
symbol_list = [item["coin"] for item in filtered_data]

print(len(symbol_list))

# Getting the Different Coin Exchange Possibilities
market_price_url = "https://api.poloniex.com/markets/price"
market_price_req = requests.get(market_price_url)
market_price_json = json.loads(market_price_req.text)

coin_list = [item["symbol"] for item in market_price_json]

print(len(coin_list))


"""
    Step 1: Structuring Triangular Arbitrage Pairs
"""

structured_list = arbitrage_calculations.structure_triangular_pairs(coin_list)

# Saving Structured List
with open("structured_triangular_pairs.json", "w") as fp:
    json.dump(structured_list, fp)



"""
    Step 2: Calculating Surface Arbitrage Opportunities
"""

# Get Structured Pairs
with open("structured_triangular_pairs.json") as json_file:
    structured_pairs = json.load(json_file)

print(structured_pairs)
