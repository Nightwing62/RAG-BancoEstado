import os
import json
from datetime import datetime
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_core.tools import tool

from rag_pipeline import crear_pipeline_rag


MEMORIA_FILE = "memoria/historial.json"

def cargar_memoria():

    try:

        with open(
            MEMORIA_FILE,
            "r",
            encoding="utf-8"
        ) as archivo:

            return json.load(archivo)

    except:

        return []


def guardar_memoria(memoria):

    with open(
        MEMORIA_FILE,
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            memoria,
            archivo,
            ensure_ascii=False,
            indent=4
        )


# ==================================================
# AGENTE
# ==================================================

def iniciar_agente():

    print("\n--- Agente Inteligente BancoEstado ---")

    load_dotenv()

    os.makedirs("reportes", exist_ok=True)
    os.makedirs("memoria", exist_ok=True)

    # ==================================================
    # MODELO
    # ==================================================

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0.1
    )

    print("✅ Gemini cargado")

    # ==================================================
    # RAG
    # ==================================================

    retriever = crear_pipeline_rag(
        "data/manual_bancoestado_simulado.pdf"
    )

    print("✅ RAG listo")

    
    @tool
    def buscar_normativas_banco(query: str) -> str:
        """
        Busca información dentro
        de documentos oficiales.
        """

        print("\n🔍 DECISIÓN: Consulta documental")

        docs = retriever.invoke(query)

        if not docs:

            return (
                "No se encontró información "
                "en la documentación."
            )

        return "\n\n".join(
            doc.page_content
            for doc in docs
        )

    @tool
    def generar_reporte(texto: str) -> str:
        """
        Genera reportes ejecutivos.
        """

        print("\n📝 DECISIÓN: Generar reporte")

        prompt = f"""
        Genera un reporte ejecutivo
        profesional utilizando:

        {texto}
        """

        respuesta = llm.invoke(prompt)

        nombre_archivo = (
            f"reportes/reporte_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )

        with open(
            nombre_archivo,
            "w",
            encoding="utf-8"
        ) as archivo:

            archivo.write(
                respuesta.content
            )

        return respuesta.content


    @tool
    def analizar_solicitud(caso: str) -> str:
        """
        Analiza situaciones financieras.
        """

        print("\n🧠 DECISIÓN: Analizar caso")

        prompt = f"""
        Analiza el siguiente caso:

        {caso}

        Entrega:

        - análisis
        - riesgos
        - recomendaciones
        """

        respuesta = llm.invoke(prompt)

        return respuesta.content

    @tool
    def resumir_documento(texto: str) -> str:
        """
        Resume información extensa.
        """

        print("\n📄 DECISIÓN: Resumir contenido")

        prompt = f"""
        Resume el siguiente texto
        en máximo 5 puntos:

        {texto}
        """

        respuesta = llm.invoke(prompt)

        return respuesta.content

    tools = [
        buscar_normativas_banco,
        generar_reporte,
        analizar_solicitud,
        resumir_documento
    ]

    # ==================================================
    # PROMPT
    # ==================================================

    system_prompt = """
    Eres un agente inteligente
    de apoyo para BancoEstado.

    Herramientas disponibles:

    1. buscar_normativas_banco
       Consultar documentos.

    2. generar_reporte
       Crear reportes ejecutivos.

    3. analizar_solicitud
       Analizar casos.

    4. resumir_documento
       Resumir información.

    Reglas:

    - Nunca inventes información.
    - Usa herramientas cuando sea necesario.
    - Si una tarea requiere varios pasos,
      ejecútalos en orden.
    - Fundamenta las respuestas
      en la documentación disponible.
    """

    # ==================================================
    # AGENTE
    # ==================================================

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=system_prompt
    )

    print("✅ Agente listo")

    historial_chat = []
    memoria_largo_plazo = cargar_memoria()

    # ==================================================
    # LOOP
    # ==================================================

    while True:

        pregunta = input(
            "\nEjecutivo Comercial: "
        )

        if pregunta.lower() == "salir":

            break

        historial_chat.append({
            "role": "user",
            "content": pregunta
        })

        try:

            response = agent.invoke({
                "messages": historial_chat
            })

            contenido = (
                response["messages"][-1]
                .content
            )

            if isinstance(
                contenido,
                list
            ):

                respuesta_final = ""

                for item in contenido:

                    if (
                        isinstance(item, dict)
                        and item.get("type")
                        == "text"
                    ):

                        respuesta_final += (
                            item["text"]
                        )

            else:

                respuesta_final = str(
                    contenido
                )

            historial_chat.append({
                "role": "assistant",
                "content": respuesta_final
            })

            memoria_largo_plazo.append({
                "fecha": str(
                    datetime.now()
                ),
                "pregunta": pregunta,
                "respuesta": respuesta_final
            })

            guardar_memoria(
                memoria_largo_plazo
            )

            print(
                f"\n🤖 Asistente IA:\n\n"
                f"{respuesta_final}"
            )

        except Exception as e:

            print(
                f"\n❌ Error: {e}"
            )


if __name__ == "__main__":

    iniciar_agente()