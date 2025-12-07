#1. VWAP Calculation Function
def calculate_vwap(candles):
    """
    Calculate the Volume Weighted Average Price (VWAP) from a list of candle data.

    Parameters:
        candles (list[dict]):
            A list of OHLCV candle dictionaries.
            Each candle must contain:
                - 'high'   (float): highest price in the candle
                - 'low'    (float): lowest price in the candle
                - 'close'  (float): closing price
                - 'volume' (float): trading volume during the candle

            Example:
            [
                {"high": 50, "low": 40, "close": 48, "volume": 20},
                {"high": 52, "low": 47, "close": 50, "volume": 35},
                ...
            ]

    Returns:
        float:
            The VWAP value computed as: sum(TP * Volume) / sum(Volume)
            Returns None if total volume = 0.

    Notes:
        - VWAP is computed using "Typical Price" = (High + Low + Close) / 3
        - VWAP weights each candle's price by the volume traded at that price.
        - VWAP resets each session (typically at market open).
    """
    #Sum-of-(Typical-Price*Volume)
    total_PriceVolume = 0

    #Sum-of-Volume
    total_Volume = 0

    #Loop-through-each-candle-in-the-dataset
    for c in candles:
        #Calculate-Typical-Price
        typical_price = (c['high'] + c['low'] + c['close']) / 3

        #Volume-for-the-candle
        Volume = c['volume']

        #Accumulate-Price*Volume
        total_PriceVolume += typical_price * Volume

        #Accumulate-Volume
        total_Volume += Volume

    #Prevent-division-by-zero
    if total_Volume == 0:
        return None

    #Return-VWAP-value
    return total_PriceVolume / total_Volume