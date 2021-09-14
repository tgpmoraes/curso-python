# função open() está no buildins
arquivo = open('pessoas.csv', encoding='utf8')
# Python lê o arquivo sobre demanda, em streaming
# Não carrega para memória o arquivo todo como o v1
for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
arquivo.close()
