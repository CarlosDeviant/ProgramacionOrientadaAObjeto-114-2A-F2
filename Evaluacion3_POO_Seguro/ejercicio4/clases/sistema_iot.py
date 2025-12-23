from __future__ import annotations

from dataclasses import asdict
from statistics import mean
from typing import Dict, List, Tuple

from .archivo import ArchivoJSON
from .sensores import Sensor, SensorTemperatura, SensorHumedad, SensorMovimiento, Lectura, crear_lectura


class SistemaIoT(ArchivoJSON):
    def __init__(self) -> None:
        super().__init__("iot_ej4.json")
        self._sensores: Dict[str, str] = {}  # id -> tipo
        self._lecturas: List[Lectura] = []
        self._cargar()

    def _cargar(self) -> None:
        raw = self.cargar()
        if not raw:
            return
        try:
            self._sensores = dict(raw.get("sensores", {}))
            self._lecturas = [Lectura(**x) for x in raw.get("lecturas", [])]
        except Exception:
            self._sensores = {}
            self._lecturas = []

    def _persistir(self) -> None:
        self.guardar({
            "sensores": self._sensores,
            "lecturas": [asdict(l) for l in self._lecturas],
        })

    def registrar_sensor(self, sensor_id: str, tipo: str) -> None:
        sensor_id = sensor_id.strip()
        tipo = tipo.strip().lower()
        if not sensor_id:
            raise ValueError("sensor_id vacío.")
        if tipo not in ("temperatura", "humedad", "movimiento"):
            raise ValueError("Tipo no soportado.")
        if sensor_id in self._sensores:
            raise ValueError("Sensor duplicado (mismo id).")
        self._sensores[sensor_id] = tipo
        self._persistir()

    def _instanciar(self, sensor_id: str, tipo: str) -> Sensor:
        if tipo == "temperatura":
            return SensorTemperatura(sensor_id)
        if tipo == "humedad":
            return SensorHumedad(sensor_id)
        return SensorMovimiento(sensor_id)

    def generar_lecturas(self) -> Tuple[int, int]:
        ok = 0
        fallos = 0
        for sid, tipo in self._sensores.items():
            sensor = self._instanciar(sid, tipo)
            try:
                lectura = crear_lectura(sensor)
                self._lecturas.append(lectura)
                ok += 1
            except Exception:
                fallos += 1
        self._persistir()
        return ok, fallos

    def reporte(self) -> Dict[str, object]:
        por_tipo: Dict[str, List[Lectura]] = {"temperatura": [], "humedad": [], "movimiento": []}
        for l in self._lecturas:
            if l.tipo in por_tipo:
                por_tipo[l.tipo].append(l)

        stats: Dict[str, Dict[str, float]] = {}
        for tipo, lects in por_tipo.items():
            if not lects:
                continue
            valores = [l.valor_std for l in lects]
            # movimiento: promedio = proporción de detección
            stats[tipo] = {
                "min": min(valores),
                "max": max(valores),
                "prom": mean(valores),
                "n": len(valores),
            }

        return {
            "sensores_registrados": dict(self._sensores),
            "lecturas_total": len(self._lecturas),
            "stats": stats,
            "ultimas_lecturas": self._lecturas[-10:],
        }

    def cargar_prueba(self) -> None:
        if len(self._sensores) >= 3:
            return
        self.registrar_sensor("T-01", "temperatura")
        self.registrar_sensor("H-01", "humedad")
        self.registrar_sensor("M-01", "movimiento")
