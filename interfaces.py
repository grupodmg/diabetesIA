from pydantic import BaseModel

class dataTest(BaseModel):
    nombre: str
    estudiante: float

class DiabetesData(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int