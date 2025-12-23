from __future__ import annotations

import math
from dataclasses import asdict
from datetime import datetime, time
from typing import Dict, List, Tuple

from .archivo import ArchivoJSON
from .utils import parse_hora_hhmm
from .vehiculos import Auto, Moto, Camion, Vehiculo, Estadia


PUNTA_RANGOS = [
    (time(7, 30), time(9, 30)),
    (time(18, 0), time(21, 0)),
]
RECARGO_PUNTA = 0.20  # 20%


class Estacionamiento(ArchivoJSON):
    def __init__(self) -> None:
        super().__init__("estadias_ej2.json")
        self._estadias: List[Estadia] = []
        self._cargar()

    def _cargar(self) -> None:
        raw = self.cargar()
        if not raw:
            return
        try:
            self._estadias = [Estadia(**x) for x in raw]
        except Exception:
            self._estadias = []

    def _persistir(self) -> None:
        self.guardar([asdict(e) for e in self._estadias])

    @staticmethod
    def crear_vehiculo(tipo: str, patente: str) -> Vehiculo:
        tipo = tipo.lower().strip()
        if tipo == "auto":
            return Auto(patente)
        if tipo == "moto":
            return Moto(patente)
        if tipo == "camion":
            return Camion(patente)
        raise ValueError("Tipo de vehículo no soportado.")

    @staticmethod
    def _es_horario_punta(h: time) -> bool:
        for ini, fin in PUNTA_RANGOS:
            if ini <= h <= fin:
                return True
        return False

    @staticmethod
    def _minutos(entrada: datetime, salida: datetime) -> int:
        delta = salida - entrada
        mins = int(delta.total_seconds() // 60)
        if mins <= 0:
            raise ValueError("Salida debe ser posterior a entrada.")
        return mins

    def calcular_cobro(self, vehiculo: Vehiculo, entrada_hhmm: str, salida_hhmm: str) -> float:
        entrada = parse_hora_hhmm(entrada_hhmm)
        salida = parse_hora_hhmm(salida_hhmm)
        mins = self._minutos(entrada, salida)

        horas_cobrables = math.ceil(mins / 60)  # redondeo hacia arriba
        base = horas_cobrables * vehiculo.tarifa_hora

        # Recargo punta si la HORA DE ENTRADA está en punta (regla simple)
        recargo = base * RECARGO_PUNTA if self._es_horario_punta(entrada.time()) else 0.0
        return float(base + recargo)

    def registrar_estadia(self, patente: str, tipo: str, entrada: str, salida: str) -> Estadia:
        v = self.crear_vehiculo(tipo, patente)
        cobro = self.calcular_cobro(v, entrada, salida)
        e = Estadia(patente=v.patente, tipo=v.tipo, entrada=entrada, salida=salida, cobro=cobro)
        self._estadias.append(e)
        self._persistir()
        return e

    def cargar_prueba_12(self) -> None:
        # Si ya hay datos, no duplicar
        if len(self._estadias) >= 12:
            return
        ejemplos = [
            ("ABCD11", "auto",   "07:40", "08:10"),
            ("EFGH22", "moto",   "10:00", "11:20"),
            ("IJKL33", "camion", "18:05", "19:30"),
            ("MNOP44", "auto",   "12:15", "13:05"),
            ("QRST55", "moto",   "08:20", "09:10"),
            ("UVWX66", "camion", "14:00", "16:40"),
            ("YYZZ77", "auto",   "19:10", "19:50"),
            ("AA111B", "moto",   "06:50", "07:20"),
            ("CC222D", "camion", "09:40", "10:05"),
            ("EE333F", "auto",   "17:50", "18:20"),
            ("GG444H", "moto",   "20:10", "21:30"),
            ("II555J", "camion", "11:00", "12:01"),
        ]
        for patente, tipo, ent, sal in ejemplos:
            try:
                self.registrar_estadia(patente, tipo, ent, sal)
            except Exception:
                # no romper por un ejemplo malo
                pass

    def reporte(self) -> Dict[str, object]:
        total = sum(e.cobro for e in self._estadias)
        top3 = sorted(self._estadias, key=lambda e: e.cobro, reverse=True)[:3]
        conteo: Dict[str, int] = {"auto": 0, "moto": 0, "camion": 0}
        for e in self._estadias:
            if e.tipo in conteo:
                conteo[e.tipo] += 1

        return {
            "total_recaudado": total,
            "top3": top3,
            "conteo": conteo,
            "cantidad_estadias": len(self._estadias),
        }

    def listar(self) -> List[Estadia]:
        return list(self._estadias)
