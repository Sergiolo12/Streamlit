# Página Web Básica con Streamlit en Python

Este repositorio contiene el código fuente de una aplicación web interactiva básica creada con la librería Streamlit en Python. Streamlit permite convertir scripts de Python en aplicaciones web compartibles en cuestión de segundos, ideal para prototipos rápidos, visualización de datos y demostraciones de modelos de machine learning.

## Descripción de la Aplicación

Esta aplicación es un ejemplo sencillo que demuestra las funcionalidades fundamentales de Streamlit. Típicamente, una aplicación básica de Streamlit puede incluir elementos como:

* **Texto y Títulos:** Mostrar texto informativo, títulos y subtítulos.
* **Entrada de Usuario:** Permitir al usuario interactuar a través de widgets como botones, sliders, selectores y campos de texto.
* **Visualización de Datos:** Mostrar gráficos, tablas y otros elementos visuales generados con librerías de Python como Matplotlib, Seaborn o Pandas.
* **Mostrar Resultados:** Presentar los resultados del procesamiento o análisis basado en la entrada del usuario.

Este ejemplo específico puede incluir cualquiera de estas funcionalidades básicas para ilustrar cómo construir una interfaz de usuario interactiva con Streamlit utilizando código Python puro.

## Estructura del Repositorio

├── README.md
└── app.py              # El script principal de Streamlit en Python
└── requirements.txt    # Lista de dependencias de Python


* `README.md`: Este archivo, que proporciona información general sobre la aplicación.
* `app.py`: El script de Python que contiene el código de la aplicación Streamlit. Aquí se define la interfaz de usuario y la lógica de la aplicación.
* `requirements.txt`: Un archivo que lista las librerías de Python necesarias para ejecutar la aplicación (principalmente `streamlit`).

## Cómo Ejecutar la Aplicación

1.  **Clonar el repositorio (opcional):**
    Si tienes este código en un repositorio de Git, clónalo a tu máquina local:
    ```bash
    git clone [https://github.com/sindresorhus/del](https://github.com/sindresorhus/del)
    cd [nombre del repositorio]
    ```

2.  **Crear y activar un entorno virtual (recomendado):**
    Es una buena práctica crear un entorno virtual para aislar las dependencias del proyecto:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/macOS
    venv\Scripts\activate  # En Windows
    ```

3.  **Instalar las dependencias:**
    Asegúrate de tener Streamlit instalado. Si no lo tienes o si hay otras dependencias listadas en `requirements.txt`, instálalas usando pip:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecutar la aplicación Streamlit:**
    Navega al directorio donde se encuentra el archivo `app.py` en tu terminal y ejecuta el siguiente comando:
    ```bash
    streamlit run app.py
    ```
    Esto abrirá automáticamente una nueva pestaña en tu navegador web con la aplicación Streamlit en ejecución.

## Contenido del Script `app.py` (Ejemplo)

El archivo `app.py` contendrá el código Python que define la interfaz de usuario de la aplicación. Aquí tienes un ejemplo básico:

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Mi Primera Aplicación Streamlit")

# Introducción
st.write("Esta es una aplicación web básica creada con Streamlit.")

# Entrada de texto del usuario
nombre = st.text_input("Introduce tu nombre:")
if nombre:
    st.write(f"¡Hola, {nombre}!")

# Botón
if st.button("Haz clic aquí"):
    st.write("¡El botón ha sido presionado!")

# Slider
edad = st.slider("Selecciona tu edad:", 0, 100, 25)
st.write(f"Tu edad seleccionada es: {edad}")

# Ejemplo de visualización de datos
data = {'fruta': ['manzana', 'banana', 'cereza'],
        'cantidad': [10, 20, 15]}
df = pd.DataFrame(data)

st.subheader("Ventas de Frutas")
st.dataframe(df)

plt.figure(figsize=(6, 4))
plt.bar(df['fruta'], df['cantidad'])
plt.xlabel("Fruta")
plt.ylabel("Cantidad")
plt.title("Gráfico de Ventas de Frutas")
st.pyplot(plt)
