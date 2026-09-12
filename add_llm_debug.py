# Read the file
with open(r'.\src\main.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the line index of "llm = ChatGoogleGenerativeAI("
for i, line in enumerate(lines):
    if line.strip().startswith("llm = ChatGoogleGenerativeAI("):
        # Insert a print before this line
        lines.insert(i, "        print(\"--- Before LLM init ---\")\n")
        # Insert a print after the line that closes the init (we need to find the closing parenthesis)
        # For simplicity, we assume the init ends at line i+3 (after the transport line) but we can search.
        # Instead, we'll insert after the line that contains the closing parenthesis of the llm assignment.
        # We'll search from i forward for a line that contains ")" and has the same indentation.
        j = i
        while j < len(lines):
            if lines[j].strip() == ")":
                lines.insert(j+1, "        print(\"--- After LLM init ---\")\n")
                break
            j += 1
        break

# Write back
with open(r'.\src\main.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)
