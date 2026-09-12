# Read the file
with open(r'.\src\main.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the llm initialization
old = '''        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0.1
        )'''
new = '''        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0.1,
            transport="rest"
        )'''
content = content.replace(old, new)

# Write back
with open(r'.\src\main.py', 'w', encoding='utf-8') as f:
    f.write(content)
