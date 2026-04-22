print("Sistema Listo")

# Crear un algoritmo que lea 3 numero, los alamcene en una lista y los ordene de mayor a menor.
# Manejo de funciones, listas, menu intereactivo y manejo de errores.

# Instalar colorama: pip install colorama
from colorama import Fore, Style, Back, init
init(autoreset=True)

print(Fore.BLUE + "==============================================================")
print(Back.CYAN + "================ Manejo De Listas y Errores ==================")
print(Style.DIM + "========================== By CAJX ===========================")
print(Fore.BLUE + "==============================================================")

try:
    # Algoritmo a ejecutar
    print("Ingrese 3 numeros para ordenarlos de mayor a menor")

except ValueError: #TypeError, IndexError, ValueError
    print("Error: ingrese un numero valido")