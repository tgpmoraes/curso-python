from math import pi
import sys


def circulo(raio):
    return pi * float(raio) ** 2


# Se o módulo atual for o main, execute
if __name__ == '__main__':
    # índice 0 é o nome do arquivo e por isso tem que iniciar do 1
    raio = sys.argv[1]
    area = circulo(raio)
    print('Área do círculo', area)
