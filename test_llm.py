import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')
print(f'API Key: {api_key[:10]}...')
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash', temperature=0.1)
print('LLM created')
response = llm.invoke('Hello')
print(f'Response: {response}')
