"""
Finnhub API Client Module

This module will provide a simple wrapper around finnhub python sdk
to interact with the Finnhub API for Market Data: Quotes, News, Financials, etc.

Functions:
get_realtime_quote(symbol: str) -> dict
    Fetches real-time quote data for the given stock symbol.

Notes:
Requires valid finnhub key(free)
finnhub supports stocks, crypto, forex
rate limits apply (since we are using the free version 60api per min)
module only retrieves the most basic quote data, but can be expanded later to include more functionality
"""
import finnhub

client = finnhub.Client(api_key="d4r2ur1r01qrphad1d2gd4r2ur1r01qrphad1d30")

def get_realtime_quote(symbol: str):
    """
    Retrieve a real-time quote for the specified symbol.

    Parameters
    ----------
    symbol : str
        Ticker symbol to query (e.g., "AAPL", "TSLA", "BTC-USD").

    Returns
    -------
    dict
        A dictionary containing:
            - 'symbol' : The input symbol.
            - 'current' : Current price.
            - 'high' : High price of the day.
            - 'low' : Low price of the day.
            - 'open' : Opening price of the day.
            - 'previous_close' : Previous day closing price.
            - 'timestamp' : Unix timestamp of the quote update.

        Example:
        {
            "symbol": "AAPL",
            "current": 182.34,
            "high": 185.22,
            "low": 180.94,
            "open": 181.77,
            "previous_close": 180.20,
            "timestamp": 1717555098
        }

    Notes
    -----
    - Symbol names must match Finnhub's supported format.
    - Returned values may be None if Finnhub does not provide the field.
    - Best used for real-time dashboards or indicator processing.
    """
    data = client.quote(symbol)

    return {
        "symbol": symbol,
        "current": data.get('c'),
        "high": data.get('h'),
        "low": data.get('l'),
        "open": data.get('o'),
        "previous_close": data.get('pc'),
        "timestamp": data.get('t')
    }


def get_candles(symbol: str, resolution: str = "1", loopback_minutes: int = 30):
    """
    Retrieve historical candle data for the specified symbol.

    Parameters:
    symbol : str
        Ticker symbol to query (e.g., "AAPL", "TSLA", "BTC-USD").
    resolution : str
        Time resolution of the candles. Options include:
        "1" - 1 minute
        "5" - 5 minutes
        "15" - 15 minutes
        "30" - 30 minutes
        "60" - 1 hour
        "D" - Daily
        "W" - Weekly
        "M" - Monthly
    Returns:
    list[dict]
        A list of dictionaries, each containing:
            - 'timestamp' : Unix timestamp of the candle.
            - 'open' : Opening price.
            - 'high' : High price.
            - 'low' : Low price.
            - 'close' : Closing price.
            - 'volume' : Volume traded. 
    """
    import time
    now = int(time.time()) # current time in seconds
    past = now - (loopback_minutes * 60)  # loopback in seconds

    data = client.stock_candles(symbol, resolution, past, now)

    if data.get("s") != "ok":   # if status is not ok, return empty list
        return []
    

    candles = []
    for h, l, c, v in zip(data['h'], data['l'], data['c'], data['v']):
        candles.append({
            "high": h,
            "low": l,
            "close": c,
            "volume": v
        })

    return candles