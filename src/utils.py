import os
import json
from datetime import datetime


# ==================================================
# CARPETAS DEL PROYECTO
# ==================================================

def crear_carpetas_base():
    """
    Crea las carpetas necesarias para el funcionamiento
    del agente y la observabilidad.
    """

    carpetas = [
        "memoria",
        "reportes",
        "logs",
        "metricas",
        "db"
    ]

    for carpeta in carpetas:
        os.makedirs(carpeta, exist_ok=True)


# ==================================================
# MANEJO DE ARCHIVOS JSON
# ==================================================

def cargar_json(ruta_archivo, valor_defecto=None):
    """
    Carga un archivo JSON.
    Si el archivo no existe o tiene error, retorna un valor por defecto.
    """

    if valor_defecto is None:
        valor_defecto = []

    try:
        if not os.path.exists(ruta_archivo):
            return valor_defecto

        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    except Exception:
        return valor_defecto


def guardar_json(ruta_archivo, datos):
    """
    Guarda datos en un archivo JSON.
    """

    carpeta = os.path.dirname(ruta_archivo)

    if carpeta:
        os.makedirs(carpeta, exist_ok=True)

    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        json.dump(
            datos,
            archivo,
            ensure_ascii=False,
            indent=4
        )


# ==================================================
# FECHAS Y NOMBRES DE ARCHIVOS
# ==================================================

def obtener_fecha_actual():
    """
    Retorna la fecha actual como texto.
    """

    return str(datetime.now())


def obtener_timestamp():
    """
    Retorna fecha y hora en formato compacto para nombres de archivo.
    """

    return datetime.now().strftime("%Y%m%d_%H%M%S")


def generar_nombre_reporte():
    """
    Genera un nombre único para reportes.
    """

    return f"reportes/reporte_{obtener_timestamp()}.txt"


# ==================================================
# LIMPIEZA DE RESPUESTAS
# ==================================================

def extraer_texto(contenido):
    """
    Limpia respuestas del modelo.

    Evita que aparezca una salida como:
    [{'type': 'text', 'text': 'respuesta'}]
    """

    if isinstance(contenido, list):

        texto_final = ""

        for item in contenido:

            if isinstance(item, dict) and item.get("type") == "text":
                texto_final += item.get("text", "")

        return texto_final.strip()

    return str(contenido).strip()


def limitar_texto(texto, limite=1000):
    """
    Limita la cantidad de caracteres de un texto.
    Útil para logs o dashboards.
    """

    texto = str(texto)

    if len(texto) <= limite:
        return texto

    return texto[:limite] + "..."


# ==================================================
# VALIDACIÓN DE ENTRADAS
# ==================================================

def validar_pregunta(pregunta):
    """
    Valida la entrada del usuario antes de enviarla al agente.
    Esto ayuda al uso responsable del sistema.
    """

    if not pregunta or not pregunta.strip():
        return False, "La consulta no puede estar vacía."

    if len(pregunta) > 1000:
        return False, "La consulta es demasiado extensa."

    palabras_bloqueadas = [
        "contraseña",
        "password",
        "clave secreta",
        "api key",
        "token privado"
    ]

    pregunta_minuscula = pregunta.lower()

    for palabra in palabras_bloqueadas:
        if palabra in pregunta_minuscula:
            return (
                False,
                "La consulta contiene información sensible. "
                "No se recomienda ingresar claves, tokens o contraseñas."
            )

    return True, "Consulta válida."


# ==================================================
# CLASIFICACIÓN DE INTENCIÓN
# ==================================================

def clasificar_intencion(pregunta):
    """
    Clasifica la intención del usuario.
    Sirve como apoyo para métricas de observabilidad.
    """

    pregunta = pregunta.lower()

    if any(palabra in pregunta for palabra in [
        "reporte",
        "informe",
        "documento ejecutivo"
    ]):
        return "reporte"

    if any(palabra in pregunta for palabra in [
        "analiza",
        "analizar",
        "riesgo",
        "recomendación",
        "recomendaciones",
        "caso"
    ]):
        return "analisis"

    if any(palabra in pregunta for palabra in [
        "resume",
        "resumen",
        "resúmelo",
        "sintetiza"
    ]):
        return "resumen"

    if any(palabra in pregunta for palabra in [
        "requisitos",
        "normativa",
        "política",
        "plazo",
        "tasa",
        "crédito",
        "fogape",
        "producto"
    ]):
        return "consulta"

    return "general"


def herramienta_esperada(intencion):
    """
    Relaciona una intención con la herramienta esperada.
    Esto puede usarse para medir precisión de selección.
    """

    mapa = {
        "consulta": "buscar_normativas_banco",
        "reporte": "generar_reporte",
        "analisis": "analizar_solicitud",
        "resumen": "resumir_documento",
        "general": "agente_general"
    }

    return mapa.get(intencion, "agente_general")


# ==================================================
# MÉTRICA SIMPLE DE PRECISIÓN
# ==================================================

def evaluar_precision_herramienta(herramienta_esperada, herramienta_usada):
    """
    Evalúa si la herramienta usada coincide con la herramienta esperada.
    Retorna 1 si coincide y 0 si no coincide.
    """

    if herramienta_esperada in herramienta_usada:
        return 1

    return 0