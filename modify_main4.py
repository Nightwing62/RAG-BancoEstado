# Read the file
with open(r'.\src\main.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# We want to insert a print after each of these import lines
import_lines = [
    "from langchain_google_genai import ChatGoogleGenerativeAI",
    "from langchain.agents import initialize_agent, AgentType",
    "from langchain.memory import ConversationBufferMemory",
    "from langchain_core.tools import tool",
    "from rag_pipeline import crear_pipeline_rag",
    "from logger import registrar_log",
    "from metricas import guardar_metrica"
]

new_lines = []
for line in lines:
    new_lines.append(line)
    stripped = line.strip()
    if stripped in import_lines:
        new_lines.append('print("--- After importing: ' + stripped.replace('"', '\\"') + ' ---")\n')

# Write back
with open(r'.\src\main.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
