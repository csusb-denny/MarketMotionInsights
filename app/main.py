from fastapi import FastAPI
from app.indicators.vwap import calculate_vwap
from app.utils.candle_generator import generate_candles
from app.services.finnhub_client import get_realtime_quote, get_candles


app = FastAPI()
app.state.candles = {} #stores candles per ticker symbol
#1. Root Endpointer
@app.get("/")
def root():
    return {"message": "Market Analysis API is running."}

#2. VWAP ENDPOINT
@app.post("/vwap")
def vwap_endpoint(candles: list[dict]):
    """
    Calculate VWAP from provided candle data
    """ 
    return {"vwap": calculate_vwap(candles)}

#3. Candle Generation Endpoint
@app.get("/generate_candles")
def generate(count: int = 10):
    """
    Generate synthetic candle data
    """ 
    candles = generate_candles(count)
    return {"candles": candles}

@app.get("/quote/{symbol}")
def quote(symbol: str):
    """
    Get real-time quote for a given symbol
    """ 
    quote_data = get_realtime_quote(symbol.upper())
    return {"quote": quote_data}

#4. VWAP from Real Data Endpoint
@app.get("/vwap/{symbol}")
def vwap_realtime(symbol: str):

    symbol = symbol.upper()

    # 1. Pull real-time quote from Finnhub
    quote = get_realtime_quote(symbol)

    if not quote or "current" not in quote or quote["current"] is None:
        return {"error": f"Could not retrieve quote for {symbol}"}

    # 2. Convert quote into a synthetic candle
    candle = {
        "high": quote["high"],
        "low": quote["low"],
        "close": quote["current"],
        "volume": quote.get("volume", 1)  # If no volume, use 1 so math doesn't break
    }

    # 3. Get existing candle list or create a new one
    candles = app.state.candles.get(symbol, [])

    # Add the new candle
    candles.append(candle)

    # 4. Rolling window (use last 30 candles)
    candles = candles[-30:]

    # Save back to memory
    app.state.candles[symbol] = candles

    # 5. Calculate VWAP using your existing function
    vwap_value = calculate_vwap(candles)

    return {
        "symbol": symbol,
        "vwap": vwap_value,
        "candles_used": len(candles),
        "last_price": quote["current"],
        "last_volume": quote.get("volume", 1)
    }
