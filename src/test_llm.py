import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")  

respuesta = llm.invoke("Hola, ¿estás listo para el proyecto de BancoEstado?")

print(respuesta.content)