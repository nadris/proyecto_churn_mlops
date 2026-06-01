import joblib
import pandas as pd

model = joblib.load("models/model.pkl")

cliente = pd.DataFrame({
    "edad": [20],
    "salario": [40],
    "productos": [1]
})

pred = model.predict(cliente)

print("Predicción:", pred[0])
