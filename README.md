![Texto alternativo](https://github.com/abritoj/Sistema-ML/blob/master/dataj.png)
# Sistema de recomendación

# **Introducción**

Para la comodidad del cliente se desarrollo un sistema de recomendación, este se realizo con machine learning basado en los datos de Yelp y Google maps,
este sistema usa el analisis de sentimientos en los comentarios de los usuarios, ademas dela calificaciones que estos de le dan a cada restaurantes, para recomendarle a nuestro cliente las caracteristicas de los restaurantes mejores recbidos en los diferentes estados, de esta manera el cliente puede tomar mejores deciciones y adaptar su menos a la gastronomia loca.

# **Tecnologías utilizadas**

Para el desarrollo de este sistema se utilizaron principalmente librerias python como pandas para el manejo de los datos, ntkl para el machine learning y el analisis de sentimeintos, tambien se utilizo streamlit para el diseño de la aplicacion web, por ultimo se utilizo render para deployar el modelo de manera efectiva.

## **Sistema de recomendación**

En este sistema de recomendacion se realizo un analisis de sentimiento seguido de una funcion. aqui se explicara de una manera detallada el codigo. 
La función realiza los siguientes pasos:

- Carga un archivo CSV con datos de negocios en un DataFrame de pandas.
- Filtra el DataFrame para incluir solo los negocios en el estado seleccionado.
- Inicializa un analizador de sentimientos de nltk para calcular el puntaje de sentimiento de cada revisión.
- Calcula el puntaje de sentimiento para cada revisión y lo agrega como una nueva columna en el DataFrame.
- Ordena el DataFrame por puntaje de sentimiento descendente y selecciona las 10 mejores ciudades.
- Devuelve una lista de las ciudades y categorías con las mejores revisiones.

# **Funcionamiento**
Al entrar en la pagina se le pedira al usuario que seleccione una de las 5 ciudades en la cuales se realizaro todo le estudio, una vez seleccionada se le dara una tabla con las principales ciudades y las categorias de los restaurantes que mas exito tienen en esa ciudad, como se muestra en la siguiente figura.
![Texto alternativo](https://github.com/abritoj/Sistema-ML/blob/master/datal.png)


