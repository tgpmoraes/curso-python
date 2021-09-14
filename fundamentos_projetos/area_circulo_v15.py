from math import pi
import sys
import errno


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def help():
    print("É necessário informar o raio do círculo ou o lado do quadrado.")
    print(f"Sintaxe: {sys.argv[0][2:]} <raio> <lado>")


def circulo(raio):
    return pi * float(raio) ** 2


def quadrado(lado):
    return float(lado) ** 2


# Se o módulo atual for o main, execute
if __name__ == '__main__':
    if len(sys.argv) < 3:
        help()
        sys.exit(errno.EPERM)
    elif not sys.argv[1].isnumeric():
        help()
        print(TerminalColor.ERRO +
              'O raio deve ser uma valor numérico' + TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = circulo(raio)
    lado = sys.argv[2]
    area_quadrado = quadrado(lado)
    print('Área do círculo', area)
    print('Área do quadrado', area_quadrado)
    print(dir())
