import json
from pathlib import Path
from pydantic import BaseModel
from typing import Optional

class Data(BaseModel):
    dia: Optional[int] = None
    mes: Optional[int] = None
    any: Optional[int] = None

class Alumne(BaseModel):
    id: int
    nom: str = ""
    cognom: str = ""
    data: Data
    email: str = ""
    feina: bool = False
    curs: str = ""

FILE_PATH = "alumnes.json"

def create_JSON():
    if not Path(FILE_PATH).exists():
        with open (FILE_PATH, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)

def get_next_id():
    alumnes = read_alumnes()  # Get current list of alumnes
    if alumnes:
        # Find the highest id and return the next one
        max_id = max([alumne["id"] for alumne in alumnes])
        return max_id + 1
    else:
        return 1

def get_JSON():
    create_JSON()
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def add_alumne(Alumne: dict):
    data = get_JSON()
    data.append(Alumne)
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)