
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

francia=vistas('http://127.0.0.1:5984/franciafinal/_design/franciaporIdioma15Julio/_view/franciaporIdioma15Julio')
croacia=vistas('http://127.0.0.1:5984/croaciafinal/_design/croaciaporIdioma15Julio/_view/croaciaporIdioma15Julio')
rusia=vistas('http://127.0.0.1:5984/rusiafinal/_design/rusiaporIdioma15Julio/_view/rusiaporIdioma15Julio')

contadoringles=0
contadorespaniol=0
contadorruso=0
contadorportuges=0
contadorsueco=0
contadorcroata=0
contadorarabe=0
contadorfrances=0
contadorchino=0
contadoraleman=0
contadorotros=0

listaIdiomas=[]

def llenar(valor):
    for x in valor['rows']:
        idioma=x['key']
        listaIdiomas.append(idioma)
    return listaIdiomas


llenar(francia)
llenar(croacia)
llenar(rusia)

for q in range(len(listaIdiomas)):
		if "en" in listaIdiomas[q]:
			contadoringles=contadoringles+1
		elif "es" in listaIdiomas[q]:
			contadorespaniol=contadorespaniol+1
		elif "pt" in listaIdiomas[q]:
			contadorportuges=contadorportuges+1
		elif "ru" in listaIdiomas[q]:
			contadorruso=contadorruso+1
		elif "sv" in listaIdiomas[q]:
			contadorsueco=contadorsueco+1
		elif "hr" in listaIdiomas[q]:
			contadorcroata=contadorcroata+1	
		elif "zh" in listaIdiomas[q]:
			contadorchino=contadorchino+1
		elif "fr" in listaIdiomas[q]:
			contadorfrances=contadorfrances+1		
		elif "ar" in listaIdiomas[q]:
			contadorarabe=contadorarabe+1				
		elif "de" in listaIdiomas[q]:
			contadoraleman=contadoraleman+1
		else:
			contadorotros=contadorotros+1

dias=('EN','ES','POR','RU','SUE','CRO','CN','FRA','ARAB','DEU','OTROS')
y=np.arange(len(dias))
tweets=[contadoringles,contadorespaniol,contadorportuges,contadorruso,contadorsueco,contadorcroata,contadorchino,contadorfrances,contadorarabe,contadoraleman,contadorotros]
plt.bar(y,tweets,align='center',alpha=1)
plt.xticks(y,dias,fontsize=8)
plt.xlabel('Idiomas',fontsize=10)
plt.ylabel('Cantidad de tweets', fontsize=10)
plt.title('Tweets por Idiomas FranciavsCroacia (15 de Julio)')
plt.show()


