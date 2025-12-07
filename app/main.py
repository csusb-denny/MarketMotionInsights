from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Market Analysis API is running."}