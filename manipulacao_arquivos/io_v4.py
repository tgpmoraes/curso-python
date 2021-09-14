# função open() está no buildins
# Caso tenha algum problema no loop, o arquivo não será fechado
# Por isso, se utiliza o try/finally
try:
    arquivo = open('pessoas.csv', encoding='utf8')

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
# Excessão sem tratamento de erro precisa ter a palavra reservado pass
except IndexError:
    pass
finally:
    # Finally sempre será executado, mesmo que o try não dê erro
    print('finally')
    arquivo.close()

if arquivo.closed:
    print('Arquivo já foi fechado')
