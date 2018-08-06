import re
import couchdb
import sys
import urllib2
import json
import textblob
import emoji
from couchdb import view
from textblob import TextBlob
import matplotlib.pyplot as plt


def vistas(url):
    req = urllib2.Request(url)
    f = urllib2.urlopen(req)
    d = json.loads(f.read())
    return d

russia=vistas('http://127.0.0.1:5984/rusiafinal/_design/rusiaSentimientos7/_view/rusiaSentimientos7')
suecia=vistas('http://127.0.0.1:5984/sueciafinal/_design/sueciaSentimientos7/_view/sueciaSentimientos7')
inglaterra=vistas('http://127.0.0.1:5984/inglaterrafinal/_design/inglaterraSentimientos7/_view/inglaterraSentimientos7')


patron1 = 'HTTPS(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
patron2 = '(WWW\.)(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
patron3 = "['\&\-\.\/()=:;]+"
emoticones ="["u"\U0001F600-\U0001F64F"u"\U0001F300-\U0001F5FF"u"\U0001F680-\U0001F6FF"u"\U0001F1E0-\U0001F1FF"u"\U0001F914""]+"
stmiento=""
contadorpos=0
contadorneg=0
contadorneu=0

hashtags={"World":"WORLDCUP","World2018":"WORLDCUP18","Rusia2018":"RUSIA2018","Rusia":"RUS","Suecia":"SWE","Ingla": "ENG"}
def give_emoji_free_text(text):
    allchars = [str for str in text.decode('utf-8')]
    emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
    clean_text = ' '.join([str for str in text.decode('utf-8').split() if not any(i in str for i in emoji_list)])
    return clean_text


listaText=[]

for x in suecia['rows']:
    text=x['value']
    listaText.append(text)

for y in russia['rows']:
    text=y['value']
    listaText.append(text)

for z in inglaterra['rows']:
    text=z['value']
    listaText.append(text)



print len(listaText)

for x in range(len(listaText)):
	limpiador = re.compile(patron1+'|'+patron2+'|'+patron3+'|'+emoticones)
	texto=limpiador.sub('',listaText[x])
	textoLimpio=give_emoji_free_text(texto.encode('utf8'))
	if hashtags["World"] in textoLimpio or hashtags["World2018"] in textoLimpio or hashtags["Rusia2018"] in textoLimpio or hashtags["Rusia"] in textoLimpio or hashtags["Suecia"] in textoLimpio or hashtags["Ingla"] in textoLimpio:
		testimonial=TextBlob(textoLimpio)
		polaridad=testimonial.sentiment.polarity
		if  polaridad > 0:
			stmiento="pos"
			contadorpos=contadorpos+1
		elif polaridad == 0:
			stmiento="neu"
			contadorneu=contadorneu+1
		else:
			stmiento="neg"
			contadorneg=contadorneg+1
	stmiento="" 	
	
print(contadorpos,contadorneg,contadorneu)

total =0
total = float(contadorpos) + float(contadorneu) + float(contadorneg)
posi= float("{0:.2f}".format(contadorpos/total))
nega= float("{0:.2f}".format(contadorneg/total))
neut= float("{0:.2f}".format(contadorneu/total))
print("Positivo: "+str(posi)+"\nNegativo: "+str(nega)+"\nNeutral: "+str(neut))

labels = 'Positivos ', 'Negativos', 'Neutrales'
fracs = [contadorpos,contadorneg,contadorneu]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0)
plt.pie(fracs, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()
