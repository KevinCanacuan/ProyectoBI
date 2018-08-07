
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
argentina=vistas('http://127.0.0.1:5984/argentinafinal/_design/argentinaporPais/_view/argentinaporPais')
belgica=vistas('http://127.0.0.1:5984/belgicafinal/_design/belgicaporPais/_view/belgicaporPais')
brasil=vistas('http://127.0.0.1:5984/brasilfinal/_design/brasilporPais/_view/brasilporPais')
colombia=vistas('http://127.0.0.1:5984/colombiafinal/_design/colombiaporPais/_view/colombiaporPais')
croacia=vistas('http://127.0.0.1:5984/croaciafinal/_design/croaciaporPais/_view/croaciaporPais')
dinamarca=vistas('http://127.0.0.1:5984/dinamarcafinal/_design/dinamarcaporPais/_view/dinamarcaporPais')
espania=vistas('http://127.0.0.1:5984/espanafinal/_design/espanaporPais/_view/espanaporPais')
francia=vistas('http://127.0.0.1:5984/franciafinal/_design/franciaporPais/_view/franciaporPais')
inglaterra=vistas('http://127.0.0.1:5984/inglaterrafinal/_design/inglaterraporPais/_view/inglaterraporPais')
japon=vistas('http://127.0.0.1:5984/japonfinal/_design/japonporPais/_view/japonporPais')
mexico=vistas('http://127.0.0.1:5984/mexicofinal/_design/mexicoporPais/_view/mexicoporPais')
panama=vistas('http://127.0.0.1:5984/panamafinal/_design/panamaporPais/_view/panamaporPais')
polonia=vistas('http://127.0.0.1:5984/poloniafinal/_design/poloniaporPais/_view/poloniaporPais')
portugal=vistas('http://127.0.0.1:5984/portugalfinal/_design/portugalporPais/_view/portugalporPais')
russia=vistas('http://127.0.0.1:5984/rusiafinal/_design/rusiaporPais/_view/rusiaporPais')
senegal=vistas('http://127.0.0.1:5984/senegalfinal/_design/senegalporPais/_view/senegalporPais')
suecia=vistas('http://127.0.0.1:5984/sueciafinal/_design/sueciaporPais/_view/sueciaporPais')
suiza=vistas('http://127.0.0.1:5984/suizafinal/_design/suizaporPais/_view/suizaporPais')
tunez=vistas('http://127.0.0.1:5984/tunezfinal/_design/tunezporPais/_view/tunezporPais')
uruguay=vistas('http://127.0.0.1:5984/uruguayfinal/_design/uruguayporPais/_view/uruguayporPais')

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

listaPais=[]

def llenar(valor):
    for x in valor['rows']:
        idioma=x['key']
        listaPais.append(idioma)
    return listaPais

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
for q in range(len(listaPais)):
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


