import random

def generate_candles(count: int = 10):
    """
    Generate a list of random OHLCV candles for testing market indicators.

    This function simulates realistic market candle behavior by starting from
    a base price and generating fluctuations for each candle. Useful for testing
    the VWAP endpoint, plotting, or stress-testing indicator logic without needing
    live market data.

    Parameters:
    ----------
    count : int, optional
        Number of candles to generate (default is 10).

    Returns:
    -------
    list[dict]
        A list of candle dictionaries. Each candle contains:
            - 'high'   (float): highest price in the candle
            - 'low'    (float): lowest price in the candle
            - 'close'  (float): closing price
            - 'volume' (int): trading volume for the candle

        Example output:
        [
            {"high": 101.23, "low": 98.44, "close": 99.50, "volume": 52},
            {"high": 100.87, "low": 97.90, "close": 98.66, "volume": 110},
            ...
        ]

    Notes:
    -----
    - Each candle's range (high/low/close) is based on the previous candle's
      closing price, giving a more natural price progression.
    - 'volume' is generated as a random integer to approximate varying liquidity.
    - Ideal for testing indicators such as VWAP, SMA, EMA, RSI, etc., when real
      market data is not available.
    """

    candles = []
    price = 100  # starting price

    for _ in range(count):
        high = price + random.uniform(0, 3)
        low = price - random.uniform(0, 3)
        close = random.uniform(low, high)
        volume = random.randint(10, 200)

        candles.append({
            "high": round(high, 2),
            "low": round(low, 2),
            "close": round(close, 2),
            "volume": volume
        })

        price = close  # next candle starts from previous close

    return candles
