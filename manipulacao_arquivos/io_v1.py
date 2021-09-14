# função open() está no buildins
arquivo = open('pessoas.csv', encoding='utf8')
dados = arquivo.read()
arquivo.close()
# splitlines vai quebrar cada uma das linhas
for registro in dados.splitlines():
    # split cria uma lista de elementos
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
