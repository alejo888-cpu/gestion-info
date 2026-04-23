from validate import validar_id, validar_nombre
from file import load_data, save_data

# Cargar datos al iniciar
registros = load_data()

# Crear set de IDs basado en los datos existentes
ids = set(r["id"] for r in registros)

def crear_registro(id, nombre):
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

    save_data(registros)  # 👈 Guardar automáticamente

    return "Registro guardado en archivo correctamente"

def listar_registros():
    return registros