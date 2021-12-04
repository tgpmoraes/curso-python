# Gerador de números sob demanda, e usa menos memória que o list comprehension
generator = (i ** 2 for i in range(10) if i % 2 == 0)
print(next(generator))  # Saída 0
print(next(generator))  # Saída 4
print(next(generator))  # Saída 16
print(next(generator))  # Saída 36
print(next(generator))  # Saída 64
# print(next(generator))  # Erro!

# Validar o uso de memória no terminal
'''
    a = [i * 2 for i in range(1000) if i % 2 == 0]
    b = (i ** 2 for i in range(1000) if i % 2 == 0)
    import sys
    sys.getsizeof(a)
    sys.getsizeof(b)
'''
