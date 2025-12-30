from binance import Client
from binance.enums import *
from config import API_KEY, API_SECRET, BASE_URL
from logger import setup_logger
import logging
import sys

class BasicBot:
    def __init__(self):
        setup_logger()
        self.client = Client(API_KEY, API_SECRET)
        self.client.FUTURES_URL = BASE_URL
        logging.info("Connected to Binance Futures Testnet")

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logging.info(f"Market Order Success: {order}")
            print("Order Executed:", order)
        except Exception as e:
            logging.error(str(e))
            print("Error:", e)

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price
            )
            logging.info(f"Limit Order Placed: {order}")
            print("Order Placed:", order)
        except Exception as e:
            logging.error(str(e))
            print("Error:", e)

    def place_stop_limit(self, symbol, side, quantity, stop_price, limit_price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=FUTURE_ORDER_TYPE_STOP,
                stopPrice=stop_price,
                price=limit_price,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity
            )
            logging.info(f"Stop-Limit Order: {order}")
            print("Stop-Limit Order Placed:", order)
        except Exception as e:
            logging.error(str(e))
            print("Error:", e)

def clear():
    print("\n" * 2)

def menu():
    print("=" * 40)
    print("      BINANCE FUTURES TRADING BOT BY GOURAV")
    print("=" * 40)
    print("1. Market Order")
    print("2. Limit Order")
    print("3. Stop-Limit Order")
    print("0. Exit")
    print("=" * 40)

def main():
    bot = BasicBot()

    print("\n=== Binance Futures Trading Bot BY GOURAV ===")
    print("1. Market Order")
    print("2. Limit Order")
    print("3. Stop-Limit Order")

    choice = input("Select order type: ")

    symbol = input("Symbol (e.g. BTCUSDT): ").upper()
    side = input("Side (BUY / SELL): ").upper()
    quantity = float(input("Quantity: "))

    if choice == "1":
        bot.place_market_order(symbol, side, quantity)

    elif choice == "2":
        price = float(input("Limit Price: "))
        bot.place_limit_order(symbol, side, quantity, price)

    elif choice == "3":
        stop_price = float(input("Stop Price: "))
        limit_price = float(input("Limit Price: "))
        bot.place_stop_limit(symbol, side, quantity, stop_price, limit_price)

    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
