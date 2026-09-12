# Read the file
with open(r'.\src\main.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the line index of "def iniciar_agente():"
for i, line in enumerate(lines):
    if line.strip() == "def iniciar_agente():":
        # Replace this line with the function definition and a print
        lines[i] = "def iniciar_agente():\n"
        lines.insert(i+1, "    print(\"--- Iniciar agente function start ---\")\n")
        break

# Write back
with open(r'.\src\main.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)
