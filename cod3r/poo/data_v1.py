class Data:
    # self é o objeto que está em execução
    # é obrigatório o uso do mesmo
    # def to_str(self):
    # Método mágico que é usado para converter o objeto para string
    # fazendo com que não haja na necessidade de explicitar a chamada
    # da mesma
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


# Criando um novo objeto
d1 = Data()
# Pelo fato do Python possuir tipos de atributos dinâmicos
# é possível definí-los a partir de um objeto sem que o mesmo
# tenha sido feito na classe
d1.dia = 24
d1.mes = 8
d1.ano = 2021
print(d1)


d2 = Data()
d2.dia = 7
d2.mes = 11
d2.ano = 2020
print(d2)
