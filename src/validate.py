from typing import Tuple, Set


def validar_id(record_id: str, ids_existentes: Set[str]) -> Tuple[bool, str]:
    """
    Valida que el ID no esté vacío ni duplicado.

    Args:
        record_id (str): ID a validar
        ids_existentes (set): Conjunto de IDs ya registrados

    Returns:
        tuple: (True, "") si es válido, o (False, mensaje de error)
    """
    if not record_id:
        return False, "El ID no puede estar vacío"

    if record_id in ids_existentes:
        return False, "El ID ya existe"

    return True, ""


def validar_nombre(nombre: str) -> Tuple[bool, str]:
    """
    Valida que el nombre no esté vacío.

    Args:
        nombre (str): Nombre a validar

    Returns:
        tuple: (True, "") si es válido, o (False, mensaje de error)
    """
    if not nombre.strip():
        return False, "El nombre no puede estar vacío"

    return True, ""