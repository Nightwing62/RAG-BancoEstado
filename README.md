# Agente Inteligente BancoEstado con Observabilidad

Proyecto desarrollado para implementar un agente de IA aplicado a un flujo organizacional simulado de BancoEstado.

El sistema permite consultar documentación institucional mediante RAG, generar reportes, analizar casos, resumir información y registrar métricas de observabilidad para evaluar el desempeño del agente.

---

## Funcionalidades principales

* Consulta documental usando RAG.
* Recuperación de información desde PDF institucional.
* Generación automática de reportes.
* Análisis de casos financieros.
* Resumen de información.
* Memoria conversacional.
* Registro de logs de ejecución.
* Registro de métricas de observabilidad.
* Dashboard de monitoreo con Streamlit.

---

## Tecnologías utilizadas

* Python
* LangChain
* Google Gemini API
* ChromaDB
* Sentence Transformers
* HuggingFace Embeddings
* PyPDFLoader
* Streamlit
* dotenv
* JSON

---

## Estructura del proyecto

```text
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
├── reportes/
│   └── reportes generados automáticamente
│
├── src/
│   ├── main.py
│   ├── rag_pipeline.py
│   ├── logger.py
│   ├── metricas.py
│   ├── dashboard.py
│   └── utils.py
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Descripción del sistema

El agente funciona como un asistente para ejecutivos comerciales. Recibe consultas del usuario, analiza la intención de la solicitud y selecciona una herramienta adecuada para responder.

El sistema puede utilizar las siguientes herramientas:

```text
buscar_normativas_banco
generar_reporte
analizar_solicitud
resumir_documento
```

La información documental se recupera desde un archivo PDF ubicado en la carpeta `data/`. El contenido del documento se procesa mediante embeddings y se almacena en una base vectorial ChromaDB.

---

## Observabilidad implementada

Para el Parcial 3 se agregó una capa de observabilidad que permite analizar el comportamiento del agente.

Las métricas implementadas son:

* Latencia de respuesta.
* Estado de ejecución: OK o ERROR.
* Herramienta utilizada.
* Largo de la respuesta generada.
* Frecuencia de errores.
* Cantidad total de consultas.

Los datos se almacenan en:

```text
metricas/metricas.json
```

---

## Trazabilidad

Cada ejecución del agente genera un registro en:

```text
logs/agente.log
```

Cada log contiene:

* Fecha y hora.
* Pregunta del usuario.
* Herramienta utilizada.
* Latencia.
* Estado de ejecución.
* Respuesta generada.
* Error detectado, si corresponde.

---

## Dashboard

El proyecto incluye un dashboard desarrollado con Streamlit.

El dashboard permite visualizar:

* Total de consultas.
* Latencia promedio.
* Cantidad de errores.
* Tasa de error.
* Herramientas más utilizadas.
* Evolución de la latencia.
* Distribución de estados OK y ERROR.

Para ejecutar el dashboard:

```bash
streamlit run src/dashboard.py
```

---

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/usuario/proyecto-bancoestado.git
```

Ingresar a la carpeta del proyecto:

```bash
cd proyecto-bancoestado
```

Crear entorno virtual:

```bash
python -m venv venv
```

Activar entorno virtual en Windows:

```bash
venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Configuración

Crear un archivo `.env` en la raíz del proyecto.

Contenido del archivo:

```env
GOOGLE_API_KEY=TU_API_KEY
```

El archivo `.env` no debe subirse a GitHub.

Para documentar la configuración se incluye el archivo:

```text
.env.example
```

Ejemplo:

```env
GOOGLE_API_KEY=TU_API_KEY_AQUI
```

---

## Ejecución del agente

Desde la raíz del proyecto ejecutar:

```bash
python src/main.py
```

Ejemplo de interacción:

```text
Ejecutivo Comercial: ¿Cuáles son los requisitos del Crédito FOGAPE?
```

Para cerrar el agente:

```text
salir
```

---

## Ejecución del dashboard

Primero se deben realizar consultas al agente para generar métricas.

Luego ejecutar:

```bash
streamlit run src/dashboard.py
```

---

## Archivos generados automáticamente

Durante la ejecución se generan los siguientes archivos:

```text
memoria/historial.json
logs/agente.log
metricas/metricas.json
reportes/reporte_YYYYMMDD_HHMMSS.txt
```

---

## Pruebas sugeridas

Consulta documental:

```text
¿Cuáles son los requisitos del Crédito FOGAPE?
```

Generación de reporte:

```text
Genera un reporte ejecutivo sobre el Crédito FOGAPE.
```

Análisis de caso:

```text
Analiza una empresa con ingresos variables que solicita financiamiento.
```

Resumen:

```text
Resume la información del Crédito FOGAPE.
```

Consulta fuera del documento:

```text
¿Qué tasas tiene el crédito hipotecario?
```

Esta última prueba permite verificar que el agente no invente información cuando el dato no se encuentra en la documentación disponible.

---

## Seguridad y uso responsable

El sistema considera medidas básicas de seguridad:

* Uso de archivo `.env` para proteger la API Key.
* Exclusión de `.env` mediante `.gitignore`.
* Uso de `.env.example` como plantilla.
* Validación de entradas del usuario.
* Registro de errores sin exponer claves privadas.
* Instrucción al agente para no inventar información.
* Respuesta explícita cuando la información no está disponible en los documentos.

---

## Recomendaciones de mejora

A partir de los datos obtenidos en métricas y logs, se pueden considerar las siguientes mejoras:

* Agregar más documentos institucionales para ampliar la cobertura del RAG.
* Optimizar prompts para reducir latencia.
* Implementar caché para consultas frecuentes.
* Mejorar la clasificación de intención del usuario.
* Ampliar el dashboard con métricas de precisión y consistencia.
* Separar logs técnicos de logs visibles para auditoría.

---

## Autor

* Felipe Cárdenas
---

## Referencias

* LangChain Documentation.
* Google Gemini API Documentation.
* ChromaDB Documentation.
* Streamlit Documentation.
* Sentence Transformers Documentation.
