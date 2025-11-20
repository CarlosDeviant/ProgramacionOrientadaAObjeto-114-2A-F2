import sys
import os
import importlib
from os import system

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

CANTIDAD_EJERCICIOS = 7

def ejecutar_ejercicio(numero):
    nombre_modulo = f"Ejercicio{numero}"
    try:
        modulo = importlib.import_module(nombre_modulo)
        if hasattr(modulo, "main"):
            modulo.main()
        elif hasattr(modulo, "run"):
            modulo.run()
    except Exception as e:
        print(f"Error: {e}")

def mostrar_menu():
    system("cls")
    print("=== Evaluación 1 - Carlos_Rojas ===")
    for i in range(1, CANTIDAD_EJERCICIOS + 1):
        print(f"{i}. Ejercicio{i}.py")
    print("0. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingresa una opción: ").strip()
        if opcion == "0":
            break
        if opcion.isdigit():
            numero = int(opcion)
            if 1 <= numero <= CANTIDAD_EJERCICIOS:
                ejecutar_ejercicio(numero)
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
