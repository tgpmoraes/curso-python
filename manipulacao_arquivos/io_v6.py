# função open() está no buildins

with open('pessoas.csv', encoding='utf8') as arquivo:
    with open('pessoas.txt', 'w', encoding='utf8') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            # print dentro do arquivo com o parâmetro file
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('Arquivo já foi fechado')
