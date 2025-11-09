from os import system
system("cls")

class Sensor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mediciones = []

    def registrar_medicion(self, valor):
        self.mediciones.append(valor)
        print(f"Medición {valor} registrada correctamente.")

    def calcular_promedio(self):
        if not self.mediciones:
            return 0
        return sum(self.mediciones) / len(self.mediciones)

    def obtener_maximo(self):
        if not self.mediciones:
            return None
        return max(self.mediciones)

    def obtener_minimo(self):
        if not self.mediciones:
            return None
        return min(self.mediciones)

    def mostrar_resumen(self):
        if not self.mediciones:
            print(f"Sensor: {self.nombre}\nNo hay mediciones registradas.")
        else:
            print(f"Sensor: {self.nombre}")
            print(f"Promedio: {self.calcular_promedio():.2f}")
            print(f"Valor máximo: {self.obtener_maximo()}")
            print(f"Valor mínimo: {self.obtener_minimo()}")

def menu():
    system("cls")
    nombre_sensor = input("Ingrese el nombre del sensor: ")
    sensor = Sensor(nombre_sensor)

    while True:
        system("cls")
        print(f"====== SISTEMA DE MEDICIONES - SENSOR: {sensor.nombre} ======")
        print("1. Registrar nueva medición")
        print("2. Consultar promedio de mediciones")
        print("3. Consultar valor máximo")
        print("4. Consultar valor mínimo")
        print("5. Mostrar resumen del sensor")
        print("0. Salir")
        opcion = input("\nSeleccione una opción: ")

        system("cls")

        if opcion == "1":
            try:
                valor = float(input("Ingrese el valor de la medición: "))
                sensor.registrar_medicion(valor)
            except ValueError:
                print("Debe ingresar un valor numérico válido.")
        elif opcion == "2":
            promedio = sensor.calcular_promedio()
            if promedio == 0:
                print("No hay mediciones registradas.")
            else:
                print(f"Promedio de mediciones: {promedio:.2f}")
        elif opcion == "3":
            maximo = sensor.obtener_maximo()
            if maximo is None:
                print("No hay mediciones registradas.")
            else:
                print(f"Valor máximo registrado: {maximo}")
        elif opcion == "4":
            minimo = sensor.obtener_minimo()
            if minimo is None:
                print("No hay mediciones registradas.")
            else:
                print(f"Valor mínimo registrado: {minimo}")
        elif opcion == "5":
            sensor.mostrar_resumen()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

        input("\nPresione ENTER para continuar...")

if __name__ == "__main__":
    menu()
