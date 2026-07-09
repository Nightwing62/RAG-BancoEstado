import os
from datetime import datetime


LOG_FILE = "logs/agente.log"


def registrar_log(
    pregunta,
    respuesta,
    herramienta,
    latencia,
    estado,
    error=None
):
    os.makedirs("logs", exist_ok=True)

    with open(LOG_FILE, "a", encoding="utf-8") as archivo:
        archivo.write("\n" + "=" * 60 + "\n")
        archivo.write(f"Fecha: {datetime.now()}\n")
        archivo.write(f"Pregunta: {pregunta}\n")
        archivo.write(f"Herramienta utilizada: {herramienta}\n")
        archivo.write(f"Latencia: {latencia:.2f} segundos\n")
        archivo.write(f"Estado: {estado}\n")

        if error:
            archivo.write(f"Error: {error}\n")

        archivo.write(f"Respuesta: {respuesta}\n")