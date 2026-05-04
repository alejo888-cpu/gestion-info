from typing import List, Dict, Union
from src.validate import validar_id, validar_nombre
from src.file import load_data, save_data

# Tipos para mayor claridad
Registro = Dict[str, str]

# Cargar datos
registros: List[Registro] = load_data()
ids = set(r["id"] for r in registros)


# CREATE
def new_register(record_id: str, nombre: str) -> str:
    """
    Crea un nuevo registro validando ID y nombre.

    Args:
        record_id (str): ID único del registro
        nombre (str): Nombre del usuario

    Returns:
        str: Mensaje de resultado
    """
    valido_id, msg_id = validar_id(record_id, ids)
    if not valido_id:
        return msg_id

    valido_nombre, msg_nombre = validar_nombre(nombre)
    if not valido_nombre:
        return msg_nombre

    registro: Registro = {
        "id": record_id,
        "nombre": nombre
    }

    registros.append(registro)
    ids.add(record_id)
    save_data(registros)

    return "Registro creado correctamente"


# READ (LISTAR)
def list_records() -> Union[str, List[Registro]]:
    """
    Retorna todos los registros almacenados.

    Returns:
        list | str: Lista de registros o mensaje si está vacío
    """
    if not registros:
        return "No hay registros"

    return registros


# SEARCH
def search_record(record_id: str) -> Union[str, Registro]:
    """
    Busca un registro por ID.

    Args:
        record_id (str): ID a buscar

    Returns:
        dict | str: Registro encontrado o mensaje de error
    """
    resultado = [r for r in registros if r["id"] == record_id]

    if not resultado:
        return "Registro no encontrado"

    return resultado[0]


# UPDATE
def update_record(record_id: str, nuevo_nombre: str) -> str:
    """
    Actualiza el nombre de un registro existente.

    Args:
        record_id (str): ID del registro
        nuevo_nombre (str): Nuevo nombre

    Returns:
        str: Resultado de la operación
    """
    for r in registros:
        if r["id"] == record_id:

            valido_nombre, msg = validar_nombre(nuevo_nombre)
            if not valido_nombre:
                return msg

            r["nombre"] = nuevo_nombre
            save_data(registros)
            return "Registro actualizado"

    return "Error: ID no existe"


# DELETE
def delete_record(record_id: str) -> str:
    """
    Elimina un registro por ID.

    Args:
        record_id (str): ID a eliminar

    Returns:
        str: Resultado de la operación
    """
    global registros

    nueva_lista = [r for r in registros if r["id"] != record_id]

    if len(nueva_lista) == len(registros):
        return "Error: ID no existe"

    registros = nueva_lista
    ids.discard(record_id)

    save_data(registros)
    return "Registro eliminado"


def sort_records() -> List[Registro]:
    """
    Ordena los registros por nombre.

    Returns:
        list: Lista ordenada
    """
    return sorted(registros, key=lambda x: x["nombre"])