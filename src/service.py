from validate import validar_id, validar_nombre
from file import load_data, save_data

# Cargar datos
registros = load_data()
ids = set(r["id"] for r in registros)

# 🟢 CREATE
def new_register(id, nombre):
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
    save_data(registros)

    return "Registro creado correctamente"


# 🔵 READ (LISTAR)
def list_records():
    if not registros:
        return "No hay registros"

    return registros


# 🔍 SEARCH (con list comprehension)
def search_record(id):
    resultado = [r for r in registros if r["id"] == id]

    if not resultado:
        return "Registro no encontrado"

    return resultado[0]


# 🟡 UPDATE
def update_record(id, nuevo_nombre):
    for r in registros:
        if r["id"] == id:

            valido_nombre, msg = validar_nombre(nuevo_nombre)
            if not valido_nombre:
                return msg

            r["nombre"] = nuevo_nombre
            save_data(registros)
            return "Registro actualizado"

    return "Error: ID no existe"


# 🔴 DELETE
def delete_record(id):
    global registros

    nueva_lista = [r for r in registros if r["id"] != id]

    if len(nueva_lista) == len(registros):
        return "Error: ID no existe"

    registros = nueva_lista
    ids.discard(id)

    save_data(registros)
    return "Registro eliminado"


# ⚡ EXTRA (lambda para ordenar)
def sort_records():
    return sorted(registros, key=lambda x: x["nombre"])