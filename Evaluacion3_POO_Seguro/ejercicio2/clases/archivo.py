from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any


class ArchivoJSON:
    """Clase base para persistir datos en JSON (herencia de 'archivo').

    - Escribe siempre en una ruta controlada por el programa (no acepta rutas del usuario).
    - Maneja errores típicos de lectura/escritura.
    """

    def __init__(self, nombre_archivo: str, carpeta_datos: str = "data") -> None:
        self._base_dir = Path(__file__).resolve().parent.parent / carpeta_datos
        self._base_dir.mkdir(parents=True, exist_ok=True)
        self._ruta = (self._base_dir / nombre_archivo).resolve()

        # Seguridad básica: evitar que la ruta "escape" de la carpeta data
        if self._base_dir not in self._ruta.parents and self._ruta != self._base_dir:
            raise ValueError("Ruta de almacenamiento inválida.")

    def guardar(self, data: Any) -> None:
        try:
            serializable = self._to_json_serializable(data)
            with self._ruta.open("w", encoding="utf-8") as f:
                json.dump(serializable, f, ensure_ascii=False, indent=2)
        except OSError as e:
            raise RuntimeError(f"No se pudo guardar el archivo: {e}") from e

    def cargar(self) -> Any:
        if not self._ruta.exists():
            return None
        try:
            with self._ruta.open("r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            # Archivo corrupto o vacío: no romper el programa completo
            return None
        except OSError as e:
            raise RuntimeError(f"No se pudo leer el archivo: {e}") from e

    @staticmethod
    def _to_json_serializable(obj: Any) -> Any:
        # dataclass -> dict
        if is_dataclass(obj):
            return asdict(obj)
        # list/tuple -> lista serializable
        if isinstance(obj, (list, tuple)):
            return [ArchivoJSON._to_json_serializable(x) for x in obj]
        # dict -> dict serializable
        if isinstance(obj, dict):
            return {str(k): ArchivoJSON._to_json_serializable(v) for k, v in obj.items()}
        # primitivos
        if obj is None or isinstance(obj, (str, int, float, bool)):
            return obj
        # fallback: str
        return str(obj)
