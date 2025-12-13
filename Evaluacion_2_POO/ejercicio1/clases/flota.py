
class Vehiculo:
    def __init__(self, patente, marca, modelo, anio):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def calcular_consumo(self, km):
        return 0  

    def mostrar_info(self):
        return f"{self.marca} {self.modelo} ({self.anio}) - Patente: {self.patente}"


class Automovil(Vehiculo):
    def calcular_consumo(self, km):
        
        litros = km / 12
        return round(litros, 2)

class Motocicleta(Vehiculo):
    def calcular_consumo(self, km):
        
        litros = km / 25
        return round(litros, 2)

class Camion(Vehiculo):
    def calcular_consumo(self, km):
        
        litros = km / 4
        return round(litros, 2)


class Flota:
    def __init__(self):
        self.lista_vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        
        for v in self.lista_vehiculos:
            if v.patente == vehiculo.patente:
                print("Error: Ya existe esa patente.")
                return
        self.lista_vehiculos.append(vehiculo)

    def mostrar_todos(self):
        print("\n--- LISTA DE FLOTA ---")
        for v in self.lista_vehiculos:
            print(v.mostrar_info())