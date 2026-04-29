from colorama import Fore, Style, Back, init
from service import *
from integration import export_to_csv

init(autoreset=True)

def mostrar_menu():
    print(Fore.BLUE + "==============================")
    print(Back.CYAN + "     SISTEMA DE REGISTROS     ")
    print(Fore.BLUE + "==============================")
    print("1. Crear registro")
    print("2. Listar registros")
    print("3. Buscar registro")
    print("4. Actualizar registro")
    print("5. Eliminar registro")
    print("6. Salir")
    print("7. Exportar reporte CSV")

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

            elif opcion == 7:
                print("1. Exportar normal")
                print("2. Ordenar por nombre")
                print("3. Filtrar por nombre")

                sub = input("Seleccione: ")

                if sub == "1":
                    print(export_to_csv())

                elif sub == "2":
                    print(export_to_csv(ordenar_por="nombre"))

                elif sub == "3":
                    texto = input("Ingrese nombre a filtrar: ")
                    print(export_to_csv(filtro_nombre=texto))

                else:
                    print("Opción inválida")

            else:
                print(Fore.RED + "Opción inválida")

        except ValueError:
            print(Fore.RED + "Error: Debe ingresar un número válido")

if __name__ == "__main__":
    ejecutar_menu()