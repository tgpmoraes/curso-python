# função open() está no buildins
arquivo = open('pessoas.csv', encoding='utf8')
# strip remove os espaços por padrão nas laterais
# caso seja algo diferente de espaço, pode colocar
# o caracter como parâmetro
for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
arquivo.close()
