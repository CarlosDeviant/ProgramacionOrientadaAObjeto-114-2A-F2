from __future__ import annotations

from clases.pagos import Tarjeta, Transferencia, BilleteraDigital
from clases.tienda import Tienda
from clases.utils import input_no_vacio, input_float_positivo, input_opcion


def main() -> None:
    tienda = Tienda()
    medios = {
        "tarjeta": Tarjeta(),
        "transferencia": Transferencia(),
        "billetera": BilleteraDigital(),
    }

    while True:
        print("\n=== EJERCICIO 3: Pagos en una tienda (múltiples medios) ===")
        print("1) Registrar venta + pagar")
        print("2) Ver reporte final")
        print("0) Salir")
        op = input_opcion("Elige: ", ["1", "2", "0"])

        if op == "1":
            id_venta = input_no_vacio("ID venta: ")
            monto = input_float_positivo("Monto: ")
            medio = input_opcion("Medio (tarjeta/transferencia/billetera): ", ["tarjeta", "transferencia", "billetera"])
            datos = {}

            #
            try:
                if medio == "tarjeta":
                    cupo = input_float_positivo("Cupo disponible (simulado): ")
                    datos["cupo"] = str(cupo)
                elif medio == "transferencia":
                    datos["codigo"] = input_no_vacio("Código confirmación (mín. 6): ")
                else:
                    saldo = input_float_positivo("Saldo disponible (simulado): ")
                    datos["saldo"] = str(saldo)

                comp = tienda.pagar(id_venta, monto, medios[medio], datos)
                print("\n✅ Comprobante generado:")
                print(comp)

            except Exception as ex:
                print(f"❌ No se pudo procesar el pago: {ex}")

        elif op == "2":
            rep = tienda.reporte()
            print("\n--- REPORTE ---")
            print(f"Cantidad de ventas: {rep['cantidad']}")
            print(f"Total recaudado: ${rep['total_recaudado']:.0f}")
            print(f"Total de recargos: ${rep['total_recargos']:.0f}")
            print("\nComprobantes:")
            if not rep["comprobantes"]:
                print("(sin comprobantes)")
            else:
                for c in rep["comprobantes"]:
                    print("-", c)

        else:
            print("Chao 👋")
            break


if __name__ == "__main__":
    main()
