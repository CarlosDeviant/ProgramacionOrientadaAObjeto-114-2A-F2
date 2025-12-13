from clases.flota import Flota, Automovil, Motocicleta, Camion


def main():
    mi_flota = Flota()

    
    auto = Automovil("AA11", "Toyota", "Yaris", 2020)
    moto = Motocicleta("BB22", "Honda", "CBR", 2022)
    camion = Camion("CC33", "Volvo", "FMX", 2019)

    
    mi_flota.agregar_vehiculo(auto)
    mi_flota.agregar_vehiculo(moto)
    mi_flota.agregar_vehiculo(camion)

    
    mi_flota.mostrar_todos()

    
    km_viaje = 150
    print(f"\n--- CONSUMO PARA {km_viaje} KM ---")
    print(f"Auto: {auto.calcular_consumo(km_viaje)} litros")
    print(f"Moto: {moto.calcular_consumo(km_viaje)} litros")
    print(f"Camión: {camion.calcular_consumo(km_viaje)} litros")

if __name__ == "__main__":
    main()