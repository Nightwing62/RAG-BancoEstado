import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from rag_pipeline import crear_pipeline_rag
from prompts import rag_prompt_template

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def iniciar_asistente():
    print("--- Iniciando Asistente Normativo BancoEstado ---")

    load_dotenv()

    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash-latest", 
            temperature=0.1
        )
    except Exception as e:
        print(f"Error al cargar el LLM. Revisa tu API Key: {e}")
        return

    ruta_documento = "data/manual_bancoestado_simulado.pdf"

    try:
        retriever = crear_pipeline_rag(ruta_documento)
    except Exception as e:
        print(f"Error al leer el PDF: {e}")
        return

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | rag_prompt_template
        | llm
        | StrOutputParser()
    )

    print("\n¡Sistema listo! Escribe 'salir' para terminar.\n")
    print("-" * 50)

    while True:
        pregunta = input("\nEjecutivo Comercial: ")
        
        if pregunta.lower() in ['salir', 'exit', 'quit']:
            print("Cerrando el sistema... ¡Buen turno!")
            break
            
        print("Buscando en normativas...")
        
        try:
            # Ahora la cadena se invoca pasándole directamente el texto
            respuesta = chain.invoke(pregunta)
            print("\nAsistente IA:")
            print(respuesta)
        except Exception as e:
            print(f"\nOcurrió un error de conexión: {e}")
            
        print("-" * 50)

if __name__ == "__main__":
    iniciar_asistente()