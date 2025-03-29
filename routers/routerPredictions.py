import pickle
from fastapi import FastAPI, APIRouter
import numpy as np
from interfaces import DiabetesData

router = APIRouter()

with open("RFDiabetesv132.pkl", "rb") as file:
    model = pickle.load(file)

@router.post("/predict")
def predict(data:DiabetesData):
    data = data.model_dump()
    print(data)

    Pregnancies=data["Pregnancies"]
    Glucose=data["Glucose"]
    BloodPressure=data["BloodPressure"]
    SkinThickness=data["SkinThickness"]
    Insulin=data["Insulin"]
    BMI=data["BMI"]
    DiabetesPedigreeFunction=data["DiabetesPedigreeFunction"]
    Age=data["Age"]

    data = np.array([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]).reshape(1, 8)

    prediction = model.predict(data)

    label_map = {0: "No Diabetes", 1: "Diabetes"}
    label = [label_map[p] for p in prediction]
    print("Label: ", label)
    return {"message": str(label)}

if __name__ == "__main__":
    router.run()