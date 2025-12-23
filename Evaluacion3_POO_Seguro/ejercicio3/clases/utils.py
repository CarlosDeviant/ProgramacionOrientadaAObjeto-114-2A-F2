from __future__ import annotations

import re
from datetime import datetime
from typing import Callable


def input_no_vacio(mensaje: str) -> str:
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("❌ No se permite vacío. Intenta nuevamente.")


def input_float_positivo(mensaje: str) -> float:
    while True:
        raw = input(mensaje).strip().replace(",", ".")
        try:
            valor = float(raw)
            if valor > 0:
                return valor
            print("❌ Debe ser mayor que 0.")
        except ValueError:
            print("❌ Ingresa un número válido.")


def input_opcion(mensaje: str, opciones: list[str]) -> str:
    opciones_norm = [o.lower() for o in opciones]
    while True:
        v = input(mensaje).strip().lower()
        if v in opciones_norm:
            return v
        print(f"❌ Opción inválida. Opciones: {', '.join(opciones)}")


def validar_email(email: str) -> bool:
    
    return bool(re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email))


def validar_telefono(telefono: str) -> bool:

    return bool(re.fullmatch(r"\+?\d{8,15}", telefono))


def parse_hora_hhmm(hhmm: str) -> datetime:
    hhmm = hhmm.strip()
    return datetime.strptime(hhmm, "%H:%M")
