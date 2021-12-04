from random import randint

if __name__ == '__main__':
    sorteio = randint(1, 20)
    acertou = False
    print('Olá! Qual é o seu nome?')
    nome = input()
    print(f'Então, {nome}, Eu estou pensando em um número entre 1 e 20.')
    tentativas = 0
    while (not acertou):
        tentativas += 1
        print('Adivinhe ou entre com 0 para sair.')
        entrada = int(input())

        if (entrada == sorteio):
            print(f'Bom trabalho, {nome}! Você acertou meu \
número em {tentativas} tentativas!')
            acertou = True
        elif (entrada == 0):
            print(f'Você desistiu após {tentativas} tentativas')
            acertou = True
        elif (entrada > sorteio):
            print('Sua tentativa é maior do que número sorteado.')
        else:
            print('Sua tentativa é menor do que número sorteado.')
