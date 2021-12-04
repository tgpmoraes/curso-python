import random

number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
print(f'Quanto é {number1} + {number2}?')
answer = input()
resultado = str(number1 + number2)
if answer == resultado:
    print('Correto!')
else:
    print(f'Não! A resposta é {resultado}')
