import streamlit as st
import pandas as pd
import plotly.express as px

ruta_archivo = r"C:\Users\SaraO\OneDrive - Universidad EAFIT\Semestres\5to semestre\Proyecto integrador 1\DataYa\Code\base_de_datos.csv"
df = pd.read_csv(ruta_archivo, encoding='latin1') 


# Layout del Dashboard
st.title("Reporte en tiempo real de propiedades")

# Opciones de filtro
mostrar_categoria_cliente = st.sidebar.checkbox("Mostrar Gráfico: Categoría de Cliente", True)
mostrar_propiedades_inventario = st.sidebar.checkbox("Mostrar Gráfico: Propiedades en Inventario Mayor a 1", True)
mostrar_clientes_por_ciudad = st.sidebar.checkbox("Mostrar Gráfico: Número de Clientes por Ciudad", True)
mostrar_canal_comunicacion = st.sidebar.checkbox("Mostrar Gráfico: Canal de Comunicación y Número de Clientes", True)
mostrar_tipo_propiedad = st.sidebar.checkbox("Mostrar Gráfico: Tipo de Propiedad y Número de Clientes", True)

# Gráfico de Categoría de Cliente
if mostrar_categoria_cliente:
    st.subheader("Clientes Organizados por Categoría")
    fig_categoria_cliente = px.pie(df, names="Estado del Cliente", title="Distribución de Categoría de Cliente")
    st.plotly_chart(fig_categoria_cliente)

# Gráfico de Propiedades en Inventario Mayor a 1
if mostrar_propiedades_inventario:
    st.subheader("Clientes con Propiedades en Inventario Mayor a 1")
    fig_propiedades_inventario = px.histogram(df[df["Propiedades en Inventario"] > 1], x="Propiedades en Inventario", title="Número de Clientes con Propiedades en Inventario Mayor a 1")
    st.plotly_chart(fig_propiedades_inventario)

# Gráfico de Número de Clientes por Ciudad
if mostrar_clientes_por_ciudad:
    st.subheader("Número de Clientes por Ciudad")
    fig_clientes_por_ciudad = px.bar(df, x="Ciudad", title="Número de Clientes por Ciudad")
    st.plotly_chart(fig_clientes_por_ciudad)

# Gráfico de Canal de Comunicación
if mostrar_canal_comunicacion:
    st.subheader("Canal de Comunicación y Número de Clientes")
    fig_canal_comunicacion = px.bar(df, x="Canal de Comunicación", title="Número de Clientes por Canal de Comunicación")
    st.plotly_chart(fig_canal_comunicacion)


# Gráfico de Tipo de Propiedad
if mostrar_tipo_propiedad:
    st.subheader("Tipo de Propiedad y Número de Clientes")
    fig_tipo_propiedad = px.bar(df, x="Tipo de Propiedad", title="Número de Clientes por Tipo de Propiedad")
    st.plotly_chart(fig_tipo_propiedad)





