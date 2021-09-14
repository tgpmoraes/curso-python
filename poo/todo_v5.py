from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    # Método mágico usado em variáveis que permite laço.
    # Neste caso, vai agir como __str__, não precisa passar
    # nenhum método na chamada, ver o for abaixo
    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        # Como o list comprehension retorna uma lista,
        # precisa passar o índice 0 para ser o primeiro elemento
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]

    # função mágica __str__ para converser um projeto em uma string
    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefas(s) pendentes(s))'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('(Concluída)')
        elif self.vencimento:
            if datetime.now() >= self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dias)')
        return f'{self.descricao} ' + ' '.join(status)


# Ao definir Tarefa como parâmetro, significa que será Pai
# Atributos e comportamentos serão herdados por TarefaRecorrente
class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):
        # Chamar o construtor da classe pai
        super().__init__(descricao, vencimento)
        # o novo parâmetro dias não está definido na classe pai,
        # por isso feito explicitamente no construtor da filha
        self.dias = dias

    # Para não perder o concluir da classe pai, faz o uso do
    # método super() para chamar o método pai
    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        return TarefaRecorrente(self.descricao, novo_vencimento, self.dias)


def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Lavar prato')
    # A classe projeto cria uma tarefa e não tarefa recorrente,
    # por isso será feito append manualmente e não pelo método
    casa.tarefas.append(TarefaRecorrente('Trocar lençóis', datetime.now(), 7))
    # Atualiza a tarefa recorrente atual para concluir e o
    # método já cria a nova
    casa.tarefas.append(casa.procurar('Trocar lençóis').concluir())
    print(casa)

    casa.procurar('Lavar prato').concluir()
    for tarefa in casa:
        print(f'- {tarefa}')
    print(casa)

    mercado = Projeto('Compras no mercado')
    mercado.add('Frutas secas')
    mercado.add('Carne')
    mercado.add('Tomate', datetime.now() + timedelta(days=3, minutes=12))
    print(mercado)

    comprar_carne = mercado.procurar('Carne')
    comprar_carne.concluir()
    for tarefa in mercado:
        print(f'- {tarefa}')
    print(mercado)


if __name__ == '__main__':
    main()
