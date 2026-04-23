# Lista de registros
registros = []

# Set para IDs únicos
ids = set()

def crear_registro(id, nombre):
    from validate import validar_id, validar_nombre

    valido_id, msg_id = validar_id(id, ids)
    if not valido_id:
        return msg_id

    valido_nombre, msg_nombre = validar_nombre(nombre)
    if not valido_nombre:
        return msg_nombre

    registro = {
        "id": id,
        "nombre": nombre
    }

    registros.append(registro)
    ids.add(id)

    return "Registro creado correctamente"

def listar_registros():
    return registros