import os
import json
from datetime import datetime


METRICAS_FILE = "metricas/metricas.json"


def cargar_metricas():
    os.makedirs("metricas", exist_ok=True)

    if not os.path.exists(METRICAS_FILE):
        return []

    try:
        with open(METRICAS_FILE, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except:
        return []


def guardar_metrica(
    pregunta,
    herramienta,
    latencia,
    estado,
    largo_respuesta,
    error=None
):
    metricas = cargar_metricas()

    nueva_metrica = {
        "fecha": str(datetime.now()),
        "pregunta": pregunta,
        "herramienta": herramienta,
        "latencia": latencia,
        "estado": estado,
        "largo_respuesta": largo_respuesta,
        "error": error
    }

    metricas.append(nueva_metrica)

    with open(METRICAS_FILE, "w", encoding="utf-8") as archivo:
        json.dump(metricas, archivo, ensure_ascii=False, indent=4)