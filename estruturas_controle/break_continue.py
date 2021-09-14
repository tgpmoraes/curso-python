for x in range(1, 11):
    if x % 2 == 0:
        continue
    # continue faz com que não seja impresso números pares
    print(x)

for x in range(1, 11):
    if x == 5:
        break
    print(x)

print('Fim!')
