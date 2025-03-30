import json  # Módulo para manejar archivos JSON
from pathlib import Path  # Módulo para verificar si un archivo existe
from pydantic import BaseModel  # Pydantic para validación de datos
from typing import Optional  # Para definir campos opcionales en los modelos

# Definimos el modelo de la fecha de nacimiento de un alumno
class Data(BaseModel):
    dia: Optional[int] = None
    mes: Optional[int] = None
    any: Optional[int] = None

# Modelo base para la creación de un alumno (sin ID)
class AlumneCreate(BaseModel):
    nom: str = ""
    cognom: str = ""
    data: Data  # Usa el modelo Data para la fecha
    email: str = ""
    feina: bool = False
    curs: str = ""

# Modelo de alumno completo (incluye ID)
class Alumne(AlumneCreate):
    id: int  # Añadimos el ID al modelo Alumne

# Ruta del archivo donde se almacenan los alumnos
FILE_PATH = "alumnes.json"

# Crea el archivo JSON si no existe
def create_JSON():
    if not Path(FILE_PATH).exists():  # Verifica si el archivo existe
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)  # Si no existe, crea un archivo vacío

# Lee la lista de alumnos desde el archivo JSON
def read_alumnes():
    create_JSON()  # Asegura que el archivo existe antes de leer
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)  # Devuelve la lista de alumnos

# Obtiene el siguiente ID disponible para un nuevo alumno
def get_next_id():
    alumnes = read_alumnes()  # Lee la lista de alumnos
    if alumnes:
        max_id = max([alumne["id"] for alumne in alumnes])  # Encuentra el ID más alto
        return max_id + 1  # Retorna el siguiente ID disponible
    else:
        return 1  # Si no hay alumnos, el primer ID es 1

# Agrega un nuevo alumno al archivo JSON
def add_alumne(data: AlumneCreate):
    alumnes = read_alumnes()  # Carga la lista de alumnos
    new_id = get_next_id()  # Obtiene el nuevo ID
    alumne_data = data.model_dump()  # Convierte el objeto Pydantic a diccionario
    alumne_data["id"] = new_id  # Asigna el nuevo ID
    alumnes.append(alumne_data)  # Agrega el nuevo alumno a la lista
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(alumnes, f, indent=4)  # Guarda los datos en el archivo JSON

# Devuelve la lista completa de alumnos (sin modificarla)
def get_JSON():
    return read_alumnes()

# Busca un alumno por su ID
def get_alumne_by_id(alumne_id: int):
    alumnes = read_alumnes()  # Carga la lista de alumnos
    for alumne in alumnes:
        if alumne["id"] == alumne_id:  # Si el ID coincide, retorna el alumno
            return alumne
    return None  # Si no se encuentra, retorna None

# Elimina un alumno por su ID
def delete_alumne_by_id(alumne_id: int):
    alumnes = read_alumnes()  # Carga la lista de alumnos
    updated_alumnes = [alumne for alumne in alumnes if alumne["id"] != alumne_id]  # Filtra los alumnos eliminando el que tiene el ID especificado

    if len(updated_alumnes) == len(alumnes):  # Si la lista no cambió, el alumno no existía
        return False

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(updated_alumnes, f, indent=4)  # Guarda la lista actualizada

    return True  # Retorna True si el alumno fue eliminado correctamente