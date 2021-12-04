def mdc(lista):
    divisor = 1
    resultado = 0
    while divisor <= min(lista):
        filtro = filter(lambda x: x % divisor == 0, lista)
        if len(list(filtro)) == len(lista):
            resultado = divisor
        divisor += 1
    return resultado


if __name__ == '__main__':
    print(mdc([21, 7]))  # 7
    print(mdc([125, 40]))  # 5
    print(mdc([9, 564, 66, 3]))  # 3
    print(mdc([55, 22]))  # 11
    print(mdc([15, 150]))  # 15
    print(mdc([7, 9]))  # 1
    print(mdc([4, 6]))  # 2
