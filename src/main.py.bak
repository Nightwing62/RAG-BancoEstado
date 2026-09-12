import os
import json
import time

from datetime import datetime
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from langchain_core.tools import tool

from rag_pipeline import crear_pipeline_rag
from logger import registrar_log
from metricas import guardar_metrica


MEMORIA_FILE = "memoria/historial.json"


# ==================================================
# MEMORIA PERSISTENTE
# ==================================================

def cargar_memoria():
    try:
        with open(MEMORIA_FILE, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except:
        return []


def guardar_memoria(memoria):
    os.makedirs("memoria", exist_ok=True)

    with open(MEMORIA_FILE, "w", encoding="utf-8") as archivo:
        json.dump(
            memoria,
            archivo,
            ensure_ascii=False,
            indent=4
        )


# ==================================================
# LIMPIEZA DE RESPUESTAS
# ==================================================

def extraer_texto(contenido):
    if isinstance(contenido, list):
        texto_final = ""

        for item in contenido:
            if isinstance(item, dict) and item.get("type") == "text":
                texto_final += item.get("text", "")

        return texto_final

    return str(contenido)


# ==================================================
# AGENTE PRINCIPAL
# ==================================================

def iniciar_agente():

    print("\n--- Agente Inteligente BancoEstado con Observabilidad ---")

    load_dotenv()

    os.makedirs("memoria", exist_ok=True)
    os.makedirs("reportes", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    os.makedirs("metricas", exist_ok=True)

    # ==================================================
    # 1. MODELO LLM
    # ==================================================

    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0.1
        )

        print("✅ Gemini cargado correctamente")

    except Exception as e:
        print(f"❌ Error cargando Gemini: {e}")
        return

    # ==================================================
    # 2. RAG
    # ==================================================

    try:
        retriever = crear_pipeline_rag(
            "data/manual_bancoestado_simulado.pdf"
        )

        print("✅ RAG cargado correctamente")

    except Exception as e:
        print(f"❌ Error cargando RAG: {e}")
        return

    # Lista para registrar herramientas usadas
    herramientas_usadas = []

    # ==================================================
    # 3. TOOL CONSULTA DOCUMENTAL
    # ==================================================

    @tool
    def buscar_normativas_banco(query: str) -> str:
        """
        Busca información en documentos oficiales de BancoEstado.
        Útil para consultas sobre requisitos, normativas, productos,
        plazos, créditos o condiciones comerciales.
        """

        print("\n🔍 DECISIÓN: Consulta documental")
        print("🔍 TOOL USADA: buscar_normativas_banco")

        herramientas_usadas.append("buscar_normativas_banco")

        try:
            docs = retriever.invoke(query)

            if not docs:
                return "No se encontró información en la documentación oficial."

            resultado = "\n\n".join(
                doc.page_content for doc in docs
            )

            return resultado

        except Exception as e:
            return f"Error usando herramienta RAG: {e}"

    # ==================================================
    # 4. TOOL GENERACIÓN DE REPORTES
    # ==================================================

    @tool
    def generar_reporte(texto: str) -> str:
        """
        Genera un reporte ejecutivo a partir de información entregada.
        Útil cuando el usuario pide un informe, reporte o resumen ejecutivo.
        """

        print("\n📝 DECISIÓN: Generar reporte")
        print("📝 TOOL USADA: generar_reporte")

        herramientas_usadas.append("generar_reporte")

        prompt = f"""
        Genera un reporte ejecutivo profesional, claro y estructurado
        a partir de la siguiente información:

        {texto}

        El reporte debe incluir:
        - Título
        - Resumen ejecutivo
        - Puntos principales
        - Conclusión
        """

        respuesta = llm.invoke(prompt)
        texto_respuesta = extraer_texto(respuesta.content)

        nombre_archivo = (
            f"reportes/reporte_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )

        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(texto_respuesta)

        return texto_respuesta

    # ==================================================
    # 5. TOOL ANÁLISIS
    # ==================================================

    @tool
    def analizar_solicitud(caso: str) -> str:
        """
        Analiza situaciones financieras o comerciales.
        Útil cuando el usuario pide evaluar riesgos, casos o recomendaciones.
        """

        print("\n🧠 DECISIÓN: Analizar caso")
        print("🧠 TOOL USADA: analizar_solicitud")

        herramientas_usadas.append("analizar_solicitud")

        prompt = f"""
        Analiza el siguiente caso financiero o comercial:

        {caso}

        Entrega la respuesta con esta estructura:

        1. Análisis del caso
        2. Riesgos detectados
        3. Recomendaciones
        4. Conclusión
        """

        respuesta = llm.invoke(prompt)

        return extraer_texto(respuesta.content)

    # ==================================================
    # 6. TOOL RESUMEN
    # ==================================================

    @tool
    def resumir_documento(texto: str) -> str:
        """
        Resume información extensa en puntos clave.
        Útil cuando el usuario pide resumir una respuesta anterior,
        un documento o información recuperada.
        """

        print("\n📄 DECISIÓN: Resumir contenido")
        print("📄 TOOL USADA: resumir_documento")

        herramientas_usadas.append("resumir_documento")

        prompt = f"""
        Resume la siguiente información en máximo 5 puntos claros:

        {texto}
        """

        respuesta = llm.invoke(prompt)

        return extraer_texto(respuesta.content)

    # ==================================================
    # 7. LISTA DE HERRAMIENTAS
    # ==================================================

    tools = [
        buscar_normativas_banco,
        generar_reporte,
        analizar_solicitud,
        resumir_documento
    ]

    # ==================================================
    # 8. PROMPT DEL AGENTE
    # ==================================================

    system_prompt = """
    Eres un agente inteligente de apoyo para ejecutivos comerciales
    de BancoEstado.

    Tu función es responder consultas, recuperar información desde
    documentos internos, generar reportes, resumir información y analizar
    casos financieros.

    Herramientas disponibles:

    1. buscar_normativas_banco:
       úsala para consultar información en documentos oficiales.

    2. generar_reporte:
       úsala cuando el usuario pida un informe o reporte ejecutivo.

    3. analizar_solicitud:
       úsala cuando el usuario pida analizar un caso o situación.

    4. resumir_documento:
       úsala cuando el usuario pida resumir información.

    Reglas obligatorias:

    - Nunca inventes información.
    - Si la consulta requiere información documental, usa buscar_normativas_banco.
    - Si el usuario pide un reporte, usa generar_reporte.
    - Si el usuario pide analizar un caso, usa analizar_solicitud.
    - Si el usuario pide resumir, usa resumir_documento.
    - Si una tarea tiene varias etapas, ejecútalas en orden.
    - Si la información no aparece en los documentos, indícalo claramente.
    - Responde con lenguaje profesional, claro y breve.
    """

    # ==================================================
    # 9. MEMORIA DE CORTO PLAZO
    # ==================================================

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    memoria_largo_plazo = cargar_memoria()

    # ==================================================
    # 10. CREAR AGENTE COMPATIBLE CON TU VERSIÓN
    # ==================================================

    try:
        agent = initialize_agent(
            tools=tools,
            llm=llm,
            agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            memory=memory,
            agent_kwargs={
                "prefix": system_prompt
            },
            handle_parsing_errors=True
        )

        print("✅ Agente creado correctamente con initialize_agent")

    except Exception as e:
        print(f"❌ Error creando agente: {e}")
        return

    # ==================================================
    # 11. LOOP PRINCIPAL
    # ==================================================

    print("\n🤖 Agente listo.")
    print("Escribe 'salir' para terminar.")
    print("-" * 60)

    while True:

        pregunta = input("\nEjecutivo Comercial: ")

        if pregunta.lower().strip() in ["salir", "exit", "quit"]:
            print("\nCerrando sistema...")
            break

        inicio = time.time()
        herramientas_usadas.clear()

        try:
            resultado = agent.invoke({
                "input": pregunta
            })

            if isinstance(resultado, dict):
                respuesta_final = resultado.get("output", str(resultado))
            else:
                respuesta_final = str(resultado)

            respuesta_final = extraer_texto(respuesta_final)

            memoria_largo_plazo.append({
                "fecha": str(datetime.now()),
                "pregunta": pregunta,
                "respuesta": respuesta_final
            })

            guardar_memoria(memoria_largo_plazo)

            fin = time.time()
            latencia = fin - inicio

            if herramientas_usadas:
                herramienta_final = ", ".join(herramientas_usadas)
            else:
                herramienta_final = "agente_general"

            guardar_metrica(
                pregunta=pregunta,
                herramienta=herramienta_final,
                latencia=latencia,
                estado="OK",
                largo_respuesta=len(respuesta_final)
            )

            registrar_log(
                pregunta=pregunta,
                respuesta=respuesta_final,
                herramienta=herramienta_final,
                latencia=latencia,
                estado="OK"
            )

            print(f"\n🤖 Asistente IA:\n\n{respuesta_final}")
            print(f"\n⏱️ Latencia: {latencia:.2f} segundos")
            print(f"🧩 Herramienta(s): {herramienta_final}")

        except Exception as e:

            fin = time.time()
            latencia = fin - inicio

            guardar_metrica(
                pregunta=pregunta,
                herramienta="error",
                latencia=latencia,
                estado="ERROR",
                largo_respuesta=0,
                error=str(e)
            )

            registrar_log(
                pregunta=pregunta,
                respuesta="Sin respuesta",
                herramienta="error",
                latencia=latencia,
                estado="ERROR",
                error=str(e)
            )

            print(f"\n❌ Error: {e}")
            print(f"⏱️ Latencia hasta el error: {latencia:.2f} segundos")

        print("-" * 60)


if __name__ == "__main__":
    iniciar_agente()