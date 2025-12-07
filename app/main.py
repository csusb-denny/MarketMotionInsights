from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Market Analysis API is running."}

#What happens when a clients ask for a API request for VWAP calculation?
#Client makes a request
#Step 1:
#GET /vwap?symbol=SPX

#Step 2: FastAPI recieves Request
#route function runs:
@app.get("/vwap")
def get_vwap(symbol: str):
    """
    candles: list of dicts with keys ['high', 'low', 'close', 'volume']
    """
    total_PriceVolume = 0 #Sum of (Typical Price * Volume)
    Volume = 0      #Sum of Volume

    for c in candles:
        typical_price = (c['high'] + c['low'] + c['close']) / 3
        total_Volume += c['volume']

        total_PriceVolume += typical_price * Volume 
        total_Volume += Volume
    
    if total_Volume == 0:
        return None # Avoid division by zero
    return total_PriceVolume / total_Volume

#Step 3: Data Retrieval
#Fetch recent candle data from: Database
#Vwap requires: Price, Volume, Times Series


#Step 4: VWAP Calculation
#Typical Price = (High + Low + Close) / 3
#VWAP = sum(typicalPrice * Volume) / sum(Volume)

#Step 5: Response is sent back to Client
#FastAPI sends JSON response with VWAP value