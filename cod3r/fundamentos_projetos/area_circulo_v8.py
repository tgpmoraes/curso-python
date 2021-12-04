from math import pi


def circulo(raio):
    print('Área do círculo', pi * float(raio) ** 2)


# Se o módulo atual for o main, execute
if __name__ == '__main__':
    raio = input('Informe o raio: ')
    circulo(raio)
