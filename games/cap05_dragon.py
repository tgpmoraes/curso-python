import random
import time


def displayIntro():
    print('''
            Você está em uma terra cheia de dragões. Em frente de você,
            haverá duas cavernas. Em uma caverna, o dragão é amistoso e
            irá compartilhar seu tesouro com você. O outro dragão é
            ambicioso e faminto, ele o comerá em um piscar de olhos.
          ''')


print()


def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Qual caverna você vai entrar? (1 ou 2)')
        cave = input()
    return cave


def checkCave(chosenCave):
    print('Você chegou na caverna...')
    time.sleep(2)
    print('Está escuro e assustador...')
    time.sleep(2)
    print('''
            Um enorme dragão pula em frente de você!
            Ele abre suas mandíbulas e...
          ''')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Ele dará seu tesouro')
    else:
        print('Ele o devorará em uma mordida')


if __name__ == '__main__':
    playAgain = 'sim'
    while playAgain == 'sim' or playAgain == 's':
        displayIntro()
        caveNumber = chooseCave()
        checkCave(caveNumber)

        print('Você gostaria de tentar novamente? (sim ou não)')
        playAgain = input()
