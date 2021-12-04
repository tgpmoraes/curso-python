import requests
import csv

url = 'http://www.geoservicos.ibge.gov.br/geoserver/wms?service' \
      '=WFS&version=1.0.0&request=GetFeature&typeName=CGEO:' \
      'RedeUrbanaSintese_Regic2007&outputFormat=CSV'

r = requests.get(url)

# r.encoding = 'ISO-8859-1'

with open("desafio-ibge-downlaod.csv", 'wb') as f:
    f.write(r.content)

with open('desafio-ibge-downlaod.csv', encoding='utf8') as entrada:
    reader = csv.reader(entrada)
    # skip the headers
    next(reader, None)
    for linha in reader:
        print('{}: {}'.format(linha[8], linha[3]))
