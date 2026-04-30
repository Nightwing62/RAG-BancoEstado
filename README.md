# Asistente Normativo RAG - BancoEstado Microempresas

# Este proyecto es un prototipo funcional de un Agente de Inteligencia Artificial diseñado para apoyar a los ejecutivos comerciales de BancoEstado Microempresas. Utiliza una arquitectura **RAG (Retrieval-Augmented Generation)** para consultar manuales normativos internos y entregar respuestas precisas, mitigando el riesgo de alucinaciones.

# Proyecto desarrollado para la asignatura **Ingeniería de Soluciones con Inteligencia Artificial (ISY0101)**.

##  Características Principales

# * **Búsqueda Semántica:** Extrae contexto relevante de documentos PDF (manuales de crédito, normativas).
# * **Cero Alucinaciones:** Configurado con temperatura baja (0.1) para garantizar respuestas basadas estrictamente en la documentación oficial del banco.
# * **Tecnología Moderna:** Implementado con Python, LangChain, ChromaDB y los modelos de OpenAI (GPT-3.5-turbo).

## 📁 Estructura del Proyecto

# * **`data/`**: Contiene el documento `manual_bancoestado_simulado.pdf` que alimenta la base de datos.
# * **`src/main.py`**: Archivo principal y orquestador del chat interactivo.
# * **`src/rag_pipeline.py`**: Lógica de carga, chunking y vectorización.
# * **`src/prompts.py`**: Plantillas de instrucciones estrictas para el LLM.
# * **`.env`**: Archivo de variables de entorno con las credenciales de la API (excluido del control de versiones).

## 🛠️ Requisitos Previos

* Python 3.10 o superior instalado en tu equipo.
* Una cuenta en Google AI Studio para obtener una API Key gratuita.

## ⚙️ Instalación y Configuración

**1. Clonar el repositorio e ingresar a la carpeta:**
```bash
git clone <URL_DE_TU_REPOSITORIO>
cd RAG-BancoEstado

# 1.Crear y activar el entorno virtual:
# python -m venv venv
# venv\Scripts\activate

# 2.Instalar las dependencias necesarias:
# python -m pip install --upgrade langchain langchain-google-genai langchain-community langchain-chroma pypdf chromadb

## Uso del sistema
# python src/main.py