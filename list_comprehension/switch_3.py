# Terceiro exemplo de simulando switch que foi visto
# inicialmente no capítulo de estruturas_controle
# agora será usado o que foi aprendido em list_comprehension
def get_tipo_dia(dia):
    dias = {
        (1, 7): 'Fim de semana',
        # Tupla de múltiplos valores não funciona, por isso o uso do range
        # 7 não está incluído
        tuple(range(2, 7)): 'Dia de semana',
    }
    dia_escolhido = (tipo for numeros, tipo in dias.items() if dia in numeros)
    return next(dia_escolhido, '** dia inválido **')


if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_tipo_dia(dia)}')
