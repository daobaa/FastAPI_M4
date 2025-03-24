import json
from pathlib import Path
from pydantic import BaseModel
from typing import Optional

class Data(BaseModel):
    dia: Optional[int] = None
    mes: Optional[int] = None
    any: Optional[int] = None

class AlumneCreate(BaseModel):
    nom: str = ""
    cognom: str = ""
    data: Data
    email: str = ""
    feina: bool = False
    curs: str = ""

class Alumne(AlumneCreate):
    id: int

FILE_PATH = "alumnes.json"

def create_JSON():
    if not Path(FILE_PATH).exists():
        with open (FILE_PATH, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)

def read_alumnes():
    create_JSON()
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def get_next_id():
    alumnes = read_alumnes()
    if alumnes:
        max_id = max([alumne["id"] for alumne in alumnes])
        return max_id + 1
    else:
        return 1
    
def add_alumne(data: AlumneCreate):
    alumnes = read_alumnes()
    new_id = get_next_id()
    alumne_data = data.dict()
    alumne_data["id"] = new_id
    alumnes.append(alumne_data)
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(alumnes, f, indent=4)

def get_JSON():
    return read_alumnes()