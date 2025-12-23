from __future__ import annotations

from dataclasses import asdict
from typing import Dict, List, Tuple

from .archivo import ArchivoJSON
from .pagos import Comprobante, MedioPago, crear_comprobante


class Tienda(ArchivoJSON):
    def __init__(self) -> None:
        super().__init__("ventas_ej3.json")
        self._comprobantes: List[Comprobante] = []
        self._cargar()

    def _cargar(self) -> None:
        raw = self.cargar()
        if not raw:
            return
        try:
            self._comprobantes = [Comprobante(**x) for x in raw]
        except Exception:
            self._comprobantes = []

    def _persistir(self) -> None:
        self.guardar([asdict(c) for c in self._comprobantes])

    def pagar(self, id_venta: str, monto: float, medio: MedioPago, datos: Dict[str, str]) -> Comprobante:
        if not id_venta.strip():
            raise ValueError("id_venta no puede ser vacío.")
        if monto <= 0:
            raise ValueError("monto debe ser > 0.")

        total, recargo = medio.calcular(monto, datos)
        comp = crear_comprobante(id_venta=id_venta.strip(), medio=medio.nombre, base=monto, recargo=recargo, total=total)

        self._comprobantes.append(comp)
        self._persistir()
        return comp

    def reporte(self) -> Dict[str, object]:
        total_recaudado = sum(c.monto_final for c in self._comprobantes)
        total_recargos = sum(c.recargo for c in self._comprobantes)
        return {
            "total_recaudado": total_recaudado,
            "total_recargos": total_recargos,
            "comprobantes": list(self._comprobantes),
            "cantidad": len(self._comprobantes),
        }
