import csv

with open('pessoas.csv') as entrada:
    # O módulo já trata o arquivo CSV
    for pessoa in csv.reader(entrada):
        print('Nome: {}, Idade: {}'.format(*pessoa))
