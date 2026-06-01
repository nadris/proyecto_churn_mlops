# Proyecto Churn MLOps

Proyecto de Machine Learning para predecir abandono de clientes (churn) con un flujo simple de MLOps: datos, entrenamiento, serializacion del modelo y exposicion por API.

## Que incluye este proyecto

- Entrenamiento de modelo de clasificacion con `scikit-learn`
- Dataset de churn en `data/churn.csv` (ampliado con miles de registros sinteticos)
- API REST con FastAPI para consultar predicciones
- Dockerfile para ejecucion en contenedor
- Test basico de consumo de endpoint

## Estructura del repositorio

- `data/`: dataset fuente (`churn.csv`)
- `src/`: scripts de entrenamiento y prediccion local
- `api/`: servicio REST (FastAPI)
- `models/`: artefactos entrenados (`model.pkl`)
- `tests/`: pruebas simples de la API

## Requisitos

- Python 3.10+ (recomendado 3.12)
- `pip`
- (Opcional) Docker Desktop para despliegue en contenedor

## Instalacion

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Flujo rapido (end-to-end)

### 1) Entrenar modelo

```bash
python3 src/train.py
```

Este script:
- carga `data/churn.csv`
- entrena un `RandomForestClassifier`
- calcula `Accuracy`, `Precision`, `Recall` y `F1`
- guarda el modelo en `models/model.pkl`

### 2) Prediccion local por script

```bash
python3 src/predict.py
```

### 3) Levantar API local

```bash
uvicorn main:app --app-dir api --host 0.0.0.0 --port 8001
```

> Nota: se usa `--app-dir api` para asegurar que se cargue el `main.py` correcto del proyecto.

### 4) Probar endpoints

En otra terminal:

```bash
curl http://localhost:8001/
curl http://localhost:8001/predict
```

Respuesta esperada:
- `/` -> `{"status":"running"}`
- `/predict` -> `{"prediction":0|1}`

## Docker

### Build de imagen

```bash
docker build -t churn-api .
```

### Ejecutar contenedor

```bash
docker run --rm -p 8001:8000 churn-api
```

Luego probar:

```bash
curl http://localhost:8001/
curl http://localhost:8001/predict
```

## Dataset

Archivo: `data/churn.csv`

Columnas:
- `edad`
- `salario`
- `productos`
- `churn` (0 = no churn, 1 = churn)

## Pruebas

```bash
pytest -q
```

## Troubleshooting rapido

- Error de Docker daemon: inicia Docker Desktop antes de ejecutar `docker build` o `docker run`.
- Error al cargar app con Uvicorn: usa el comando recomendado con `--app-dir api`.
- Error de modelo no encontrado: ejecuta primero `python3 src/train.py`.
