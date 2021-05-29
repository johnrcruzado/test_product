import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from binance.client import Client

api_key = ""
api_secret = ""

client = Client(api_key, api_secret)
price_checker = 0


sell_plus = 200
buy_minus = 200
cancel_price = 400
#order_price = 35180.99
while True:

    orders = client.get_open_orders(symbol='BTCUSDT')
    balance = client.get_asset_balance(asset='BTC')
    current_coin = float(balance["free"][:8])
    current_price = client.get_symbol_ticker(symbol="BTCUSDT")
    current_price = float(current_price["price"])

    if orders:
        for x in range(len(orders)):
            order_id = orders[x]["orderId"]
            order_qty = orders[x]["origQty"]
            price = float(orders[x]["price"])
            side = orders[x]["side"]
            if side == "BUY":
                price_checker = current_price - float(price)
                if price_checker > cancel_price:
                    result = client.cancel_order(symbol='BTCUSDT', orderId=order_id)
                    pass
            time.sleep(1)

    else :
        if current_coin > 0.000226:
            print(current_coin)
            order = client.order_limit_sell(symbol='BTCUSDT', quantity=current_coin, price=order_price+sell_plus)
            print("sell coin :" ,str(current_coin) )
            current_coin = 0
            time.sleep(1)
        elif current_coin < 0.000126 :
             order_price = float(current_price) - buy_minus
             buy_order_limit = client.create_order(symbol='BTCUSDT', side='BUY', type='LIMIT', timeInForce='GTC', quantity=0.000426,
                                                  price=order_price)
             print("no order")
             time.sleep(2)

    if current_coin > 0.000226:
       order = client.order_limit_sell(symbol='BTCUSDT', quantity=current_coin, price=order_price+sell_plus)
       print("sell coin :" ,str(current_coin) )
       current_coin = 0
       time.sleep(1)

    time.sleep(10)
    print("current_price :", current_price, " coin_balance=", current_coin, "price_checker=", price_checker)
