# MarketMotionInsights

A realtime SPX/ES analytics microservice with alerts, VWAP signals, and probability engine

# VWAP Endpoint Flow:

# 1. Client calls /vwap?symbol=...

# 2. API retrieves candle data for the symbol

# 3. Passes data into calculate_vwap()

# 4. Returns the VWAP as JSON
