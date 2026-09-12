# Read the file
with open(r'.\src\main.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Define insertions: (index, text) where index is the 0-indexed position to insert at (after the line at index-1)
# We want to insert after the given 1-indexed line number -> index = line_number (0-indexed)
insertions = [
    # generar_reporte: after line 170 and after line 173
    (170, '        print(\"--- LLM CALL START: generar_reporte ---\")\n'),
    (173, '        print(\"--- LLM CALL END: generar_reporte ---\")\n'),
    # analizar_solicitud: after line 212 and after line 216
    (212, '        print(\"--- LLM CALL START: analizar_solicitud ---\")\n'),
    (216, '        print(\"--- LLM CALL END: analizar_solicitud ---\")\n'),
    # resumir_documento: after line 239 and after line 243
    (239, '        print(\"--- LLM CALL START: resumir_documento ---\")\n'),
    (243, '        print(\"--- LLM CALL END: resumir_documento ---\")\n')
]

# Sort insertions by index descending
insertions.sort(key=lambda x: x[0], reverse=True)

# Apply insertions
for index, text in insertions:
    lines.insert(index, text)

# Write back
with open(r'.\src\main.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)
