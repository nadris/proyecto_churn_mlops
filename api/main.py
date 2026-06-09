from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI(title="Servicio ML-Ops - Churn")

model = joblib.load("models/model.pkl")

@app.get("/")
def inicio():
    return {
        "mensaje": "Servicio ML-Ops activo",
        "estado": "ok",
        "autor": "Never Adrian Sossa"
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

@app.get("/health")
def health():
    return {
        "status": "running"
    }