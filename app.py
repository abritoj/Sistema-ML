import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import streamlit as st
nltk.download('vader_lexicon')
def obtener_ciudades_con_mejor_review(estado):
    # Cargar el DataFrame con los datos de los negocios
    df = pd.read_csv('datamodelo5estadossinsentimiento.csv')  # Reemplaza 'ruta_del_archivo.csv' con la ruta real de tu archivo de datos
    
    # Filtrar el DataFrame por el estado seleccionado
    df_estado = df[df['state'].str.lower() == estado.lower()]
    
    # Inicializar el analizador de sentimientos
    sia = SentimentIntensityAnalyzer()
    
    # Calcular el puntaje de sentimiento para cada revisión
    df_estado['sentiment_score'] = df_estado['review'].apply(lambda x: sia.polarity_scores(x)['compound'])
    
    # Ordenar el DataFrame por puntaje de sentimiento descendente y seleccionar las 10 mejores ciudades
    df_top_ciudades = df_estado.sort_values(by='sentiment_score', ascending=False).head(10)
    
    # Obtener una lista de las ciudades y categorías con las mejores revisiones
    lista_ciudades_categorias = df_top_ciudades[['city', 'categories']].values.tolist()
    
    return lista_ciudades_categorias

# Configuración de la página
st.image('dataj.png')  # Reemplaza 'ruta_de_la_imagen.jpg' con la ruta real de tu imagen
st.title("Sistema de Recomendación")

# Obtener la selección del estado
estado_seleccionado = st.selectbox("Selecciona un estado", ['NY', 'CA', 'HI', 'NV', 'FL'])

# Obtener las ciudades con las mejores revisiones
lista_ciudades_categorias = obtener_ciudades_con_mejor_review(estado_seleccionado)

# Mostrar los resultados en una tabla
st.subheader("Ciudades con las Mejores Revisiones")
df_resultados = pd.DataFrame(lista_ciudades_categorias, columns=['Ciudad', 'Categorías'])
st.table(df_resultados)

