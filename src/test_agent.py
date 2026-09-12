from dotenv import load_dotenv

from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()


@tool
def herramienta_prueba(texto: str) -> str:
    """
    Herramienta simple de prueba.
    """
    return f"Resultado de prueba: {texto}"


llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0.1,
    convert_system_message_to_human=True
)


print("Modelo:", llm.model)
print(
    "Convert system:",
    llm.convert_system_message_to_human
)


# ==================================================
# MEMORIA
# ==================================================

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=False
)


# ==================================================
# AGENTE
# ==================================================

agent = initialize_agent(
    tools=[herramienta_prueba],
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    memory=memory,
    handle_parsing_errors=True
)


resultado = agent.invoke({
    "input": "Usa la herramienta de prueba con el texto BancoEstado"
})


print("\nRESULTADO:")
print(resultado)