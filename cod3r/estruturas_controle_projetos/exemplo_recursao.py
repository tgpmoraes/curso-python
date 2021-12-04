def imprimir(maximo, atual):
    # forma de parada do método recursivo
    if atual >= maximo:
        # return sem nada, vai devolver sem nenhum tipo de valor.
        # Usado para sair do método
        return
    print(atual)
    imprimir(maximo, atual + 1)


def imprimir2(maximo, atual):
    if atual < maximo:
        print(atual)
        imprimir2(maximo, atual + 1)


imprimir(10, 1)
imprimir2(10, 1)
