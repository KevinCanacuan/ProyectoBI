
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
argentina=vistas('http://127.0.0.1:5984/argentinafinal/_design/argentinaporFecha/_view/argentinaporFecha')
belgica=vistas('http://127.0.0.1:5984/belgicafinal/_design/belgicaporFecha/_view/belgicaporFecha')
brasil=vistas('http://127.0.0.1:5984/brasilfinal/_design/brasilporFecha/_view/brasilporFecha')
colombia=vistas('http://127.0.0.1:5984/colombiafinal/_design/colombiaporFecha/_view/colombiaporFecha')
croacia=vistas('http://127.0.0.1:5984/croaciafinal/_design/croaciaporFecha/_view/croaciaporFecha')
dinamarca=vistas('http://127.0.0.1:5984/dinamarcafinal/_design/dinamarcaporFecha/_view/dinamarcaporFecha')
espania=vistas('http://127.0.0.1:5984/espanafinal/_design/espanaporFecha/_view/espanaporFecha')
francia=vistas('http://127.0.0.1:5984/franciafinal/_design/franciaporFecha/_view/franciaporFecha')
inglaterra=vistas('http://127.0.0.1:5984/inglaterrafinal/_design/inglaterraporFecha/_view/inglaterraporFecha')
japon=vistas('http://127.0.0.1:5984/japonfinal/_design/japonporFecha/_view/japonporFecha')
mexico=vistas('http://127.0.0.1:5984/mexicofinal/_design/mexicoporFecha/_view/mexicoporFecha')
panama=vistas('http://127.0.0.1:5984/panamafinal/_design/panamaporFecha/_view/panamaporFecha')
polonia=vistas('http://127.0.0.1:5984/poloniafinal/_design/poloniaporFecha/_view/poloniaporFecha')
portugal=vistas('http://127.0.0.1:5984/portugalfinal/_design/portugalporFecha/_view/portugalporFecha')
russia=vistas('http://127.0.0.1:5984/rusiafinal/_design/rusiaporFecha/_view/rusiaporFecha')
senegal=vistas('http://127.0.0.1:5984/senegalfinal/_design/senegalporFecha/_view/senegalporFecha')
suecia=vistas('http://127.0.0.1:5984/sueciafinal/_design/sueciaporFecha/_view/sueciaporFecha')
suiza=vistas('http://127.0.0.1:5984/suizafinal/_design/suizaporFecha/_view/suizaporFecha')
tunez=vistas('http://127.0.0.1:5984/tunezfinal/_design/tunezporFecha/_view/tunezporFecha')
uruguay=vistas('http://127.0.0.1:5984/uruguayfinal/_design/uruguayporFecha/_view/uruguayporFecha')

contadorFecha=[0,0,0,0,0,0,0,0,0,0,0]

patron1 = 'HTTPS(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
patron2 = '(WWW\.)(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
patron3 = "['\&\-\.\/()=:;]+"
emoticones ="["u"\U0001F600-\U0001F64F"u"\U0001F300-\U0001F5FF"u"\U0001F680-\U0001F6FF"u"\U0001F1E0-\U0001F1FF"u"\U0001F914""]+"

hashtags={"World":"WORLDCUP","World2018":"WORLDCUP18","Rusia2018":"RUSIA2018","Argentina":"ARG","Belgica":"BEL","Brasil":"BRA","Colombia":"COL","Croacia":"CRO","Dinamarca":"DEN","Ingla": "ENG","Espana":"ESP","Francia":"FRA","Alemania":"GER","Japon":"JPN","Mexico":"MEX","Panama":"PAN","Polonia":"POL","Portugal":"POR","Russia":"RUS","Senegal":"SEN","Suiza":"SUI","Suecia":"SWE","Tunez":"TUN","Uruguay":"URU"}

def limpiarEmojis(text):
    allchars = [str for str in text.decode('utf-8')]
    listaEmojis = [c for c in allchars if c in emoji.UNICODE_EMOJI]
    texto_limpio= ' '.join([str for str in text.decode('utf-8').split() if not any(i in str for i in listaEmojis)])
    return texto_limpio

listaFecha=[]
listaText=[]

def llenar(valor):
    for x in valor['rows']:
        fecha=x['key']
	textovistas=x['value']
        listaFecha.append(fecha)
	listaText.append(textovistas)
    return listaFecha,listaText

llenar(argentina)
llenar(belgica)
llenar(brasil)
llenar(croacia)
llenar(colombia)
llenar(dinamarca)
llenar(espania)
llenar(francia)
llenar(inglaterra)
llenar(japon)
llenar(mexico)
llenar(panama)
llenar(polonia)
llenar(portugal)
llenar(russia)
llenar(senegal)
llenar(suecia)
llenar(suiza)
llenar(tunez)
llenar(uruguay)

for q in range(len(listaText)):
	limpiador = re.compile(patron1+'|'+patron2+'|'+patron3+'|'+emoticones)
	texto=limpiador.sub('',listaText[q])
	textoLimpio=limpiarEmojis(texto.encode('utf8'))	
	if hashtags["World"] in textoLimpio or hashtags["World2018"] in textoLimpio or hashtags["Rusia2018"] in textoLimpio or hashtags["Argentina"] in textoLimpio or hashtags["Belgica"] in textoLimpio or hashtags['Brasil'] in textoLimpio or hashtags['Colombia'] in textoLimpio or hashtags['Croacia'] in textoLimpio or hashtags['Dinamarca'] or hashtags['Ingla'] in textoLimpio or hashtags['Espana'] in textoLimpio or hashtags['Francia'] in textoLimpio or hashtags['Alemania'] in textoLimpio or hashtags['Japon'] in textoLimpio or hashtags['Mexico'] in textoLimpio or hashtags['Panama'] in textoLimpio or hashtags['Polonia'] in textoLimpio or hashtags['Portugal'] in textoLimpio or hashtags["Rusia"] in textoLimpio or hashtags['Senegal'] in textoLimpio or hashtags['Suiza'] in textoLimpio or hashtags["Suecia"] in textoLimpio or hashtags['Tunez'] in textoLimpio or hashtags['Uruguay'] in textoLimpio:
 		if "Jun 28" in listaFecha[q]:
			contadorFecha[0]=contadorFecha[0]+1
		elif "Jun 30" in listaFecha[q]:
			contadorFecha[1]=contadorFecha[1]+1
		elif "Jul 01" in listaFecha[q]:
			contadorFecha[2]=contadorFecha[2]+1
		elif "Jul 02" in listaFecha[q]:
			contadorFecha[3]=contadorFecha[3]+1
		elif "Jul 03" in listaFecha[q]:
			contadorFecha[4]=contadorFecha[4]+1
		elif "Jul 06" in listaFecha[q]:
			contadorFecha[5]=contadorFecha[5]+1
		elif "Jul 07" in listaFecha[q]:
			contadorFecha[6]=contadorFecha[6]+1	
		elif "Jul 10" in listaFecha[q]:
			contadorFecha[7]=contadorFecha[7]+1
		elif "Jul 11" in listaFecha[q]:
			contadorFecha[8]=contadorFecha[8]+1		
		elif "Jul 14" in listaFecha[q]:
			contadorFecha[9]=contadorFecha[9]+1			
		elif "Jul 15" in listaFecha[q]:
			contadorFecha[10]=contadorFecha[10]+1
		
dias=('28Jun','30Jun','01Jul','02Jul','03Jul','06Jul','07Jul','10Jul','11Jul','14Jul','15Jul')
y=np.arange(len(dias))
print contadorFecha
tweets=contadorFecha
plt.bar(y,tweets,align='center',alpha=1)
plt.xticks(y,dias,fontsize=8)
plt.xlabel('Fechas',fontsize=10)
plt.ylabel('Cantidad de tweets', fontsize=10)
plt.title('Tweets por Fecha')
plt.show()


