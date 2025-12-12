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
def vwap_realtime(symbol: str, resolution: str = "1", loopback_minutes: int = 30):

    symbol = symbol.upper()

    #1. Pull real-time quote from Finnhub
    quote = get_realtime_quote(symbol)
    #2. Create a new candle from the quote
    candles = get_candles(symbol = symbol, resolution = resolution, loopback_minutes= loopback_minutes)
    #3. Validate candle data
    if not candles:
        return {"error": "No candle data available for symbol."}
    #4. Calculate VWAP using existing function
    vwap_value = calculate_vwap(candles)

    return {
        "symbol": symbol,
        "vwap": vwap_value,
        "candles_used": len(candles),
        "resolution": f"{resolution} m",
        "lookback_minutes": loopback_minutes,
        "source": "Finnhub",
        "calculation": "VWAP calculated using historical candles from Finnhub."
    }
