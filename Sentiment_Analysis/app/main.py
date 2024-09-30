from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import model_predict


app = FastAPI()


class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    language: str


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": "0.1.0"}


@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    sentiment = model_predict(payload.text)
    return {"sentiment": sentiment}