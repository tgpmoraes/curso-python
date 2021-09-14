def todos_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'Kargs: {kwargs}')


if __name__ == '__main__':
    # Existem dois tipos de parâmetros:
    # - Posicionados
    # - Nomeados
    # Exemplo abaixo apenas com parâmetros posicionados
    todos_params('a', 'b', 'c')
    # Exemplo abaixo com parâmetros posicionados e nomeados
    todos_params(1, 2, 3, legal=True, valor=12.99)
    todos_params('Ana', False, [1, 2, 3], tamanho='M', fragil=False)
    # Exemplo abaixo não funciona, pois argumentos do tipo posicional
    # não pode vir depois do nomeado
    # todos_params(primeiro='João', Maria)
    todos_params(primeiro='João', segundo='Maria')
    todos_params('Maria', primeiro='João')
