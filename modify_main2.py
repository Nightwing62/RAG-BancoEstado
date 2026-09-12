# Read the backup file
with open(r'.\src\main.py.bak', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the replacements for each function

# 1. generar_reporte
old_gen = r'''        prompt = f"""
        Genera un reporte ejecutivo profesional, claro y estructurado
        a partir de la siguiente información:

        {texto}

        El reporte debe incluir:
        - Título
        - Resumen ejecutivo
        - Puntos principales
        - Conclusión
        """

        respuesta = llm.invoke(prompt)
        texto_respuesta = extraer_texto(respuesta.content)'''

new_gen = r'''        prompt = f"""
        Genera un reporte ejecutivo profesional, claro y estructurado
        a partir de la siguiente información:

        {texto}

        El reporte debe incluir:
        - Título
        - Resumen ejecutivo
        - Puntos principales
        - Conclusión
        """

        print("--- LLM CALL START: generar_reporte ---")
        respuesta = llm.invoke(prompt)
        texto_respuesta = extraer_texto(respuesta.content)
        print("--- LLM CALL END: generar_reporte ---")'''

content = content.replace(old_gen, new_gen)

# 2. analizar_solicitud
old_ana = r'''        prompt = f"""
        Analiza el siguiente caso financiero o comercial:

        {caso}

        Entrega la respuesta con esta estructura:

        1. Análisis del caso
        2. Riesgos detectados
        3. Recomendaciones
        4. Conclusión
        """

        respuesta = llm.invoke(prompt)

        return extraer_texto(respuesta.content)'''

new_ana = r'''        prompt = f"""
        Analiza el siguiente caso financiero o comercial:

        {caso}

        Entrega la respuesta con esta estructura:

        1. Análisis del caso
        2. Riesgos detectados
        3. Recomendaciones
        4. Conclusión
        """

        print("--- LLM CALL START: analizar_solicitud ---")
        respuesta = llm.invoke(prompt)
        print("--- LLM CALL END: analizar_solicitud ---")
        return extraer_texto(respuesta.content)'''

content = content.replace(old_ana, new_ana)

# 3. resumir_documento
old_res = r'''        prompt = f"""
        Resume la siguiente información en máximo 5 puntos claros:

        {texto}
        """

        respuesta = llm.invoke(prompt)

        return extraer_texto(respuesta.content)'''

new_res = r'''        prompt = f"""
        Resume la siguiente información en máximo 5 puntos claros:

        {texto}
        """

        print("--- LLM CALL START: resumir_documento ---")
        respuesta = llm.invoke(prompt)
        print("--- LLM CALL END: resumir_documento ---")
        return extraer_texto(respuesta.content)'''

content = content.replace(old_res, new_res)

# Write the modified content to the main file
with open(r'.\src\main.py', 'w', encoding='utf-8') as f:
    f.write(content)
