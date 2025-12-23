from __future__ import annotations

from clases.estacionamiento import Estacionamiento
from clases.utils import input_no_vacio, input_opcion


def main() -> None:
    est = Estacionamiento()

    while True:
        print("\n=== EJERCICIO 2: Tarificador de estacionamiento ===")
        print("1) Registrar estadía")
        print("2) Cargar prueba (12 estadías)")
        print("3) Ver reporte final")
        print("4) Listar estadías")
        print("0) Salir")
        op = input_opcion("Elige: ", ["1", "2", "3", "4", "0"])

        if op == "1":
            patente = input_no_vacio("Patente: ")
            tipo = input_opcion("Tipo (auto/moto/camion): ", ["auto", "moto", "camion"])
            entrada = input_no_vacio("Hora entrada (HH:MM): ")
            salida = input_no_vacio("Hora salida  (HH:MM): ")
            try:
                e = est.registrar_estadia(patente, tipo, entrada, salida)
                print(f"✅ Cobro: ${e.cobro:.0f} (patente={e.patente}, tipo={e.tipo})")
            except Exception as ex:
                print(f"❌ Error: {ex}")

        elif op == "2":
            est.cargar_prueba_12()
            print("✅ Prueba cargada (si no existía).")

        elif op == "3":
            rep = est.reporte()
            print("\n--- REPORTE ---")
            print(f"Cantidad de estadías: {rep['cantidad_estadias']}")
            print(f"Total recaudado: ${rep['total_recaudado']:.0f}")
            print("\nTop 3 cobros más altos:")
            for i, e in enumerate(rep["top3"], 1):
                print(f"{i}. {e.patente} ({e.tipo}) {e.entrada}-{e.salida} -> ${e.cobro:.0f}")
            print("\nCantidad de vehículos por tipo:")
            for t, c in rep["conteo"].items():
                print(f"- {t}: {c}")

        elif op == "4":
            items = est.listar()
            if not items:
                print("No hay estadías registradas.")
            else:
                for i, e in enumerate(items, 1):
                    print(f"{i}. {e.patente} {e.tipo} {e.entrada}-{e.salida} -> ${e.cobro:.0f}")

        else:
            print("Chao 👋")
            break


if __name__ == "__main__":
    main()
