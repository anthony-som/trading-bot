from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

trading_client = TradingClient(API_KEY, API_SECRET)


from alpaca.data.live import CryptoDataStream

stream = CryptoDataStream(API_KEY, API_SECRET)

async def handle_trade(data):
    print(data)
    
stream.subscribe_quotes(handle_trade, "BTC/USD")

stream.run()