# log será a função que vai docarar a função
# que vai receber como parâmetro
def log(function):
    # A função decorator recebe todos os parâmetros,
    # não importa se são posicionais ou nomeados
    def decorator(*args, **kwargs):
        # Função é um objeto e por isso conseguimos elementos da mesma
        print(f'Início da chamada da função: {function.__name__}')
        # Imprimir os argumentos posicionais
        print(f'args: {args}')
        # Imprimir os argumentos nomeados
        print(f'kwargs: {kwargs}')
        resultado = function(*args, **kwargs)
        print(f'Resultado da chamada: {resultado}')
        return resultado
    return decorator


# @log retorna a função decorator
# A função decorator tem que retornar a função chamada inicialmente
@log
def soma(x, y):
    return x + y


@log
def sub(x, y):
    return x - y


if __name__ == '__main__':
    print(soma(5, 7))
    print(sub(5, y=7))
