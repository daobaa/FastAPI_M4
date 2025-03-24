from fastapi import FastAPI
from gestor import *

app = FastAPI()

@app.get("/")
def index():
    return("Institut TIC de Barcelona")

@app.get("/JSON/")
def get_file():
    return get_JSON

@app.post("/alumne/", response_model=Alumne)
def add_new(alumne: AlumneCreate):
    add_alumne(alumne)
    return alumne