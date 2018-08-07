
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
argentina=vistas('http://127.0.0.1:5984/argentinafinal/_design/argentinaporPaisMundial/_view/argentinaporPaisMundial')
belgica=vistas('http://127.0.0.1:5984/belgicafinal/_design/belgicaporPaisMundial/_view/belgicaporPaisMundial')
brasil=vistas('http://127.0.0.1:5984/brasilfinal/_design/brasilporPaisMundial/_view/brasilporPaisMundial')
colombia=vistas('http://127.0.0.1:5984/colombiafinal/_design/colombiaporPaisMundial/_view/colombiaporPaisMundial')
croacia=vistas('http://127.0.0.1:5984/croaciafinal/_design/croaciaporPaisMundial/_view/croaciaporPaisMundial')
dinamarca=vistas('http://127.0.0.1:5984/dinamarcafinal/_design/dinamarcaporPaisMundial/_view/dinamarcaporPaisMundial')
espania=vistas('http://127.0.0.1:5984/espanafinal/_design/espanaporPaisMundial/_view/espanaporPaisMundial')
francia=vistas('http://127.0.0.1:5984/franciafinal/_design/franciaporPaisMundial/_view/franciaporPaisMundial')
inglaterra=vistas('http://127.0.0.1:5984/inglaterrafinal/_design/inglaterraporPaisMundial/_view/inglaterraporPaisMundial')
japon=vistas('http://127.0.0.1:5984/japonfinal/_design/japonporPaisMundial/_view/japonporPaisMundial')
mexico=vistas('http://127.0.0.1:5984/mexicofinal/_design/mexicoporPaisMundial/_view/mexicoporPaisMundial')
panama=vistas('http://127.0.0.1:5984/panamafinal/_design/panamaporPaisMundial/_view/panamaporPaisMundial')
polonia=vistas('http://127.0.0.1:5984/poloniafinal/_design/poloniaporPaisMundial/_view/poloniaporPaisMundial')
portugal=vistas('http://127.0.0.1:5984/portugalfinal/_design/portugalporPaisMundial/_view/portugalporPaisMundial')
russia=vistas('http://127.0.0.1:5984/rusiafinal/_design/rusiaporPaisMundial/_view/rusiaporPaisMundial')
senegal=vistas('http://127.0.0.1:5984/senegalfinal/_design/senegalporPaisMundial/_view/senegalporPaisMundial')
suecia=vistas('http://127.0.0.1:5984/sueciafinal/_design/sueciaporPaisMundial/_view/sueciaporPaisMundial')
suiza=vistas('http://127.0.0.1:5984/suizafinal/_design/suizaporPaisMundial/_view/suizaporPaisMundial')
tunez=vistas('http://127.0.0.1:5984/tunezfinal/_design/tunezporPaisMundial/_view/tunezporPaisMundial')
uruguay=vistas('http://127.0.0.1:5984/uruguayfinal/_design/uruguayporPaisMundial/_view/uruguayporPaisMundial')

contadorargentina=0
contadorbelgica=0
contadorbrasil=0
contadorcolombia=0
contadorcroacia=0
contadordinamarca=0
contadorespania=0
contadorfrancia=0
contadoringlaterra=0
contadorjapon=0
contadormexico=0
contadorpanama=0
contadorpolonia=0
contadorportugal=0
contadorrussia=0
contadorsenegal=0
contadorsuecia=0
contadorsuiza=0
contadortunez=0
contadoruruguay=0
contadorotros=0

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

listaPais=[]
listaText=[]

def llenar(valor):
    for x in valor['rows']:
        idioma=x['key']
	textovistas=x['value']
        listaPais.append(idioma)
	listaText.append(textovistas)
    return listaPais,listaText

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
 		if "AR" in listaPais[q]:
			contadorargentina=contadorargentina+1
		elif "BE" in listaPais[q]:
			contadorbelgica=contadorbelgica+1
		elif "BR" in listaPais[q]:
			contadorbrasil=contadorbrasil+1
		elif "CO" in listaPais[q]:
			contadorcolombia=contadorcolombia+1
		elif "DK" in listaPais[q]:
			contadordinamarca=contadordinamarca+1
		elif "HR" in listaPais[q]:
			contadorcroacia=contadorcroacia+1	
		elif "ES" in listaPais[q]:
			contadorespania=contadorespania+1
		elif "FR" in listaPais[q]:
			contadorfrancia=contadorfrancia+1		
		elif "GB" in listaPais[q]:
			contadoringlaterra=contadoringlaterra+1				
		elif "JP" in listaPais[q]:
			contadorjapon=contadorjapon+1
		elif "MX" in listaPais[q]:
			contadormexico=contadormexico+1
		elif "PA" in listaPais[q]:
			contadorpanama=contadorpanama+1
		elif "PL" in listaPais[q]:
			contadorpolonia=contadorpolonia+1
		elif "PT" in listaPais[q]:
			contadorportugal=contadorportugal+1
		elif "RU" in listaPais[q]:
			contadorrussia=contadorrussia+1
		elif "SN" in listaPais[q]:
			contadorsenegal=contadorsenegal+1
		elif "SE" in listaPais[q]:
			contadorsuecia=contadorsuecia+1
		elif "CH" in listaPais[q]:
			contadorsuiza=contadorsuiza+1
		elif "TN" in listaPais[q]:
			contadortunez=contadortunez+1
		elif "UY" in listaPais[q]:
			contadoruruguay=contadoruruguay+1
		else:
			contadorotros=contadorotros+1
dias=('ARG','BE','BRA','COL','CRO','DIN','ESP','FRA','ING','JAP','MX','PAN','POL','POR','RUS','SEN','SUE','SUI','TUN','URU','OTROS')
y=np.arange(len(dias))
tweets=[contadorargentina,contadorbelgica,contadorbrasil,contadorcolombia,contadorcroacia,contadordinamarca,contadorespania,contadorfrancia,contadoringlaterra,contadorjapon,contadormexico,contadorpanama,contadorpolonia,contadorportugal,contadorrussia,contadorsenegal,contadorsuecia,contadorsuiza,contadortunez,contadoruruguay,contadorotros]
plt.bar(y,tweets,align='center',alpha=1)
plt.xticks(y,dias,fontsize=8)
plt.xlabel('Paises',fontsize=10)
plt.ylabel('Cantidad de tweets', fontsize=10)
plt.title('Tweets por paises')
plt.show()


