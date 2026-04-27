from colorama import Fore, Style, Back, init
from service import *

init(autoreset=True)

def mostrar_menu():
    print(Fore.BLUE + "\n==============================")
    print(Back.CYAN + "      SISTEMA DE REGISTROS     ")
    print(Fore.BLUE + "==============================")
    print("1. Crear registro")
    print("2. Listar registros")
    print("3. Buscar registro")
    print("4. Actualizar registro")
    print("5. Eliminar registro")
    print("6. Salir")


def ejecutar_menu():
    while True:
        mostrar_menu()

        try:
            opcion = int(input(Fore.YELLOW + "Seleccione una opción: "))

            if opcion == 1:
                id = input("Ingrese ID: ")
                nombre = input("Ingrese nombre: ")
                print(Fore.GREEN + new_register(id, nombre))

            elif opcion == 2:
                datos = list_records()
                print(Fore.GREEN + "\n--- REGISTROS ---")
                if isinstance(datos, str):
                    print(datos)
                else:
                    for r in datos:
                        print(f"ID: {r['id']} | Nombre: {r['nombre']}")

            elif opcion == 3:
                id = input("Ingrese ID a buscar: ")
                resultado = search_record(id)
                print(Fore.GREEN + str(resultado))

            elif opcion == 4:
                id = input("Ingrese ID a actualizar: ")
                nuevo = input("Nuevo nombre: ")
                print(Fore.GREEN + update_record(id, nuevo))

            elif opcion == 5:
                id = input("Ingrese ID a eliminar: ")
                print(Fore.RED + delete_record(id))

            elif opcion == 6:
                print(Fore.CYAN + "Saliendo del sistema...")
                break

            else:
                print(Fore.RED + "Opción inválida")

        except ValueError:
            print(Fore.RED + "Error: Debe ingresar un número válido")