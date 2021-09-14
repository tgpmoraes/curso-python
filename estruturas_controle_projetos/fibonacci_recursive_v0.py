# 0, 1, 1, 2, 3, 5, 8, 13, 21
def fibonacci(quantidade, resultado=[0, 1]):
    if len(resultado) < quantidade:
        resultado.append(sum(resultado[-2:]))
        fibonacci(quantidade, resultado)
    return resultado


if __name__ == '__main__':
    # Listar os 20 primeiros números da sequência
    for fib in fibonacci(20):
        print(fib)
