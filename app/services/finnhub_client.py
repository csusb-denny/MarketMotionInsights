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
