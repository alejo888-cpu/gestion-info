from service import *

def menu():
    while True:
        print("--- MENÚ ---")
        print("1. Crear")
        print("2. Listar")
        print("3. Buscar")
        print("4. Actualizar")
        print("5. Eliminar")
        print("6. Salir")

        op = input("Opción: ")

        if op == "1":
            print(new_register(input("ID: "), input("Nombre: ")))

        elif op == "2":
            print(list_records())

        elif op == "3":
            print(search_record(input("ID: ")))

        elif op == "4":
            print(update_record(input("ID: "), input("Nuevo nombre: ")))

        elif op == "5":
            print(delete_record(input("ID: ")))

        elif op == "6":
            break

        else:
            print("Opción inválida")

menu()