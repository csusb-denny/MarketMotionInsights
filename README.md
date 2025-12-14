MarketMotionInsights

A realtime SPX/ES analytics microservice with alerts, VWAP signals, and probability engine

This project is a backend Market Analytics API built with FastAPI that computes VWAP (Volume Weighted Average Price) using live market data from Finnhub.
It is designed to be production-aware, handling real-world API limitations gracefully while still delivering consistent analytics output.

🛠 Tech Stack

Python

FastAPI

Finnhub API

Uvicorn

Swagger / OpenAPI

🚀 Features

Real-time VWAP calculation

Configurable time window & resolution

Finnhub API integration

Graceful fallback when historical data is unavailable

Clean, modular architecture

Interactive API documentation (Swagger UI)

🧠 How It Works (Request Flow)

A user sends a request with a ticker symbol (e.g. TSLA)

The API attempts to fetch historical candle data from Finnhub

If candle data is available:

VWAP is computed over the requested rolling time window

If candle data is restricted by API permissions:

The system automatically falls back to real-time quote data

A synthetic candle is generated to ensure uninterrupted VWAP computation

The API returns:

VWAP value

Number of candles used

Data source used

Calculation method metadata

This design ensures reliability, transparency, and resilience in real-world environments.
