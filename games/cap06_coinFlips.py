import random


def retorna_progresso(flips, heads):
    return f'{flips} jogadas realizadas e tiveram {heads} caras.'


print('''Eu vou jogar uma moeda 1000 vezes. Adivinhe quantas
 vezes virará cara. (Pressione enter para começar)''')
input()
flips = 0
heads = 0

while flips < 1000:
    if random.randint(0, 1) == 1:
        heads += 1
    flips += 1

    if flips == 900:
        print(retorna_progresso(flips, heads))
    if flips == 100:
        print(retorna_progresso(flips, heads))
    if flips == 500:
        print(retorna_progresso(flips, heads))

print()
print(f'Dos 1000 lançamentos de moeda, cara apareceu {heads} vezes!')
print('Você chegou perto?')
