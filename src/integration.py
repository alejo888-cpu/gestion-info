import os
from typing import Optional
import pandas as pd
from src.file import load_data


def export_to_csv(
    ordenar_por: Optional[str] = None,
    filtro_nombre: Optional[str] = None
) -> str:
    """
    Exporta los registros a un archivo CSV usando pandas.

    Permite ordenar y filtrar los datos dinámicamente.

    Args:
        ordenar_por (str, opcional): Campo por el cual ordenar (ej: "nombre")
        filtro_nombre (str, opcional): Texto para filtrar nombres

    Returns:
        str: Mensaje con el resultado de la operación
    """
    try:
        data = load_data()

        if not data:
            return "No hay datos para exportar"

        df = pd.DataFrame(data)

        # 🔥 Ordenar (lambda implícito en pandas)
        if ordenar_por:
            df = df.sort_values(by=ordenar_por)

        # 🔥 Filtrar
        if filtro_nombre:
            df = df[df["nombre"].str.contains(filtro_nombre, case=False, na=False)]

        # 🔥 Asegurar carpeta
        ruta = "data/reporte.csv"
        os.makedirs(os.path.dirname(ruta), exist_ok=True)

        df.to_csv(ruta, index=False, encoding="utf-8")

        return f"Reporte generado en {ruta}"

    except Exception as e:
        return f"Error al generar reporte: {e}"