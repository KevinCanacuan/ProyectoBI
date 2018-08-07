from gmplot import gmplot
import re
import couchdb
import sys
import urllib2
import json
import textblob
import emoji
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from couchdb import view
from textblob import TextBlob


def vistas(url):
    req = urllib2.Request(url)
    f = urllib2.urlopen(req)
    d = json.loads(f.read())
    return d


inglaterra=vistas('http://127.0.0.1:5984/inglaterrafinal/_design/inglaterraMapa14/_view/inglaterraMapa14')
russia=vistas('http://127.0.0.1:5984/rusiafinal/_design/rusiaMapa14/_view/rusiaMapa14')
belgica=vistas('http://127.0.0.1:5984/belgicafinal/_design/belgicaMapa/_view/belgicaMapa')


patron1 = 'HTTPS(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
patron2 = '(WWW\.)(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
patron3 = "['\&\-\.\/()=:;]+"
emoticones ="["u"\U0001F600-\U0001F64F"u"\U0001F300-\U0001F5FF"u"\U0001F680-\U0001F6FF"u"\U0001F1E0-\U0001F1FF"u"\U0001F914""]+"
contadorhoras=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

hashtags={"World":"WORLDCUP","World2018":"WORLDCUP18","Rusia2018":"RUSIA2018","Rusia":"RUS","Ingla": "ENG"}
def limpiarEmojis(text):
    allchars = [str for str in text.decode('utf-8')]
    listaEmojis = [c for c in allchars if c in emoji.UNICODE_EMOJI]
    texto_limpio= ' '.join([str for str in text.decode('utf-8').split() if not any(i in str for i in listaEmojis)])
    return texto_limpio

listacoordenadas=[]
listaText=[]
coordenadasFinales=[]

def llenar(valor):
    for x in valor['rows']:
        coordenadas=x['key']
	textovistas=x['value']
        listacoordenadas.append(coordenadas)
	listaText.append(textovistas)
    return listacoordenadas,listaText

llenar(russia)
llenar(belgica)
llenar(inglaterra)

for q in range(len(listaText)):
	limpiador = re.compile(patron1+'|'+patron2+'|'+patron3+'|'+emoticones)
	texto=limpiador.sub('',listaText[q])
	textoLimpio=limpiarEmojis(texto.encode('utf8'))	
	if hashtags["World"] in textoLimpio or hashtags["World2018"] in textoLimpio or hashtags["Rusia2018"] in textoLimpio or	hashtags["Ingla"] in textoLimpio:
		coordenadasFinales.append(listacoordenadas[q])
	


# Place map

gmap = gmplot.GoogleMapPlotter(45.1667000,15.5000000,6.5)


# Scatter points
longitud,latitud = zip(*coordenadasFinales)
gmap.heatmap(latitud,longitud)

# Draw
gmap.draw("BelgicavsInglaterra.html")
