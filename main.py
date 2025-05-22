# Librerias
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt
from model import predict_iris
from PIL import Image
import datetime

# Configurar pagina
st.set_page_config(page_title="Streamlit Mega Demo", layout="wide")

# 🎨 Ponemos el fondo lila
st.markdown(
    """
    <style>
    /* Fondo general */
    .stApp {
        background-color: #F3E6F5;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Empezamos con el titulo
st.title("🚀 Streamlit Mega Demo")

# Sidebar Widgets
sidebar_option = st.sidebar.radio("Elige una opción: ", ["Inicio","Multimedia","Datos", "Visualizaciones","Clasificador Iris","Celebremos"])
#st.write(sidebar_option)--> coge el valor de la opción seleccionada

# --- Inicio ---
if sidebar_option == "Inicio":
    st.header("Widgets básicos")

    with st.expander("Controles de entrada"):
        if st.button("Haz click"):
            st.write("Bienvenido")
        if st.checkbox("Ok, estoy de acuerdo"):
             st.checkbox("muy bien hecho")
        st.radio("Elige una opción", ["Manzana", "Naranja"])
        letra_elegida = st.selectbox("Elige una opción", ["A", "B", "C", "D", "E"])
        st.multiselect("Selecciones múltiples", ["A", "B", "C", "D", "E"])
        st.slider("Rango de valor", 0, 100, 50) # Donde se muestra por defecto
        edad = st.number_input("Edad", min_value = 0, max_value = 120, value = 18) # no hace falta poner el nombre de los argumentos si se mantiene el orden común
        st.text_input("Pon tu nombre")
        st.text_area("Comentarios")
        st.date_input("Fecha")
        st.time_input("Hora")
        st.file_uploader("Sube un selfie")
        mi_color = st.color_picker("Elige un color") # poniendo el mi_loquesea delante se queda guardado
        st.write(mi_color)

    with st.expander("Widgets visuales"):
        st.metric("Ventas", value = "1.200$", delta = "+5%")
        st.progress(70)
        with st.spinner("Cargando..."):
             st.success("Listo!!!!")


# --- Multimedia ---
elif sidebar_option == "Multimedia":
    st.subheader("Multimedia")
    st.markdown("Imagen")
    st.image(Image.open("assets/iris.jpg"), caption="Iris")

    st.markdown("Video")
    st.video("https://www.youtube.com/watch?v=3Yy-GC4WMRw")

    st.markdown("Audio")
    st.audio("assets/gatito.mp3")
    st.audio("assets/gatito2.mp3")

    camera = st.camera_input("Toma una foto")
    if camera:
        st.image(camera, caption="Tu selfie")
       
    st.code("X_train,X_test,y_train,y_test = train_test_split(X,y)")
    st.latex(r"E = mc^2")

# --- Datos ---
elif sidebar_option == "Datos":
    st.subheader("Dataset")
    df = pd.read_csv("data/sample_data.csv")
    st.dataframe(df)

    df_iris = pd.read_csv("data/iris.csv")
    st.dataframe(df_iris)

    st.write(df_iris.describe())

    st.markdown("FILTRADOR")
    categoria = st.selectbox("Qué categoría quieres ver", df.category.unique())
    df_filtrado = df[df.category == categoria]
    st.dataframe(df_filtrado)

# --- Visualizaciones ---
elif sidebar_option == "Visualizaciones":
    st.subheader("Visualizaciones")
    df = pd.read_csv("data/sample_data.csv")
    
    #st.markdown("Gráficos rápidos")
    #st.line_chart(df["value"]) # NO TIENE NINGÚN SENTIDO(MAL HECHO!!!)
    #st.area_chart(df["value"])
    #st.bar_chart(df["target_name"]) # NO TIENE NINGÚN SENTIDO(MAL HECHO!!!)

    st.markdown("Gráficos rápidos")

    fig, ax = plt.subplots()
    ax.plot(df["id"], df["value"], marker='o')
    st.pyplot(fig)


    st.subheader("Plotly")
    fig_plotly = px.bar(df, x="category", y="value", color="category")
    st.plotly_chart(fig_plotly)


    st.subheader("Altair")
    chart = alt.Chart(df).mark_line().encode(x='id', y='value', color='category')
    st.altair_chart(chart, use_container_width=True)

    st.subheader("Altair Iris")
    df_iris = pd.read_csv("data/iris.csv")
    st.dataframe(df_iris)
    st.write(df_iris.columns)

    df_iris_media = df_iris.groupby("target_name")["sepal length (cm)"].mean().reset_index()

    st.dataframe(df_iris_media)

    chart = alt.Chart(df_iris_media).mark_bar().encode(x="target_name",y="sepal length (cm)")
    st.altair_chart(chart, use_container_width=True)

# --- Clasificador Iris ---
if sidebar_option == "Clasificador Iris":

    st.subheader("Clasificador de flores Iris")
    st.write("Introduce las caracteristicas de una flor para predecir")
    
    sepal_lenght = st.number_input("Largo del sépalo (cm)", min_value=0.0, max_value=10.0, value=5.0)
    sepal_width = st.number_input("Ancho del sépalo (cm)", min_value=0.0, max_value=10.0, value=3.0)
    petal_length = st.number_input("Largo del pétalo (cm)", min_value=0.0, max_value=10.0, value=1.0)
    petal_width = st.number_input("Ancho del pétalo (cm)", min_value=0.0, max_value=10.0, value=0.2)
    st.toast("Gracias por participar")

    if st.button("Dime que especie es"):
        features = [sepal_lenght, sepal_width, petal_length, petal_width]
        prediction, proba, target_names = predict_iris(features)
        especie = target_names[prediction]
        st.success(f"La especie es: {especie}")
        st.write("Probabilidades:")
        st.bar_chart(proba)

# --- Celebremos ---
if sidebar_option == "Celebremos":
    if st.button("Celebrar la vuelta al cole"):
        st.balloons()
        st.snow()
        st.toast("Buenas noticias, APROBADO!!!")