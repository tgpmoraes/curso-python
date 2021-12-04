bloco_atrs = ('bloco_accesskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_style')


def filtrar_atrs(informados, suportados):
    # split por _ pela razão do que está passando por parâmetro
    # está sendo concatenado chave e valor com um espaço em branco
    # chave e valor é usado pelo fato dos valores passados ser
    # transformados em dicionário
    # filtrar apenas os elementos suportados
    return ' '.join(f'{k.split("_")[-1]}="{v}"'
                    for k, v in informados.items() if k in suportados)


def tag_bloco(conteudo, *args, classe='success', inline=False, **novos_atrs):
    # operador ternario
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(
        conteudo) else conteudo(*args, **novos_atrs)
    atributos = filtrar_atrs(novos_atrs, bloco_atrs)
    return f'<{tag} {atributos} class="{classe}">{html}</{tag}>'


def tag_lista(*itens, **novos_atrs):
    # join fará uma concatenação de um generator
    # O generator está em uma chamada de função e
    # por isso não precisa de ()
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul {filtrar_atrs(novos_atrs, ul_atrs)}>{lista}</ul>'


if __name__ == '__main__':
    # Parâmetros nomeados para trazer clareza para ao algoritmo
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', classe='info', inline=True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(inline=True, conteudo='inline'))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='Info'))
    # Após o uso de uma lista de argumentos, tem que usar os
    # parâmetros nomeados
    # A função sem () não é chamado
    print(tag_bloco(tag_lista, 'Sábado', 'Domingo',
                    classe='Info', inline=True))
    print(tag_bloco(tag_lista, 'Item 1', 'Item 2', classe='info',
                    bloco_accesskey='m', bloco_id='conteudo', ul_id='lista',
                    ul_style='color:red'))
