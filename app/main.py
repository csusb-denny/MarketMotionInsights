from fastapi import FastAPI
from app.indicators.vwap import calculate_vwap
from app.utils.candle_generator import generate_candles

app = FastAPI()

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