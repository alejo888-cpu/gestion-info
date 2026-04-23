from service import crear_registro, listar_registros

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Crear registro")
        print("2. Listar registros")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese ID: ")
            nombre = input("Ingrese nombre: ")

            resultado = crear_registro(id, nombre)
            print(resultado)

        elif opcion == "2":
            registros = listar_registros()
            print("\n--- REGISTROS ---")
            for r in registros:
                print(r)

        elif opcion == "3":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")

menu()