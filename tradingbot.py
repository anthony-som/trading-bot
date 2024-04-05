from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

trading_client = TradingClient(API_KEY, API_SECRET)


market_order_data = MarketOrderRequest(
    symbol="BTC/USD",
    qty=1.2,
    side=OrderSide.BUY,
    time_in_force=TimeInForce.GTC
)

market_order = trading_client.submit_order(market_order_data)
print(market_order)