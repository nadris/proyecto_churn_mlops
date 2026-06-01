from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI(
    title="Churn Prediction API"
)

model = joblib.load("models/model.pkl")

@app.get("/")
def home():
    return {
        "status": "running"
    }

@app.get("/predict")
def predict():

    data = pd.DataFrame({
        "edad": [20],
        "salario": [200],
        "productos": [1]
    })

    pred = model.predict(data)

    return {
        "prediction": int(pred[0])
    }
