import arbitrage_calculations
import arbitrage_functions
import json
import requests
import time

"""
    Step 1: Finding Tradeable Coins
"""


def step_1():
    # Getting the Different Coin Exchange Possibilities
    coin_list = arbitrage_functions.possible_coins_for_arbitrage()

    return coin_list


"""
    Step 2: Structuring Triangular Arbitrage Pairs
"""


def step_2(coin_list):
    # Structure the list of tradeable triangular arbitrage pairs
    structured_list = arbitrage_calculations.structure_triangular_pairs(coin_list)

    # Save structured list
    with open("structured_triangular_pairs.json", "w") as fp:
        json.dump(structured_list, fp)


"""
    Step 3: Calculating Surface Arbitrage Opportunities
"""


def step_3():
    # Get Structured Pairs
    with open("structured_triangular_pairs.json") as json_file:
        structured_pairs = json.load(json_file)

    # print(structured_pairs)

    prices_json = arbitrage_functions.get_coin_tickers("https://api.poloniex.com/markets/ticker24h")

    for t_pair in structured_pairs:
        prices_dict = arbitrage_calculations.get_price_for_t_pair(t_pair, prices_json)
        surface_arb = arbitrage_calculations.calc_triangular_arb_surface_rate(t_pair, prices_dict)


""" MAIN """
if __name__ == "__main__":
    # print("Retrieving list of cryptos...")
    # coin_list = step_1()
    #
    # print("Structuring cryptos into triangular pairs (2 mins)...")
    # structured_pairs = step_2(coin_list)
    #
    # print("Running scanning algorithm (will run until killed)...")
    # while True:
    #     time.sleep(1)
    #     step_3()
    arbitrage_calculations.get_depth_from_orderbook()