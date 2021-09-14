# Implementação simplificada do map
def mapear(funcao, lista):
    for i in lista:
        yield funcao(i)


if __name__ == '__main__':
    resultado = mapear(lambda x: x ** 2, [2, 3, 4])
    print(list(resultado))
