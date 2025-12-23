from __future__ import annotations

from clases.canales import EmailCanal, SMSCanal, AppTokenCanal
from clases.notificador import Notificador
from clases.utils import input_no_vacio, input_opcion


def menu() -> None:
    notificador = Notificador()
    canales = {
        "email": EmailCanal(),
        "sms": SMSCanal(),
        "app": AppTokenCanal(),
    }

    while True:
        print("\n=== EJERCICIO 1: Notificaciones multicanal ===")
        print("1) Registrar destino")
        print("2) Listar destinos")
        print("3) Enviar mensaje a todos")
        print("4) Ejecutar prueba (registra y envía 2 mensajes)")
        print("0) Salir")
        op = input_opcion("Elige: ", ["1", "2", "3", "4", "0"])

        if op == "1":
            canal = input_opcion("Canal (email/sms/app): ", ["email", "sms", "app"])
            destino = input_no_vacio("Destino: ")
            ok, msg = notificador.registrar(canales[canal], destino)
            print(("✅ " if ok else "❌ ") + msg)

        elif op == "2":
            destinos = notificador.listar()
            if not destinos:
                print("No hay destinos registrados.")
            else:
                for i, d in enumerate(destinos, 1):
                    print(f"{i}. {d.canal}: {d.destino}")

        elif op == "3":
            mensaje = input_no_vacio("Mensaje a enviar: ")
            resumen, logs = notificador.enviar_a_todos(mensaje, canales)
            print("\n--- Detalle ---")
            for l in logs:
                print(l)
            print("\n--- Resumen ---")
            print(f"Exitosos: {resumen.exitosos}")
            print(f"Fallos:   {resumen.fallos}")
            print(f"Costo total: ${resumen.costo_total:.0f}")

        elif op == "4":
            # Prueba pedida: registrar varios destinos y simular envío de 2 mensajes
            print("Cargando destinos de prueba...")
            pruebas = [
                ("email", "cliente1@correo.cl"),
                ("email", "fail@correo.cl"),     # simula fallo
                ("sms", "+56912345678"),
                ("sms", "+56900000000"),        # simula fallo por contener 0
                ("app", "token_abcdef12345"),
                ("app", "invalidtoken"),        # simula fallo
            ]
            for c, d in pruebas:
                notificador.registrar(canales[c], d)

            for msg in ["Alerta: mantención programada 21:00", "Promo: 20% descuento hoy"]:
                print(f"\nEnviando: {msg}")
                resumen, logs = notificador.enviar_a_todos(msg, canales)
                for l in logs:
                    print(l)
                print(f"Resumen -> exitosos={resumen.exitosos}, fallos={resumen.fallos}, costo=${resumen.costo_total:.0f}")

        else:
            print("Chao 👋")
            break


if __name__ == "__main__":
    menu()
