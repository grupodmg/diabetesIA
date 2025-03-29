import pickle
from fastapi import FastAPI
import numpy as np

from interfaces import DiabetesData

app = FastAPI()

with open("RFDiabetesv132.pkl", "rb") as file:
    model = pickle.load(file)

@app.get("/")
def index():
    return {"message": "API2 RUNNING"}


@app.post("/predict")
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

    label_map = {0: "Si Diabetes", 1: "No Diabetes"}
    label = [label_map[p] for p in prediction]
    print("Label: ", label)
    return {"message": str(label)}

if __name__ == "__main__":
    app.run()