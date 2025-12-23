from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Tuple


@dataclass
class Comprobante:
    id_venta: str
    medio: str
    monto_base: float
    recargo: float
    monto_final: float
    fecha: str

    def __str__(self) -> str:
        return (
            f"[{self.fecha}] Venta {self.id_venta} | medio={self.medio} | "
            f"base=${self.monto_base:.0f} | recargo=${self.recargo:.0f} | total=${self.monto_final:.0f}"
        )


class MedioPago(ABC):
    @property
    @abstractmethod
    def nombre(self) -> str: ...

    @abstractmethod
    def calcular(self, monto: float, datos: Dict[str, str]) -> Tuple[float, float]:
        """Retorna (monto_final, recargo). Debe validar con los datos entregados."""


class Tarjeta(MedioPago):
    @property
    def nombre(self) -> str:
        return "tarjeta"

    def calcular(self, monto: float, datos: Dict[str, str]) -> Tuple[float, float]:
        
        cupo = float(datos.get("cupo", "0"))
        if cupo < monto:
            raise ValueError("Cupo insuficiente para pagar con tarjeta.")
        recargo = monto * 0.025  
        return monto + recargo, recargo


class Transferencia(MedioPago):
    @property
    def nombre(self) -> str:
        return "transferencia"

    def calcular(self, monto: float, datos: Dict[str, str]) -> Tuple[float, float]:
        
        codigo = datos.get("codigo", "").strip()
        if len(codigo) < 6:
            raise ValueError("Código de confirmación inválido (mín. 6).")
        return monto, 0.0


class BilleteraDigital(MedioPago):
    @property
    def nombre(self) -> str:
        return "billetera"

    def calcular(self, monto: float, datos: Dict[str, str]) -> Tuple[float, float]:
        saldo = float(datos.get("saldo", "0"))
        if saldo < monto:
            raise ValueError("Saldo insuficiente en la billetera.")
        recargo = 200.0  
        return monto + recargo, recargo


def crear_comprobante(id_venta: str, medio: str, base: float, recargo: float, total: float) -> Comprobante:
    return Comprobante(
        id_venta=id_venta,
        medio=medio,
        monto_base=base,
        recargo=recargo,
        monto_final=total,
        fecha=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )
