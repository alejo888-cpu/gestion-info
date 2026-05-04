import json
import os
from typing import List, Dict

# Tipo de dato
Registro = Dict[str, str]

RUTA_ARCHIVO = "data/records.json"


def load_data() -> List[Registro]:
    """
    Carga los registros desde el archivo JSON.

    Returns:
        list: Lista de registros. Si no existe o hay error, retorna lista vacía.
    """
    try:
        if not os.path.exists(RUTA_ARCHIVO):
            return []

        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("Error: El archivo está dañado.")
        return []

    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return []


def save_data(data: List[Registro]) -> None:
    """
    Guarda los registros en el archivo JSON.

    Args:
        data (list): Lista de registros a guardar
    """
    try:
        # 🔥 Asegura que la carpeta exista
        os.makedirs(os.path.dirname(RUTA_ARCHIVO), exist_ok=True)

        with open(RUTA_ARCHIVO, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    except Exception as e:
        print(f"Error al guardar el archivo: {e}")