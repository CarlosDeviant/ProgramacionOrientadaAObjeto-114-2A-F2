import importlib

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
        print(e)

def mostrar_menu():
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

if __name__ == "__main__":
    main()
