from fastapi import FastAPI, HTTPException
from interfaces import dataTest
app = FastAPI()

cursos = {
    "programacion": {"fundamentos": 15, "POO": 20},
    "matematicas": {"matEspeciales": 20, "calculoVect": 25},
}

@app.get("/cursos/{tipo}")
def tipo_cursos(tipo: str):
    if tipo not in cursos:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    return {"cursos": cursos[tipo]}

@app.get("/cursos")
def get_cursos():
    return cursos

@app.post("/asignatura")
def asignatura(data: dataTest):
    data = data.model_dump()
    print(data)
    return {"asignatura": data}