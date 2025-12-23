from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

from .archivo import ArchivoJSON
from .canales import CanalNotificacion, Destino


@dataclass
class ResumenEnvio:
    exitosos: int
    fallos: int
    costo_total: float


class Notificador(ArchivoJSON):
    """Administra destinos y envía mensajes (evita duplicados)."""

    def __init__(self) -> None:
        super().__init__("destinos_ej1.json")
        self._destinos: List[Destino] = []
        self._cargar_destinos()

    def _cargar_destinos(self) -> None:
        raw = self.cargar()
        if not raw:
            return
        try:
            self._destinos = [Destino(**d) for d in raw]
        except Exception:
            self._destinos = []

    def _persistir(self) -> None:
        self.guardar([d.__dict__ for d in self._destinos])

    def registrar(self, canal: CanalNotificacion, destino: str) -> Tuple[bool, str]:
        destino = destino.strip()
        if not canal.validar_destino(destino):
            return False, "Destino inválido para ese canal."

        nuevo = Destino(canal=canal.nombre, destino=destino)
        if nuevo in self._destinos:
            return False, "Destino duplicado (ya existe)."

        self._destinos.append(nuevo)
        self._persistir()
        return True, "Destino registrado."

    def listar(self) -> List[Destino]:
        return list(self._destinos)

    def enviar_a_todos(self, mensaje: str, canales: Dict[str, CanalNotificacion]) -> Tuple[ResumenEnvio, List[str]]:
        if not mensaje.strip():
            return ResumenEnvio(0, 0, 0.0), ["Mensaje vacío (no se envía)."]

        logs: List[str] = []
        exitosos = 0
        fallos = 0
        costo_total = 0.0

        for d in self._destinos:
            canal = canales.get(d.canal)
            if canal is None:
                fallos += 1
                logs.append(f"❌ Canal no disponible: {d.canal} ({d.destino})")
                continue

            ok_msg, err = canal.validar_mensaje(mensaje)
            if not ok_msg:
                fallos += 1
                logs.append(f"❌ Validación mensaje falló en {d.canal}: {err}")
                continue

            enviado = canal.enviar(d.destino, mensaje)
            if enviado:
                exitosos += 1
                c = canal.costo(mensaje)
                costo_total += c
                logs.append(f"✅ Enviado por {d.canal} a {d.destino} (costo ${c:.0f})")
            else:
                fallos += 1
                logs.append(f"❌ Falló envío por {d.canal} a {d.destino}")

        return ResumenEnvio(exitosos, fallos, costo_total), logs
