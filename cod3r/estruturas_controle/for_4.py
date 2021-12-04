# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i)
# else:
#     print('Fim!')

# Função sortear_dado de 6 números entre 1 e 6
# For com range 1 a 6
# Excluir os números ímpares
# Se o número for par e for igual ao valor sorteado
# pela função dado, imprimir 'ACERTOU' e depois
# chamar o break
# Se não acertar, chama o else... print('Não acertou o número!')

from random import randint


def sortear_dado():
    return randint(1, 6)


for i in range(1, 7):
    if i % 2 == 1:
        continue
    if i == sortear_dado():
        print('ACERTOU', i)
        break
else:
    print('Não acertou o número!')
