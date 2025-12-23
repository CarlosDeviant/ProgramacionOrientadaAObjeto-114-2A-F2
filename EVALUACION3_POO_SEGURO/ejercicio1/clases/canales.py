from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Tuple

from .utils import validar_email, validar_telefono


class CanalNotificacion(ABC):
    """Canal base (polimorfismo): cada canal valida, cobra y envía distinto."""

    @property
    @abstractmethod
    def nombre(self) -> str: ...

    @abstractmethod
    def validar_destino(self, destino: str) -> bool: ...

    @abstractmethod
    def validar_mensaje(self, mensaje: str) -> Tuple[bool, str]: ...

    @abstractmethod
    def costo(self, mensaje: str) -> float: ...

    @abstractmethod
    def enviar(self, destino: str, mensaje: str) -> bool: ...


@dataclass(frozen=True)
class Destino:
    canal: str
    destino: str


class EmailCanal(CanalNotificacion):
    @property
    def nombre(self) -> str:
        return "email"

    def validar_destino(self, destino: str) -> bool:
        return validar_email(destino)

    def validar_mensaje(self, mensaje: str) -> Tuple[bool, str]:
        if not mensaje.strip():
            return False, "Mensaje vacío"
        if len(mensaje) > 2000:
            return False, "Email supera largo máximo (2000)"
        return True, ""

    def costo(self, mensaje: str) -> float:
        
        return 5.0

    def enviar(self, destino: str, mensaje: str) -> bool:
        
        return "fail" not in destino.lower()


class SMSCanal(CanalNotificacion):
    @property
    def nombre(self) -> str:
        return "sms"

    def validar_destino(self, destino: str) -> bool:
        return validar_telefono(destino)

    def validar_mensaje(self, mensaje: str) -> Tuple[bool, str]:
        if not mensaje.strip():
            return False, "Mensaje vacío"
        if len(mensaje) > 160:
            return False, "SMS supera 160 caracteres"
        return True, ""

    def costo(self, mensaje: str) -> float:
        
        return 20.0

    def enviar(self, destino: str, mensaje: str) -> bool:
        return "0" not in destino  


class AppTokenCanal(CanalNotificacion):
    @property
    def nombre(self) -> str:
        return "app"

    def validar_destino(self, destino: str) -> bool:
        
        return len(destino.strip()) >= 10

    def validar_mensaje(self, mensaje: str) -> Tuple[bool, str]:
        if not mensaje.strip():
            return False, "Mensaje vacío"
        if len(mensaje) > 500:
            return False, "App supera 500 caracteres"
        return True, ""

    def costo(self, mensaje: str) -> float:
        
        return 2.0

    def enviar(self, destino: str, mensaje: str) -> bool:
        return destino.strip().lower() != "invalidtoken"
