class EmailDeBoasVindas:
    def __init__(self):
        self.pessoas = ['Cristian', 'Robert', 'Rossana', 'Ana']

    def Iniciar(self):
        print('Olá bem vindo a este site!')
        emails_apresentacao = self.MontarCredencial(self.pessoas)
        for email in emails_apresentacao:
            print(email)

    def MontarCredencial(self, pessoas):
        credenciais = []
        for pessoa in pessoas:
            credenciais.append(
                f'a empresa gostaria de dar as boas vindas para o(a) {pessoa}')
        return credenciais


def main():
    email = EmailDeBoasVindas()
    email.Iniciar()


if __name__ == '__main__':
    main()
# 'F5' Começar a debuggar seu código
# 'F10' Analisar linha sem entrar no código interno
# 'F11' Analisar linha e entrar no código interno
# 'SHIFT-F11' sair do bloco de código atual e continuar a execução
