# ESCUELA POLITÉCNICA NACIONAL- FACULTAD DE INGENIERÍA DE SISTEMAS - INTELIGENCIA DE NEGOCIOS

## I. TEMA
> Diseño e Implementación de un modelo de clasificación de sentimientos utilizando machine learning

## II.  INTEGRANTES:
    - Canacuán Kevin
    - Crespín Daniel

## III. OBJETIVOS
> El análisis de sentimiento utiliza el procesamiento de lenguaje natural, análisis de texto y lingüística computacional para identificar y extraer información subjetiva; por ende, está relacionado con la sociología en cuanto a las emociones y sentimientos ya que éstos son a menudo parte del proceso de toma de decisiones de una persona. En este sentido, se ha escogido realizar el análisis de opinión pública utilizando datos de Twitter de los países que participaron en el mundial de futbol 2018 por medio de los siguientes objetivos: 
> - Implementar e investigar el funcionamiento de un clasificador de sentimientos utilizando los algoritmos de aprendizaje vistos en clase y los datos recolectados de Twitter para identificar tendencias de opinión en los 20 países que participaron en el mundial a partir del 28 de junio del 2018.
> - Crear un clasificador de sentimiento en inglés utilizando datos extraídos de Twitter para minar opinión pública en los siguientes países: argentina, Bélgica, Brasil, Colombia, Croacia, Dinamarca, España, Francia, Inglaterra, Japón, México, Panamá, Polonia, Portugal, Rusia, Senegal, Suecia, suiza, Túnez, Uruguay.
> - Identificar y seleccionar las herramientas necesarias para procesar y analizar datos provenientes de Twitter.

## IV. DESARROLLO DEL PROYECTO - FASES:
> * Adquisición y Limpieza de Datos
> * Análisis de Resultados
> * Conclusiones y trabajo futuro

### Adquisición de Datos
> La Adquisición de Datos es realizada por medio de un script en lenguaje Python que fue proporcionado en clase. En el siguiente enlace se analiza la ciudad de Moscú - Rusia. Ejemplo:
(https://github.com/KevinCanacuan/ProyectoBI/blob/master/rusia-moscu.py). Si se desea analizar cualquier otra ciudad o zona del planeta, se debe colocar las nuevas coordenadas (formato CSV) en la parte final del script. Además, se debe cambiar el nombre de la base de datos (couchDB) en donde se requiere guardar la información.

### Preprocesamiento de Datos
> Una vez ingresados todos los tweets a la base de datos, se procede a crear " vistas " dirigidas hacia cada una de las bases de datos. Estas vistas tendrán dos campos, el día(key) y el texto(value), que son generados por el siguiente script(javascript) dentro de la BD couchDB: (https://github.com/KevinCanacuan/ProyectoBI/blob/master/javascriptVista.txt). En este script, cada tweet ha sido filtrado con la fecha " Julio 14 " y se han escogido el texto (sólo letras y números) del tweet escrito en lenguaje inglés.

### Limpieza de Datos
> Después de obtener las vistas de las bases de datos, se procede a escoger únicamente los tweets que traten sobre el mundial, como se puede observar en la parte inicial del siguiente script (Python):
(https://github.com/KevinCanacuan/ProyectoBI/blob/master/Horas/Horas14JulioBelgica-Inglaterra.py)

> Cada vista, de la base couchDB, es llamada a través de la función " vistas "; después se ingresan los patrones que se desean limpiar del texto como: direcciones web, links, caracteres especiales, emoticones y una función denominada " give_emoji_free_text / limpiarEmojis ", que también ayuda a limpiar el texto. Además, se ingresan los " hashtags ", referentes al mundial, que también sirven como filtros.

Nota: En el script analizado se trabaja con 3 países a la vez, pero se podría trabajar con un país a la vez.

### Análisis de Resultados
> En la parte intermedia del script analizado anteriormente, y una vez que el texto ha sido limpiado, se toma como campo de análisis la hora (" key " de la vista generada en couchDB) y se procede a determinar el número de tweets por hora. Por último, los resultados serán mostrados en un gráfico de barras.

> Otro ejemplo de Análisis de datos se muestran en el siguiente script:
(https://github.com/KevinCanacuan/ProyectoBI/blob/master/Sentimientos/Sentimientos14JulioBelgica-Inglaterra.py)
EL funcionamiento es similar al script del análisis por horas, pero en este análisis se quiere llevar en conteo del número de tweets positivos, negativos y neutros referentes al mundial.
Para esto se utiliza el analizador de sentimientos de [textBlob](https://textblob.readthedocs.io/en/dev/). El cual determina la polaridad de un texto (" value " de la vista generada en couchDB). Y Los resultados serán mostrados en gráfico tipo pastel.

Nota: Anteriormente, se detallan 2 formas de análisis de los datos obtenidos (sentimientos y horas), en las otras carpetas del Repositorio se tienen otros tipos de análisis hacia los datos. Todos los scripts funcionan de una manera similar: primero se cargan las vistas filtradas según el análisis requerido, luego se limpia el texto de las mismas y por último se hace el análisis que se desee.

## V. CONCLUSIONES Y TRABAJO FUTURO
> Una vez analizados los resultados, se observa que el Mundial de Fútbol Rusia 2018 fue una gran atracción tanto para los asistentes al evento y los países participantes. Aunque la diferencia de la cantidad de tweets tomados por país es muy notoria, se puede observar que la tendencia se mantiene para los países analizados (Bélgica, Inglaterra, Francia, Croacia, Rusia, Suecia).

> Por otro lado, en la carpeta [Imagenes](https://github.com/KevinCanacuan/ProyectoBI/tree/master/Imagenes) se encuentran capturas de los resultados de los distintos tipos de análisis realizados a los países antes mencionados.

> Como trabajo futuro se plantea lo siguiente:
> - Si el proyecto de asignatura sigue con el mismo tema, la toma de coordenadas de las zonas para capturar los tweets debería mejorarse, debido a que a veces se tomaba tweets de otro país cercano o de otras zonas.
> - Analizar cuánto dinero gastaron los asistentes al mundial.
> - Analizar el porcentaje de asistentes que no tengan a su selección en competición.
> - Verificar que los demás grupos también tengan resultados similares a los obtenidos, para de cierta manera asegurarnos que el análisis presentado fue correcto.

## VI. APÉNDICE: Instrucciones de Instalación y Funcionamiento
> El presente Proyecto no necesita de instalación previa para su funcionamiento, pero si requiere de cierto programas y herramientas para su funcionamiento:
> - Base de Datos couchDB
> - Navegador Web
> - Librerías de Python: json, textblob, emoji, matplotlib.pyplot
