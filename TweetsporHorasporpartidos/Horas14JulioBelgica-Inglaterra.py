
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

russia=vistas('http://127.0.0.1:5984/rusiafinal/_design/rusiaSentimientos14/_view/rusiaSentimientos14')
belgica=vistas('http://127.0.0.1:5984/belgicafinal/_design/belgicaSentimientos14/_view/belgicaSentimientos14')
inglaterra=vistas('http://127.0.0.1:5984/inglaterrafinal/_design/inglaterraSentimientos14/_view/inglaterraSentimientos14')

patron1 = 'HTTPS(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
patron2 = '(WWW\.)(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
patron3 = "['\&\-\.\/()=:;]+"
emoticones ="["u"\U0001F600-\U0001F64F"u"\U0001F300-\U0001F5FF"u"\U0001F680-\U0001F6FF"u"\U0001F1E0-\U0001F1FF"u"\U0001F914""]+"
stmiento=""
contadorhoras=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

hashtags={"World":"WORLDCUP","World2018":"WORLDCUP18","Rusia2018":"RUSIA2018","Rusia":"RUS","Belgica": "BEL", "Ingla": "ENG"}
def limpiarEmojis(text):
    allchars = [str for str in text.decode('utf-8')]
    listaEmojis = [c for c in allchars if c in emoji.UNICODE_EMOJI]
    texto_limpio= ' '.join([str for str in text.decode('utf-8').split() if not any(i in str for i in listaEmojis)])
    return texto_limpio

listaHora=[]
listaText=[]

for x in belgica['rows']:
    hora=x['key']
    text=x['value']
    listaHora.append(hora)
    listaText.append(text)

for y in russia['rows']:
    hora=y['key']
    text=y['value']
    listaHora.append(hora)
    listaText.append(text)

for z in inglaterra['rows']:
    hora=z['key']
    text=z['value']
    listaHora.append(hora)
    listaText.append(text)



for q in range(len(listaText)):
	limpiador = re.compile(patron1+'|'+patron2+'|'+patron3+'|'+emoticones)
	texto=limpiador.sub('',listaText[q])
	textoLimpio=limpiarEmojis(texto.encode('utf8'))	
	if hashtags["World"] in textoLimpio or hashtags["World2018"] in textoLimpio or hashtags["Rusia2018"] in textoLimpio or hashtags      ["Rusia"] in textoLimpio or hashtags["Belgica"] in textoLimpio or hashtags["Ingla"] in textoLimpio:
		if "07" in listaHora[q]:
			contadorhoras[0]=contadorhoras[0]+1
		elif "08" in listaHora[q]:
			contadorhoras[1]=contadorhoras[1]+1
		elif "09" in listaHora[q]:
			contadorhoras[2]=contadorhoras[2]+1
		elif "10" in listaHora[q]:
			contadorhoras[3]=contadorhoras[3]+1
		elif "11" in listaHora[q]:
			contadorhoras[4]=contadorhoras[4]+1
		elif "12" in listaHora[q]:
			contadorhoras[5]=contadorhoras[5]+1	
		elif "13" in listaHora[q]:
			contadorhoras[6]=contadorhoras[6]+1
		elif "14" in listaHora[q]:
			contadorhoras[7]=contadorhoras[7]+1		
		elif "15" in listaHora[q]:
			contadorhoras[8]=contadorhoras[8]+1				
		elif "16" in listaHora[q]:
			contadorhoras[9]=contadorhoras[9]+1
		elif "17" in listaHora[q]:
			contadorhoras[10]=contadorhoras[10]+1
		elif "18" in listaHora[q]:
			contadorhoras[11]=contadorhoras[11]+1
		elif "19" in listaHora[q]:
			contadorhoras[12]=contadorhoras[12]+1
		elif "20" in listaHora[q]:
			contadorhoras[13]=contadorhoras[13]+1
		elif "21" in listaHora[q]:
			contadorhoras[14]=contadorhoras[14]+1
		elif "22" in listaHora[q]:
			contadorhoras[15]=contadorhoras[15]+1
		elif "23" in listaHora[q]:
			contadorhoras[16]=contadorhoras[16]+1
		elif "24" in listaHora[q]:
			contadorhoras[17]=contadorhoras[17]+1

print contadorhoras
dias=('7am','8am','9am','10am','11am','12pm','13pm','14pm','15pm','16pm','17pm','18pm','19pm','20pm','21pm','22pm','23pm','24pm')
y=np.arange(len(dias))
tweets=contadorhoras
plt.bar(y,tweets,align='center',alpha=0.6)
plt.xticks(y,dias)
plt.xlabel('Horas del dia')
plt.ylabel('Cantidad de tweets')
plt.title('Tweets por hora Belgica-Inglaterra 14 de Julio')
plt.show()

