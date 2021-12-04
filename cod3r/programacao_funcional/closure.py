def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular


if __name__ == '__main__':
    # dobro vai receber a função calcular
    # Vemos a funcionalidade de lazy evaluation
    # A função só vai calcular após receber o
    # segundo parâmetro
    # Closure é demonstrado com a função calcular
    # pois ela tem consciência que a variável x
    # está ao seu redor
    dobro = multiplicar(2)
    triplo = multiplicar(3)
    print(dobro)
    print(triplo)
    print(f'O triplo de 3 é {triplo(3)}')
    print(f'O dobro de 7 é {dobro(7)}')
