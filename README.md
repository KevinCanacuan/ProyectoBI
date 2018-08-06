# ESCUELA POLITÉCNICA NACIONAL- FACULTAD DE INGENIERÍA DE SISTEMAS - INTELIGENCIA DE NEGOCIOS

## I. TEMA
> Diseño e Implementación de un modelo de clasificación de sentimientos utilizando machine learning

## II.  INTEGRANTES:
    - Canacuán Kevin
    - Crespín Daniel

## III. OBJETIVOS
> El análisis de sentimiento utiliza el procesamiento de lenguaje natural, análisis de texto y lingüística computacional para identificar y extraer información subjetiva; por ende, está relacionado con la sociología en cuanto a las emociones y sentimientos ya que éstos son a menudo parte del proceso de toma de decisiones de una persona. En este sentido, se ha escogido realizar el análisis de opinión pública utilizando datos de Twitter de los países que participaron en el mundial de futbol 2018 por medio de los siguientes objetivos: 
> - Implementar e investigar el funcionamiento de un clasificador de sentimientos utilizando los algoritmos de aprendizaje vistos en clase y los datos recolectados de Twitter para identificar tendencias de opinión en los 20 países que participaron en el mundial a partir del 28 de junio del 2018.
> - Crear un clasificador de sentimiento en inglés utilizando datos extraídos de Twitter para minar opinión pública en los siguientes países: argentina, belgica, brasil, colombia, croacia, dinamarca, espania, francia, inglaterra, japon, mexico, panama, polonia, portugal, rusia, senegal, suecia, suiza, tunez, uruguay.
> - Identificar y seleccionar las herramientas necesarias para procesar y analizar datos provenientes de Twitter.

## IV. DESAROOLO DEL PROYECTO - FASES:
> * Adquisicion y Limpieza de Datos
> * Análisis de Resultados
> * Conclusiones y trabajo futuro

### Adquisición de Datos
> La Adquisición de Datos es realizada por medio de un script en lenguaje python que fue proporcionado en clase. Se coloca un link de un ejemplo, donde la ciudad analizada es Moscú - Rusia. Ejemplo:
(https://github.com/KevinCanacuan/ProyectoBI/blob/master/rusia-moscu.py). Si se desea analizar cualquier otra ciudad o zona del planeta, se debe colocar las nuevas coordenadas (formato CSV) en la parte final del script. Además, se debe cambiar el nombre de la base de datos (couchDB) en donde se requiere guardar la información.

### Pre-procesamiento de Datos
> Una vez ingresados todos los tweets a la base de datos, se procede a crear " vistas " dirigidas hacia cada una de las bases de datos. Estas vistas tendrán dos campos, el día(key) y el texto(value), que son generados por el siguiente script(javascript) dentro de la BD couchDB: (https://github.com/KevinCanacuan/ProyectoBI/blob/master/javascriptVista.txt). En este script, cada tweet a sido filtrado con la fecha " Julio 14 " y se han escogido el texto(sólo letras y números) del tweet escrito en lenguaje inglés.

### Limpieza de Datos
> Después de obtener las vistas de las bases de datos, se procede a escoger únicamente los tweets que traten sobre el mundial, como se puede observar en la parte inicial del siguiente script(python):
(https://github.com/KevinCanacuan/ProyectoBI/blob/master/Horas/Horas14JulioBelgica-Inglaterra.py)

> Cada vista, de la base couchDB, es llamada a través de la función " vistas "; después se ingresan los patrones que se desean limpiar del texto como: direcciones web, links, caracteres especiales, emoticones y una función denominada " give_emoji_free_text ", que también ayuda a limpiar el texto. Además, se ingresan los " hashtags ", referentes al mundial, que también sirven como filtros.

Nota: En el script analizado se trabaja con 3 países a la vez, pero se podría trabajar con un país a la vez.

### Análisis de Resultados
> En la parte intermedia del script analizado anteriormente, y una vez que el texto a sido limpiado, se toma como campo de análisis la hora (" key " de la vista generada en couchDB) y se procede a determinar el número de tweets por hora. Por último, los resultados serán mostrados en un gráfico de barras.

> Otro ejemplo de Análisis de datos se muestran en el siguiente script:
(https://github.com/KevinCanacuan/ProyectoBI/blob/master/Sentimientos/Sentimientos14JulioBelgica-Inglaterra.py)
EL funcionamiento es similar al script del análisis por horas, pero en este análisis se quiere llevar en conteo del número de tweets positivos, negativos y neutros referentes al mundial.
Para esto se utiliza el analizador de sentimientos de [textBlob](https://textblob.readthedocs.io/en/dev/). El cual determina la polaridad de un texto (" value " de la vista generada en couchDB). Y Los resultados serán mostrados en gráfico tipo pastel.

## V. CONCLUSIONES Y TRABAJO FUTURO






## VI. APÉNDICE: Instrucciones de Instalación y Funcionamiento
### HERRAMIENTAS
* [Python 2.7](https://www.python.org/) - Lenguaje utilizado.
* [ElasticSearch](https://www.elastic.co/) - Herramienta de Map - Reduce.
* [Kibana](https://www.elastic.co/products/kibana) - Presentación de Gráficos.
* Para poder acceder a Kibana, se ingresa a: [Kibana](http://localhost:9200) - Presentación de Gráficos.
