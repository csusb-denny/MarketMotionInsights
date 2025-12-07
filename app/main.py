from fastapi import FastAPI
from app.indicators.vwap import calculate_vwap

app = FastAPI()

#2. Root Endpointer
@app.get("/")
def root():
    return {"message": "Market Analysis API is running."}

# 3. VWAP ENDPOINT
@app.post("/vwap")
def vwap_endpoint(candles: list[dict]):
    """
    Calculate VWAP from provided candle data
    """ 
    return {"vwap": calculate_vwap(candles)}