from __future__ import annotations

from clases.sistema_iot import SistemaIoT
from clases.utils import input_no_vacio, input_opcion


def main() -> None:
    s = SistemaIoT()

    while True:
        print("\n=== EJERCICIO 4: Sensores y lecturas normalizadas ===")
        print("1) Registrar sensor")
        print("2) Cargar prueba (3 sensores)")
        print("3) Generar lecturas (simuladas)")
        print("4) Ver reporte consolidado")
        print("0) Salir")
        op = input_opcion("Elige: ", ["1", "2", "3", "4", "0"])

        if op == "1":
            sid = input_no_vacio("ID sensor: ")
            tipo = input_opcion("Tipo (temperatura/humedad/movimiento): ", ["temperatura", "humedad", "movimiento"])
            try:
                s.registrar_sensor(sid, tipo)
                print("✅ Sensor registrado.")
            except Exception as ex:
                print(f"❌ Error: {ex}")

        elif op == "2":
            try:
                s.cargar_prueba()
                print("✅ Sensores de prueba cargados (si no existían).")
            except Exception as ex:
                print(f"❌ Error: {ex}")

        elif op == "3":
            ok, fail = s.generar_lecturas()
            print(f"✅ Lecturas generadas: {ok} | fallos por validación/rango: {fail}")

        elif op == "4":
            rep = s.reporte()
            print("\n--- REPORTE CONSOLIDADO ---")
            print(f"Sensores registrados: {len(rep['sensores_registrados'])}")
            for sid, t in rep["sensores_registrados"].items():
                print(f"- {sid}: {t}")
            print(f"Lecturas totales: {rep['lecturas_total']}")

            print("\nEstadísticas (min / max / promedio):")
            if not rep["stats"]:
                print("(sin estadísticas aún; genera lecturas primero)")
            else:
                for tipo, st in rep["stats"].items():
                    print(f"* {tipo}: n={int(st['n'])} | min={st['min']:.2f} | max={st['max']:.2f} | prom={st['prom']:.2f}")

            print("\nÚltimas lecturas (máx 10):")
            for l in rep["ultimas_lecturas"]:
                print(f"- {l.sensor_id} ({l.tipo}) = {l.valor_std:.2f} {l.unidad_std}")

        else:
            print("Chao 👋")
            break


if __name__ == "__main__":
    main()
