from math import pi
import sys


def help():
    print("É necessário informar o raio do círculo.")
    print(f"Sintaxe: {sys.argv[0][2:]} <raio>")


def circulo(raio):
    return pi * float(raio) ** 2


# Se o módulo atual for o main, execute
if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Área do círculo', area)
