import json
import os

RUTA_ARCHIVO = "data/records.json"

def load_data():
    try:
        if not os.path.exists(RUTA_ARCHIVO):
            return []

        with open(RUTA_ARCHIVO, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("Error: El archivo está dañado.")
        return []

    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return []

def save_data(data):
    try:
        with open(RUTA_ARCHIVO, "w") as file:
            json.dump(data, file, indent=4)

    except Exception as e:
        print(f"Error al guardar el archivo: {e}")