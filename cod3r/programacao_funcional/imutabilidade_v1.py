from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

# Português do Brasil
setlocale(LC_ALL, 'pt_BR')

# Listar todos os meses do ano com 31 dias
# Minha resposta
meses = map(lambda m: m, zip(month_name, mdays))
meses_31 = filter(lambda m31: m31[1] == 31, meses)
meses_nomes = map(lambda nome: nome[0], meses_31)
# print('Meses com 31 dias: ', list(meses_nomes))

# Solução da COD3R
# 1. (filter) pegar os índices de todos os meses com 31 dias 1, 3, 5...
# 2. (map) transformar os índices em nome
# 3. (reduce) juntar tudo para imprimir
meses_idx = filter(lambda midx: mdays[midx] == 31, range(1, 13))
meses_nomes = map(lambda mes: month_name[mes], meses_idx)
meses_juntos = reduce(lambda meses, mes: f'{meses}\n- {mes}',
                      meses_nomes, 'Meses com 31 dias:')
print(meses_juntos)

print(
    reduce(
        lambda meses, mes: f'{meses}\n- {mes}',
        map(
            lambda mes: month_name[mes],
            filter(
                lambda midx: mdays[midx] == 31, range(1, 13)
            )
        ), 'Meses com 31 dias:'
    )
)
