def dia_util(dia):
    dias = {
        1: 'Fim de semana',
        2: 'Dia útil',
        3: 'Dia útil',
        4: 'Dia útil',
        5: 'Dia útil',
        6: 'Dia útil',
        7: 'Fim de semana'
    }
    return dias.get(dia, '** inválido **')


if __name__ == '__main__':
    for dia in range(8):
        print(f'{dia}: {dia_util(dia)}')
