produto = {'nome': 'Caneta Chic', 'preco': 14.99,
           'importada': True, 'estoque': 793}

# por padrão as chaves serão percorridas se nenhuma função
# for informada, mas existe o .keys()
for chave in produto:
    print(chave)

for valor in produto.values():
    print(valor)

# os valores de chave e valor estarão disponíveis após
# a conclusão do loop
for chave, valor in produto.items():
    print(chave, '=', valor)
