
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

inglaterra=vistas('http://127.0.0.1:5984/inglaterrafinal/_design/inglaterraporPais7Julio/_view/inglaterraporPais7Julio')
suecia=vistas('http://127.0.0.1:5984/sueciafinal/_design/sueciaporPais7Julio/_view/sueciaporPais7Julio')
rusia=vistas('http://127.0.0.1:5984/rusiafinal/_design/rusiaporPais7Julio/_view/rusiaporPais7Julio')
croacia=vistas('http://127.0.0.1:5984/croaciafinal/_design/croaciaporPais7Julio/_view/croaciaporPais7Julio')

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

listaPaises=[]

def llenar(valor):
    for x in valor['rows']:
        pais=x['key']
        listaPaises.append(pais)
    return listaPaises


llenar(inglaterra)
llenar(suecia)
llenar(rusia)
llenar(croacia)

for q in range(len(listaPaises)):
		if "AR" in listaPaises[q]:
			contadorargentina=contadorargentina+1
		elif "BE" in listaPaises[q]:
			contadorbelgica=contadorbelgica+1
		elif "BR" in listaPaises[q]:
			contadorbrasil=contadorbrasil+1
		elif "CO" in listaPaises[q]:
			contadorcolombia=contadorcolombia+1
		elif "DK" in listaPaises[q]:
			contadordinamarca=contadordinamarca+1
		elif "HR" in listaPaises[q]:
			contadorcroacia=contadorcroacia+1	
		elif "ES" in listaPaises[q]:
			contadorespania=contadorespania+1
		elif "FR" in listaPaises[q]:
			contadorfrancia=contadorfrancia+1		
		elif "GB" in listaPaises[q]:
			contadoringlaterra=contadoringlaterra+1				
		elif "JP" in listaPaises[q]:
			contadorjapon=contadorjapon+1
		elif "MX" in listaPaises[q]:
			contadormexico=contadormexico+1
		elif "PA" in listaPaises[q]:
			contadorpanama=contadorpanama+1
		elif "PL" in listaPaises[q]:
			contadorpolonia=contadorpolonia+1
		elif "PT" in listaPaises[q]:
			contadorportugal=contadorportugal+1
		elif "RU" in listaPaises[q]:
			contadorrussia=contadorrussia+1
		elif "SN" in listaPaises[q]:
			contadorsenegal=contadorsenegal+1
		elif "SE" in listaPaises[q]:
			contadorsuecia=contadorsuecia+1
		elif "CH" in listaPaises[q]:
			contadorsuiza=contadorsuiza+1
		elif "TN" in listaPaises[q]:
			contadortunez=contadortunez+1
		elif "UY" in listaPaises[q]:
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
plt.title('Tweets por paises SueciavsInglaterra & RussiavsCroacia (7 de Julio)')
plt.show()


