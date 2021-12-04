from datetime import datetime, timedelta


class TarefaNaoEncontrada(Exception):
    pass


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    # Método mágico usado em variáveis que permite laço.
    # Neste caso, vai agir como __str__, não precisa passar
    # nenhum método na chamada, ver o for abaixo
    def __iter__(self):
        return self.tarefas.__iter__()

    # Sobrecarga do operador +=
    # projeto += tarefa
    # casa += ...
    def __iadd__(self, tarefa):
        # Defino o dono como o ojbeto que está trabalhando
        tarefa.dono = self
        # chama função interda para adicionar tarefa
        self._add_tarefa(tarefa)
        return self

    # Por convenção, usa-se _ para definir um método interno,
    # já que não existe overload em Python
    # Se espera receber pelo parâmetro tarefa, ou uma tarefa,
    # ou uma tarefarecorrente
    # kwargs (parâmetro nomeados variáveis) é adicionado para
    # manter uniforme com o outro método _add_nova_tarefa
    def _add_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)

    # kwargs, neste caso, será usado para passar vencimento
    def _add_nova_tarefa(self, descricao, **kwargs):
        # O método get pertence ao dicionário e se usa para pegar o valor
        # a partir da chave passada, e se não achar, usa o valor padrão None
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    # O método add funciona de duas formas e isso vai depender do que for
    # passado por parâmetro
    def add(self, tarefa, vencimento=None, **kwargs):
        # isinstance vai verificar se o que foi passado é um objeto instanciado
        # O objeto pode ser do tipo Tarefa ou TarefaRecorrente,
        # já que herda de Tarefa
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) \
            else self._add_nova_tarefa
        # É adicionado a chave vencimento em kwargs para usar no método
        # _add_nova_tarefa
        kwargs['vencimento'] = vencimento
        # Após o método ser escolhido, ele é chamado
        # Desta forma, é possível simular o overload de métodos
        funcao_escolhida(tarefa, **kwargs)

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        try:
            # Como o list comprehension retorna uma lista,
            # precisa passar o índice 0 para ser o primeiro elemento
            return [tarefa for tarefa in self.tarefas
                    if tarefa.descricao == descricao][0]
        # Tratar a exceção mais explicitamente
        except IndexError as e:
            raise TarefaNaoEncontrada(str(e))

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
        self.dono = None

    # Para não perder o concluir da classe pai, faz o uso do
    # método super() para chamar o método pai
    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        nova_tarefa = TarefaRecorrente(
            self.descricao, novo_vencimento, self.dias)
        # dono no contexto do código, é o projeto
        if self.dono:
            self.dono += nova_tarefa
        return nova_tarefa


def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Lavar prato')
    # A classe projeto cria uma tarefa e não tarefa recorrente,
    # por isso será feito append manualmente e não pelo método
    # A sobrecarga permite adicionar de forma mais simples
    # Neste momento a variável dono é definida
    casa += TarefaRecorrente('Trocar lençóis', datetime.now(), 7)
    # Atualiza a tarefa recorrente atual para concluir e o
    # método já cria a nova
    # Pelo fato da tarefa ter um dono, o método concluir já
    # adiciona diretamente na lista, e assim não precisa
    # deixar explicito
    # casa.add(casa.procurar('Trocar lençóis').concluir())
    casa.procurar('Trocar lençóis').concluir()
    print(casa)

    try:
        casa.procurar('Lavar prato - ERRO').concluir()
    except TarefaNaoEncontrada as e:
        print(f'A causa foi "{str(e)}"')

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
