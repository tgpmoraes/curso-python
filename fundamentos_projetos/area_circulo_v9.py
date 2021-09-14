from math import pi


def circulo(raio):
    return pi * float(raio) ** 2


# Se o módulo atual for o main, execute
if __name__ == '__main__':
    raio = input('Informe o raio: ')
    area = circulo(raio)
    print('Área do círculo', area)
