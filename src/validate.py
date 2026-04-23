def validar_id(id, ids_existentes):
    if not id:
        return False, "El ID no puede estar vacío"
    if id in ids_existentes:
        return False, "El ID ya existe"
    return True, ""

def validar_nombre(nombre):
    if not nombre.strip():
        return False, "El nombre no puede estar vacío"
    return True, ""