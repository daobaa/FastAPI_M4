from fastapi import FastAPI, HTTPException
from gestor import *

app = FastAPI()

@app.get("/")
def index():
    return("Institut TIC de Barcelona")

@app.post("/alumne/", response_model=Alumne)
def add_new(alumne: AlumneCreate):
    add_alumne(alumne)
    return alumne

@app.get("/alumne/")
def num_users():
    alumnes = read_alumnes()
    return {"total_alumnes": len(alumnes)}

@app.get("/id/{numero}", response_model=Alumne)
def get_alumne(numero: int):
    alumne = get_alumne_by_id(numero)
    if alumne is None:
        raise HTTPException(status_code=404, detail="Alumne no trobat")
    return alumne

@app.delete("/del/{numero}")
def delete_alumne(numero: int):
    success = delete_alumne_by_id(numero)
    if not success:
        raise HTTPException(status_code=404, detail="Alumne no trobat")
    return {"message": f"Alumne amb ID {numero} esborrat correctament"}