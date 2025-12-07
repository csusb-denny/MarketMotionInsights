from fastapi import FastAPI
from app.indicators.vwap import calculate_vwap

app = FastAPI()

#2. Root Endpointer
@app.get("/")
def root():
    return {"message": "Market Analysis API is running."}

# 3. VWAP ENDPOINT
@app.get("/vwap")
def get_vwap(symbol: str):
    mock_candles = [
        {"high": 50, "low": 40, "close": 48, "volume": 20},
        {"high": 52, "low": 47, "close": 50, "volume": 35},
        {"high": 55, "low": 53, "close": 54, "volume": 15}
    ]
    return {"symbol": symbol, "vwap": calculate_vwap(mock_candles)}