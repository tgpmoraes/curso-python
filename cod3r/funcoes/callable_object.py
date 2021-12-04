class Potencia:
    # Calcula uma potência específica
    # construtor usa __init__ e self é obrigatório e é o objeto atual
    def __init__(self, expoente):
        self.expoente = expoente

    # Função que será chamada quando usar um objeto como função
    def __call__(self, base):
        return base ** self.expoente


if __name__ == '__main__':
    # criação de objeto
    quadrado = Potencia(2)
    cubo = Potencia(3)

    if callable(quadrado) and callable(cubo):
        print(f'3^2 => {quadrado(3)}')
        print(f'5^3 => {cubo(5)}')
        # Chamar o objeto passando primeiro o expoente e depois a base
        print(Potencia(4)(2))
