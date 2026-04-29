import pandas as pd
from file import load_data

# 🔥 Uso de **kwargs (requisito obligatorio)
def export_to_csv(**kwargs):
    try:
        data = load_data()

        if not data:
            return "No hay datos para exportar"

        df = pd.DataFrame(data)

        # Aplicar orden dinámico si viene en kwargs
        if "ordenar_por" in kwargs:
            df = df.sort_values(by=kwargs["ordenar_por"])

        # Aplicar filtro si viene en kwargs
        if "filtro_nombre" in kwargs:
            df = df[df["nombre"].str.contains(kwargs["filtro_nombre"], case=False)]

        ruta = "data/reporte.csv"
        df.to_csv(ruta, index=False)

        return f"Reporte generado en {ruta}"

    except Exception as e:
        return f"Error al generar reporte: {e}"