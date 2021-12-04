def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c


# sempre que fizer uso do *, será criado um empacotamento em uma tupla
def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == '__main__':
    print(soma_2(2, 3))
    print(soma_3(2, 4, 6))

    # PACKING
    print(soma_n(1))
    print(soma_n(1, 1))
    print(soma_n(1, 1, 1, 1, 1, 1, 1))

    # UNPACKING, como parâmetro de entrada, serve tupla ou lista
    tupla_nums = (1, 2, 3)
    print(soma_3(*tupla_nums))
    tupla_nums = [1, 2, 3]
    print(soma_3(*tupla_nums))
