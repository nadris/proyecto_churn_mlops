# Proyecto Churn MLOps

## Objetivo

Implementar un modelo de Machine Learning para predecir abandono de clientes (Churn) utilizando buenas prácticas de MLOps.

## Estructura

- data: dataset
- src: entrenamiento y predicción
- api: servicio REST
- models: modelos entrenados

## Instalación

pip install -r requirements.txt

## Entrenamiento

python src/train.py

## Predicción

python src/predict.py

## API

uvicorn api.main:app --reload
