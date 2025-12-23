from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


class Vehiculo(ABC):
    def __init__(self, patente: str) -> None:
        self._patente = patente.strip().upper()

    @property
    def patente(self) -> str:
        return self._patente

    @property
    @abstractmethod
    def tipo(self) -> str: ...

    @property
    @abstractmethod
    def tarifa_hora(self) -> float: ...


class Auto(Vehiculo):
    @property
    def tipo(self) -> str:
        return "auto"

    @property
    def tarifa_hora(self) -> float:
        return 1200.0


class Moto(Vehiculo):
    @property
    def tipo(self) -> str:
        return "moto"

    @property
    def tarifa_hora(self) -> float:
        return 800.0


class Camion(Vehiculo):
    @property
    def tipo(self) -> str:
        return "camion"

    @property
    def tarifa_hora(self) -> float:
        return 2500.0


@dataclass
class Estadia:
    patente: str
    tipo: str
    entrada: str  
    salida: str   
    cobro: float
