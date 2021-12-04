def tag_bloco(conteudo, *args, classe='success', inline=False):
    # operador ternario
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'


def tag_lista(*itens):
    # join fará uma concatenação de um generator
    # O generator está em uma chamada de função e
    # por isso não precisa de ()
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul>{lista}</ul>'


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
