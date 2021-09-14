from datetime import datetime, timedelta


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        if not self.idade:
            return self.nome
        return f'{self.nome} possui {self.idade} anos de idade.'

    def is_adulto(self):
        return f'{self.nome} é adulto' if self.idade >= 18 \
            else f'{self.nome} não é adulto'


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    def __iter__(self):
        return self.compras.__iter__()

    def registrar_compra(self, Compra):
        self.compras.append(Compra)

    def get_data_ultima_compra(self):
        dt_string = "2021-08-28 8:54:09"
        format = '%Y-%m-%d %H:%M:%S'
        ultima_data_compra = datetime.strptime(dt_string, format)
        for compra in self.compras:
            if compra.data > ultima_data_compra:
                ultima_data_compra = compra.data
        return ultima_data_compra

    def total_compras(self):
        total = 0
        for compra in self.compras:
            total += compra.valor
        return total


class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario


class Compra:
    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.data = data
        self.valor = valor


def main():
    vendedor1 = Vendedor('João da Silva', 35, 5000.00)
    cliente1 = Cliente('José Gomes', 75)
    print(vendedor1)
    print(cliente1)
    cliente1.registrar_compra(
        Compra(vendedor1, datetime.now() - timedelta(minutes=3), 100.00))
    cliente1.registrar_compra(
        Compra(vendedor1, datetime.now() - timedelta(minutes=2), 200.00))
    cliente1.registrar_compra(
        Compra(vendedor1, datetime.now() - timedelta(minutes=1), 300.00))
    print(cliente1.get_data_ultima_compra())
    print(cliente1.total_compras())
    print(cliente1.is_adulto())


if __name__ == '__main__':
    main()
