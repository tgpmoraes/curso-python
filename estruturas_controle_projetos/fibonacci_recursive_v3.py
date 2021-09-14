# 0, 1, 1, 2, 3, 5, 8, 13, 21
import sys


def fibonacci(quantidade, sequencia=(0, 1)):
    return sequencia if sequencia[len(sequencia)-1] >= quantidade else \
        fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


def numero_em_fibonacci(numero):
    return numero in fibonacci(numero)


if __name__ == '__main__':
    # Verifica se número de entrada está na lista de Fibonacci
    numero = sys.argv[1]
    print(numero_em_fibonacci(int(numero)))
