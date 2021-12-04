# 0, 1, 1, 2, 3, 5, 8, 13, 21
def fibonacci(quantidade, sequencia=(0, 1)):
    if len(sequencia) == quantidade:
        return sequencia
    # Para criar uma tupla com um único elemento,
    # tenho que colocar uma , no final
    # a operação de soma de tuplas gera uma nova
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    # Listar os 20 primeiros números da sequência
    for fib in fibonacci(20):
        print(fib)
