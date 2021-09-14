import csv

with open('desafio-ibge.csv') as entrada:
    reader = csv.reader(entrada)
    # skip the headers
    next(reader, None)
    for linha in reader:
        print('{}: {}'.format(linha[8], linha[3]))
