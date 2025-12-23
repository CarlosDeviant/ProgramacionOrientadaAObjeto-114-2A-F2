from __future__ import annotations

import random
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass
class Lectura:
    sensor_id: str
    tipo: str
    valor_std: float
    unidad_std: str


class Sensor(ABC):
    def __init__(self, sensor_id: str) -> None:
        self._sensor_id = sensor_id.strip()

    @property
    def sensor_id(self) -> str:
        return self._sensor_id

    @property
    @abstractmethod
    def tipo(self) -> str: ...

    @property
    @abstractmethod
    def unidad_std(self) -> str: ...

    @abstractmethod
    def leer(self) -> Tuple[float, str]:
        """Retorna (valor, unidad_origen)"""

    @abstractmethod
    def normalizar(self, valor: float, unidad_origen: str) -> float: ...

    @abstractmethod
    def validar_rango(self, valor_std: float) -> None: ...


class SensorTemperatura(Sensor):
    @property
    def tipo(self) -> str:
        return "temperatura"

    @property
    def unidad_std(self) -> str:
        return "C"

    def leer(self) -> Tuple[float, str]:
        
        if random.random() < 0.5:
            return round(random.uniform(10, 35), 2), "C"
        return round(random.uniform(50, 95), 2), "F"

    def normalizar(self, valor: float, unidad_origen: str) -> float:
        u = unidad_origen.upper().strip()
        if u == "C":
            return float(valor)
        if u == "F":
            return (float(valor) - 32.0) * (5.0 / 9.0)
        raise ValueError("Unidad no soportada para temperatura.")

    def validar_rango(self, valor_std: float) -> None:
        
        if not (-50 <= valor_std <= 80):
            raise ValueError("Temperatura fuera de rango razonable.")


class SensorHumedad(Sensor):
    @property
    def tipo(self) -> str:
        return "humedad"

    @property
    def unidad_std(self) -> str:
        return "%"

    def leer(self) -> Tuple[float, str]:
        return round(random.uniform(-5, 110), 2), "%"  

    def normalizar(self, valor: float, unidad_origen: str) -> float:
        return float(valor)

    def validar_rango(self, valor_std: float) -> None:
        if not (0 <= valor_std <= 100):
            raise ValueError("Humedad fuera de rango (0-100).")


class SensorMovimiento(Sensor):
    @property
    def tipo(self) -> str:
        return "movimiento"

    @property
    def unidad_std(self) -> str:
        return "mov" 

    def leer(self) -> Tuple[float, str]:
        
        return float(1 if random.random() < 0.35 else 0), "bin"

    def normalizar(self, valor: float, unidad_origen: str) -> float:
        return 1.0 if float(valor) >= 1 else 0.0

    def validar_rango(self, valor_std: float) -> None:
        if valor_std not in (0.0, 1.0):
            raise ValueError("Movimiento inválido.")


def crear_lectura(sensor: Sensor) -> Lectura:
    valor, u = sensor.leer()
    valor_std = sensor.normalizar(valor, u)
    sensor.validar_rango(valor_std)
    return Lectura(sensor_id=sensor.sensor_id, tipo=sensor.tipo, valor_std=valor_std, unidad_std=sensor.unidad_std)
