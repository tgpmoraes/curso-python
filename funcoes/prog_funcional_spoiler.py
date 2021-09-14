# O parâmetro da função será outra função
def executar(funcao):
    # Verifica se o que passou por parâmetro é uma função
    if callable(funcao):
        # quando usa os (), a função é invocada
        funcao()


def bom_dia():
    print('Bom dia!')


def boa_tarde():
    print('Boa tarde!')


if __name__ == '__main__':
    executar(bom_dia)
    executar(boa_tarde)
    executar(1)
