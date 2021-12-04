def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'Menor de idade'
    elif idade in range(18, 65):
        return 'Adulto'
    elif idade in range(65, 100):
        return 'Melhor idade'
    elif idade >= 100:
        return 'Centenário'
    else:
        return 'idade inválida'


"""
    É sempre importante colocar o módulo principal,
    pois caso o arquivo seja importado em outro módulo,
    ele não será executado sem ser chamado.
"""

if __name__ == '__main__':
    idades = (17, 35, 87, 113, -2)
    for idade in idades:
        print(f'{idade}: {faixa_etaria(idade)}')
