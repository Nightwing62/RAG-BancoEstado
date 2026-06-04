# Agente Inteligente BancoEstado

## Descripción

Este proyecto implementa un agente inteligente basado en IA para apoyar a ejecutivos comerciales de BancoEstado en la consulta de normativas, generación de reportes, análisis de casos y resumen de información.

El sistema utiliza un enfoque RAG (Retrieval-Augmented Generation) para consultar documentación institucional almacenada en formato PDF, permitiendo generar respuestas fundamentadas en información oficial.

El proyecto fue desarrollado como parte de la asignatura de Agentes Inteligentes y Automatización Organizacional.

---

## Objetivo

Desarrollar un agente capaz de:

- Consultar documentación institucional.
- Mantener memoria de conversaciones.
- Generar reportes ejecutivos.
- Analizar situaciones comerciales.
- Adaptar su comportamiento según el tipo de solicitud.

---

## Arquitectura General

Usuario
↓
Agente LangChain
↓
Gemini 2.0 Flash
↓
Herramientas Especializadas
├── Consulta documental (RAG)
├── Generación de reportes
├── Análisis de casos
└── Resumen de información
↓
ChromaDB + PDF Institucional

---

## Tecnologías Utilizadas

- Python 3.11+
- LangChain
- Google Gemini API
- ChromaDB
- Sentence Transformers
- HuggingFace Embeddings
- PyPDFLoader
- dotenv

---

## Estructura del Proyecto

```text
Proyecto_BancoEstado/
│
├── data/
│   └── manual_bancoestado_simulado.pdf
│
├── db/
│   └── Base vectorial ChromaDB
│
├── memoria/
│   └── historial.json
│
├── src/
├── main.py
├── rag_pipeline.py
├── requirements.txt
├── .env
└── README.md
```

## Funcionalidades

### Consulta Documental

Permite buscar información dentro de los manuales institucionales utilizando recuperación semántica mediante RAG.

Ejemplo:

```text
¿Cuáles son los requisitos del Crédito FOGAPE?
```

### Generación de Reportes

Permite crear reportes ejecutivos basados en información recuperada desde la documentación institucional.

Ejemplo:

```text
Genera un reporte ejecutivo sobre el Crédito FOGAPE.
```

### Análisis de Casos

Permite analizar situaciones comerciales y generar recomendaciones.

Ejemplo:

```text
Analiza una empresa con ingresos variables que solicita financiamiento.
```

### Resumen de Información

Permite sintetizar información extensa en puntos clave.

Ejemplo:

```text
Resume la información del Crédito FOGAPE.
```

---

## Memoria del Agente

### Memoria de Corto Plazo

Se implementa mediante el historial de conversación de la sesión actual.

Permite mantener contexto durante la interacción entre usuario y agente.

### Memoria de Largo Plazo

Se implementa mediante un archivo JSON persistente:

```text
memoria/historial.json
```

Este archivo almacena:

- Fecha de la interacción.
- Consulta realizada.
- Respuesta generada.

Permitiendo conservar información entre distintas ejecuciones del sistema.

---

## Instalación

### 1. Clonar repositorio

```bash
git clone https://github.com/usuario/proyecto-bancoestado.git
```

### 2. Ingresar al proyecto

```bash
cd proyecto-bancoestado
```

### 3. Crear entorno virtual

```bash
python -m venv venv
```

### 4. Activar entorno virtual

Windows:

```bash
venv\Scripts\activate
```

### 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

## pip install langchain-google-genai
## pip install langchain-community
## pip install langchain langchain-community langchain-google-genai chromadb pypdf python-dotenv
---

## Configuración

Crear archivo `.env`

```env
GOOGLE_API_KEY=TU_API_KEY
```

---

## Ejecución

Ejecutar:

```bash
python src/main.py
```

---

## Flujo de Funcionamiento

1. El usuario realiza una consulta.
2. El agente analiza la intención.
3. Selecciona la herramienta adecuada.
4. Recupera contexto desde ChromaDB si es necesario.
5. Gemini genera la respuesta.
6. La interacción se almacena en memoria.
7. Los reportes se guardan automáticamente.