import pandas as pd
import streamlit as st

from logger import leer_logs

st.set_page_config(page_title="Observabilidad · Agente BancoEstado", layout="wide")
st.title("📊 Dashboard de Observabilidad — Agente RAG BancoEstado")

# ---------------------------------------------------------
# Carga de datos
# ---------------------------------------------------------
registros = leer_logs()

if not registros:
    st.warning(
        "Aún no hay registros en logs/agente.log.\n\n"
        "Ejecuta el agente (main.py) para generar tráfico real, "
        "y/o corre `python metricas.py` para la evaluación offline."
    )
    st.stop()

df = pd.DataFrame(registros)
df["timestamp"] = pd.to_datetime(df["timestamp"])

turnos = df[df["tipo"] == "turno_agente"].copy()
herramientas = df[df["tipo"] == "uso_herramienta"].copy()

# ---------------------------------------------------------
# KPIs principales
# ---------------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

total_consultas = len(turnos)
tasa_error = (turnos["status"] == "error").mean() if total_consultas else 0
latencia_prom = turnos["duracion_segundos"].mean() if total_consultas else 0
latencia_p95 = turnos["duracion_segundos"].quantile(0.95) if total_consultas else 0

col1.metric("Total de consultas", total_consultas)
col2.metric("Tasa de error", f"{tasa_error:.1%}")
col3.metric("Latencia promedio", f"{latencia_prom:.2f} s")
col4.metric("Latencia p95", f"{latencia_p95:.2f} s")

st.divider()

# ---------------------------------------------------------
# Latencia en el tiempo
# ---------------------------------------------------------
st.subheader("⏱️ Latencia por consulta a lo largo del tiempo")
if not turnos.empty:
    st.line_chart(turnos.set_index("timestamp")["duracion_segundos"])
else:
    st.info("No hay turnos de agente registrados aún.")

# ---------------------------------------------------------
# Uso de herramientas
# ---------------------------------------------------------
st.subheader("🛠️ Distribución de uso de herramientas")
if not herramientas.empty:
    conteo = herramientas["herramienta"].value_counts()
    st.bar_chart(conteo)
else:
    st.info("No hay registros de uso de herramientas todavía (revisa la integración del decorador en main.py).")

# ---------------------------------------------------------
# Errores recientes (trazabilidad — apartado B)
# ---------------------------------------------------------
st.subheader("🚨 Errores recientes")
errores_df = df[df["status"] == "error"].sort_values("timestamp", ascending=False)
if not errores_df.empty:
    st.dataframe(errores_df[["timestamp", "tipo", "error"]].head(20), use_container_width=True)
else:
    st.success("No se han registrado errores.")

# ---------------------------------------------------------
# Métricas de evaluación offline (metricas.py) — precisión y consistencia
# ---------------------------------------------------------
st.divider()
st.subheader("🎯 Precisión y consistencia (evaluación con escenarios de variabilidad)")

try:
    metricas_df = pd.read_csv("reportes/resultados_metricas.csv")
    st.dataframe(metricas_df, use_container_width=True)

    precision_df = metricas_df[metricas_df["metrica"] == "precision_at_k"]
    if not precision_df.empty:
        st.bar_chart(precision_df.set_index("detalle")["valor"])
except FileNotFoundError:
    st.info("Corre `python metricas.py` primero para generar reportes/resultados_metricas.csv")

# ---------------------------------------------------------
# Logs crudos completos (trazabilidad — apartado B)
# ---------------------------------------------------------
st.divider()
st.subheader("🔍 Logs crudos (trazabilidad)")
st.dataframe(df.sort_values("timestamp", ascending=False), use_container_width=True)