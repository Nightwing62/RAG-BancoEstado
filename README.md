Agente Inteligente BancoEstado con RAG y Observabilidad

Proyecto desarrollado para implementar un agente de Inteligencia Artificial aplicado a un flujo organizacional simulado de BancoEstado.

El sistema funciona como un asistente para ejecutivos comerciales y permite consultar documentación institucional mediante RAG, generar reportes, analizar casos, resumir información, mantener memoria conversacional y registrar métricas y logs para observar el comportamiento del agente.

Objetivo del proyecto

El objetivo principal es construir un agente capaz de combinar un modelo de lenguaje con herramientas especializadas y recuperación de información documental.

El agente puede:

Interpretar consultas realizadas por un ejecutivo comercial.

Seleccionar automáticamente la herramienta más adecuada.

Recuperar información desde documentación institucional simulada.

Generar respuestas basadas en contexto documental.

Analizar situaciones financieras o comerciales.

Crear reportes ejecutivos.

Resumir información.

Mantener contexto durante la conversación.

Registrar métricas de rendimiento y trazabilidad.

Funcionalidades principales

Consulta documental mediante RAG.

Recuperación de información desde PDF.

Base vectorial con ChromaDB.

Embeddings mediante Hugging Face / Sentence Transformers.

Generación automática de reportes.

Análisis de casos financieros y comerciales.

Resumen de información.

Memoria conversacional de corto plazo.

Historial persistente de conversaciones.

Registro de logs.

Registro de métricas de observabilidad.

Medición de latencia.

Registro de herramientas utilizadas.

Manejo y registro de errores.

Dashboard de monitoreo con Streamlit.

Herramientas de prueba para validar el LLM y el agente.

Arquitectura general

El flujo principal del sistema es:

Usuario / Ejecutivo Comercial
            │
            ▼
      Agente LangChain
            │
            ├── buscar_normativas_banco
            ├── generar_reporte
            ├── analizar_solicitud
            └── resumir_documento
            │
            ▼
    Google Gemini API
            │
            ▼
      Respuesta final
            │
            ├── Memoria
            ├── Logs
            └── Métricas

Cuando una consulta requiere información documental, el flujo RAG es:

Pregunta del usuario
        │
        ▼
Retriever
        │
        ▼
ChromaDB
        │
        ▼
Fragmentos relevantes del PDF
        │
        ▼
Agente + Gemini
        │
        ▼
Respuesta basada en contexto

Tecnologías utilizadas

Python

LangChain

LangChain Core

LangChain Google GenAI

Google Gemini API

ChromaDB

Hugging Face Embeddings

Sentence Transformers

PyPDFLoader

Streamlit

python-dotenv

JSON

Modelo de IA utilizado

El proyecto utiliza actualmente:

gemini-3.6-flash

El modelo se integra mediante:

ChatGoogleGenerativeAI

Configuración utilizada:

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0.1,
    convert_system_message_to_human=True
)

Nota: los modelos de Gemini pueden quedar obsoletos con el tiempo. Si Google retira un modelo, se debe actualizar el nombre del modelo configurado en el proyecto.

Versiones de LangChain utilizadas durante el desarrollo

El entorno utilizado durante las pruebas incluye:

langchain: 0.1.14
langchain-core: 0.1.53
langchain-google-genai: 0.0.11

La implementación actual utiliza initialize_agent, que sigue funcionando en estas versiones, aunque LangChain lo marca como deprecado.

En una futura actualización se recomienda migrar a los constructores modernos de agentes de LangChain.

Estructura del proyecto

RAG-BancoEstado/
│
├── data/
│   └── manual_bancoestado_simulado.pdf
│
├── db/
│   └── Base vectorial ChromaDB
│
├── logs/
│   └── agente.log
│
├── memoria/
│   └── historial.json
│
├── metricas/
│   └── metricas.json
│
├── notebooks/
│
├── reportes/
│   └── reportes generados automáticamente
│
├── src/
│   ├── main.py
│   ├── rag_pipeline.py
│   ├── logger.py
│   ├── metricas.py
│   ├── dashboard.py
│   ├── prompts.py
│   ├── utils.py
│   ├── test_llm.py
│   └── test_agent.py
│
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
└── README.md

Descripción del sistema

El agente funciona como un asistente inteligente para ejecutivos comerciales.

Al recibir una consulta, analiza la intención del usuario y decide si debe responder directamente o utilizar una herramienta.

Las herramientas disponibles son:

buscar_normativas_banco
generar_reporte
analizar_solicitud
resumir_documento

Herramientas del agente

1. buscar_normativas_banco

Se utiliza cuando la consulta requiere información contenida en la documentación institucional.

Ejemplos:

¿Cuáles son los requisitos del Crédito FOGAPE?

¿Qué condiciones aparecen en el manual para solicitar financiamiento?

Flujo:

Pregunta
  │
  ▼
Retriever
  │
  ▼
ChromaDB
  │
  ▼
Fragmentos relevantes
  │
  ▼
Respuesta del agente

2. generar_reporte

Genera un reporte ejecutivo profesional a partir de información proporcionada.

El reporte incluye:

Título.

Resumen ejecutivo.

Puntos principales.

Conclusión.

Además, se guarda automáticamente en:

reportes/

Ejemplo:

Genera un reporte ejecutivo sobre el Crédito FOGAPE.

3. analizar_solicitud

Analiza situaciones financieras o comerciales.

La respuesta se estructura en:

Análisis del caso.

Riesgos detectados.

Recomendaciones.

Conclusión.

Ejemplo:

Analiza una empresa con ingresos variables que solicita financiamiento.

4. resumir_documento

Resume información extensa en un máximo de cinco puntos principales.

Ejemplo:

Resume la información disponible sobre el Crédito FOGAPE.

Sistema RAG

El sistema utiliza Retrieval-Augmented Generation (RAG) para responder preguntas basadas en documentación.

El documento utilizado se encuentra en:

data/manual_bancoestado_simulado.pdf

El pipeline realiza las siguientes etapas:

PDF
 │
 ▼
Carga del documento
 │
 ▼
División en fragmentos
 │
 ▼
Generación de embeddings
 │
 ▼
Almacenamiento en ChromaDB
 │
 ▼
Búsqueda semántica
 │
 ▼
Recuperación de fragmentos relevantes
 │
 ▼
Respuesta del agente

El objetivo es reducir respuestas inventadas y utilizar información recuperada desde una fuente documental.

Memoria

El proyecto utiliza dos formas de almacenamiento de conversación.

Memoria conversacional

Se utiliza ConversationBufferMemory para conservar el contexto mientras el agente se encuentra en ejecución.

Ejemplo:

Ejecutivo: Mi cliente se llama Carlos.

Ejecutivo: ¿Cómo se llama el cliente?

Agente: Carlos.

Historial persistente

Las consultas y respuestas también se almacenan en:

memoria/historial.json

Cada registro contiene:

{
    "fecha": "fecha y hora",
    "pregunta": "consulta realizada",
    "respuesta": "respuesta generada"
}

Actualmente este archivo funciona como historial persistente y registro de conversaciones.

Observabilidad

El sistema incorpora una capa de observabilidad para analizar el funcionamiento del agente.

Las métricas registradas incluyen:

Pregunta realizada.

Herramienta utilizada.

Latencia.

Estado de ejecución.

Largo de la respuesta.

Información del error, si corresponde.

Los datos se almacenan en:

metricas/metricas.json

Ejemplo conceptual:

{
    "pregunta": "¿Cuáles son los requisitos del Crédito FOGAPE?",
    "herramienta": "buscar_normativas_banco",
    "latencia": 2.45,
    "estado": "OK",
    "largo_respuesta": 850
}

Trazabilidad

Cada ejecución del agente genera un registro en:

logs/agente.log

Los logs permiten revisar:

Fecha y hora.

Pregunta del usuario.

Respuesta generada.

Herramienta utilizada.

Latencia.

Estado de ejecución.

Error detectado, si corresponde.

Esto permite identificar fallos y analizar el comportamiento del agente.

Dashboard

El proyecto incluye un dashboard desarrollado con Streamlit.

Permite visualizar indicadores como:

Total de consultas.

Latencia promedio.

Cantidad de errores.

Tasa de error.

Herramientas más utilizadas.

Evolución de la latencia.

Distribución de estados OK y ERROR.

Para ejecutarlo:

streamlit run src/dashboard.py

Es recomendable realizar varias consultas al agente antes de abrir el dashboard, para disponer de métricas que visualizar.

Instalación

1. Clonar el repositorio

git clone https://github.com/usuario/proyecto-bancoestado.git

2. Ingresar a la carpeta

cd proyecto-bancoestado

3. Crear entorno virtual

python -m venv venv

4. Activar el entorno virtual

Windows CMD:

venv\Scripts\activate

Windows PowerShell:

.\venv\Scripts\Activate.ps1

5. Instalar dependencias

pip install -r requirements.txt

Configuración

Crear un archivo .env en la raíz del proyecto.

Contenido:

GOOGLE_API_KEY=TU_API_KEY

Opcionalmente, el nombre del modelo puede configurarse también desde variables de entorno si se implementa esta configuración:

GEMINI_MODEL=gemini-3.6-flash

El archivo .env contiene información sensible y no debe subirse a GitHub.

Para documentar la configuración se puede utilizar:

.env.example

Ejemplo:

GOOGLE_API_KEY=TU_API_KEY_AQUI
GEMINI_MODEL=gemini-3.6-flash

Ejecución del agente

Desde la raíz del proyecto:

python src/main.py

Al iniciar correctamente se mostrará un mensaje similar a:

--- Agente Inteligente BancoEstado con Observabilidad ---

Gemini cargado correctamente
RAG cargado correctamente
Agente creado correctamente
Agente listo.

Luego se pueden realizar consultas:

Ejecutivo Comercial: ¿Cuáles son los requisitos del Crédito FOGAPE?

Para finalizar:

salir

También se aceptan:

exit
quit

Pruebas

El proyecto incluye archivos destinados a verificar componentes de forma independiente.

Prueba del modelo

Archivo:

src/test_llm.py

Ejecutar:

python src/test_llm.py

Esta prueba permite comprobar:

API Key.

Conexión con Gemini.

Disponibilidad del modelo.

Generación básica de respuesta.

Prueba del agente

Archivo:

src/test_agent.py

Ejecutar:

python src/test_agent.py

Esta prueba permite comprobar:

Inicialización del agente.

Compatibilidad entre LangChain y Gemini.

Memoria conversacional.

Uso de herramientas.

Ejecución del AgentExecutor.

Pruebas funcionales sugeridas

Consulta documental

¿Cuáles son los requisitos del Crédito FOGAPE?

Resultado esperado:

buscar_normativas_banco

Generación de reporte

Genera un reporte ejecutivo sobre el Crédito FOGAPE.

Resultado esperado:

generar_reporte

Análisis de caso

Analiza una empresa con ingresos variables que solicita financiamiento.

Resultado esperado:

analizar_solicitud

Resumen

Resume la información disponible sobre el Crédito FOGAPE.

Resultado esperado:

resumir_documento

Consulta fuera de la documentación

¿Qué información contiene el manual sobre un producto que no aparece documentado?

El agente debe indicar que no dispone de información suficiente en la documentación y evitar inventar datos.

Archivos generados automáticamente

Durante la ejecución se pueden generar:

memoria/historial.json
logs/agente.log
metricas/metricas.json
reportes/reporte_YYYYMMDD_HHMMSS.txt

Estos archivos permiten conservar conversaciones, auditar ejecuciones y analizar el rendimiento del sistema.

Manejo de errores

El sistema registra excepciones producidas durante la ejecución.

Cuando ocurre un error se almacena:

Consulta.

Estado ERROR.

Latencia hasta el fallo.

Mensaje de error.

Herramienta asociada.

Esto permite analizar problemas sin detener el resto del diseño del sistema.

Seguridad y uso responsable

El proyecto considera medidas básicas de seguridad:

API Key almacenada mediante .env.

Exclusión de .env mediante .gitignore.

Uso de .env.example como plantilla.

No almacenar claves privadas dentro del código fuente.

Registro controlado de errores.

Instrucción al agente para no inventar información.

Respuesta explícita cuando la documentación no contiene información suficiente.

Separación entre datos, logs, métricas y código fuente.

Consideraciones importantes

Modelo Gemini

Los modelos disponibles mediante la API de Gemini pueden cambiar con el tiempo.

Si aparece un error similar a:

404 This model is no longer available

se debe revisar el modelo configurado en:

ChatGoogleGenerativeAI(...)

y actualizarlo por un modelo disponible.

LangChain

La versión actual del proyecto utiliza:

initialize_agent(...)

LangChain muestra una advertencia de deprecación para esta función.

Esto no impide actualmente la ejecución del proyecto, pero se recomienda realizar una futura migración a los constructores modernos de agentes.

Recomendaciones de mejora

Posibles mejoras futuras:

Migrar desde initialize_agent a la API moderna de agentes de LangChain.

Utilizar el historial persistente como memoria real entre ejecuciones.

Agregar fuentes y número de página a las respuestas del RAG.

Incorporar más documentos institucionales.

Implementar evaluación automática de calidad de respuestas.

Incorporar métricas de precisión y consistencia.

Implementar caché para consultas frecuentes.

Mejorar clasificación de intención.

Agregar autenticación al dashboard.

Separar logs técnicos de logs de auditoría.

Configurar el modelo Gemini completamente desde .env.

Agregar pruebas automatizadas.

Incorporar control de versiones de la base vectorial.

Estado actual del proyecto

Actualmente se encuentran operativos:

[OK] Conexión con Google Gemini
[OK] Agente LangChain
[OK] Herramientas del agente
[OK] Pipeline RAG
[OK] Memoria conversacional
[OK] Historial persistente
[OK] Registro de métricas
[OK] Registro de logs
[OK] Generación de reportes
[OK] Dashboard Streamlit