from fastapi import FastAPI, HTTPException  # Importamos FastAPI y las excepciones HTTP
from gestor import *  # Importamos todas las funciones y modelos de gestor.py

# Creamos la aplicación FastAPI
app = FastAPI()

# Ruta de prueba para verificar que el servidor funciona
@app.get("/")
def index():
    return "Institut TIC de Barcelona"

# Endpoint para agregar un nuevo alumno
@app.post("/alumne/", response_model=Alumne)
def add_new(alumne: AlumneCreate):
    add_alumne(alumne)  # Llama a la función que añade el alumno al archivo JSON
    return alumne  # Devuelve los datos del alumno añadido

# Endpoint para obtener el número total de alumnos registrados
@app.get("/alumne/")
def num_users():
    alumnes = read_alumnes()  # Lee la lista de alumnos desde el archivo JSON
    return {"total_alumnes": len(alumnes)}  # Devuelve el número total de alumnos

# Endpoint para obtener los datos de un alumno por su ID
@app.get("/id/{numero}", response_model=Alumne)
def get_alumne(numero: int):
    alumne = get_alumne_by_id(numero)  # Busca el alumno en el archivo JSON
    if alumne is None:  # Si el alumno no existe, devuelve un error 404
        raise HTTPException(status_code=404, detail="Alumne no trobat")
    return alumne  # Devuelve los datos del