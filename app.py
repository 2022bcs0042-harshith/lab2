# from fastapi import FastAPI
# import joblib
# import numpy as np

# app = FastAPI()

# # Load trained model
# model = joblib.load("outputs/model/model.pkl")


# @app.get("/")
# def home():
#     return {"message": "Wine Quality Prediction API"}

# @app.post("/predict")
# def predict(
#     fixed_acidity: float,    
#     volatile_acidity: float,
#     citric_acid: float,
#     residual_sugar: float,
#     chlorides: float,
#     free_sulfur_dioxide: float,
#     total_sulfur_dioxide: float,
#     density: float,
#     pH: float,
#     sulphates: float,
#     alcohol: float
# ):
#     features = np.array([[fixed_acidity, volatile_acidity, citric_acid,
#                           residual_sugar, chlorides, free_sulfur_dioxide,
#                           total_sulfur_dioxide, density, pH,
#                           sulphates, alcohol]])

#     prediction = model.predict(features)

#     return {
#         "name": "RALLAPALLI V S B HARSHITH",
#         "roll_no": "2022BCS0042",
#         "predicted_wine_quality": float(prediction[0])
#     }



from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load trained model
model = joblib.load("outputs/model/model.pkl")


# -------------------------------
# Health Endpoint (Required)
# -------------------------------
@app.get("/health")
def health():
    return {"status": "ok"}


# -------------------------------
# Home Endpoint
# -------------------------------
@app.get("/")
def home():
    return {"message": "Wine Quality Prediction API"}


# -------------------------------
# Request Body Schema
# -------------------------------
class WineFeatures(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float


# -------------------------------
# Predict Endpoint
# -------------------------------
@app.post("/predict")
def predict(features: WineFeatures):

    input_data = np.array([[
        features.fixed_acidity,
        features.volatile_acidity,
        features.citric_acid,
        features.residual_sugar,
        features.chlorides,
        features.free_sulfur_dioxide,
        features.total_sulfur_dioxide,
        features.density,
        features.pH,
        features.sulphates,
        features.alcohol
    ]])

    prediction = model.predict(input_data)

    return {
        "name": "RALLAPALLI V S B HARSHITH",
        "roll_no": "2022BCS0042",
        "predicted_wine_quality": float(prediction[0])
    }
