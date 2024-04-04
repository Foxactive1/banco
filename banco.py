class ContaBancaria:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.saques_diarios = 0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f'Depósito de R$ {valor:.2f}')
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser positivo.')

    def sacar(self, valor):
        if valor <= 0:
            print('O valor do saque deve ser positivo.')
            return
        if valor > 500:
            print('O valor máximo de saque é R$ 500.00 por operação.')
            return
        if self.saldo >= valor and self.saques_diarios < 3:
            self.saldo -= valor
            self.saques_diarios += 1
            self.extrato.append(f'Saque de R$ {valor:.2f}')
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
        elif self.saques_diarios >= 3:
            print('Limite de saques diários excedido.')
        else:
            print('Saldo insuficiente para realizar o saque.')

    def exibir_extrato(self):
        print('\nExtrato:')
        if not self.extrato:
            print('Não foram realizadas movimentações.')
        else:
            for movimentacao in self.extrato:
                print(movimentacao)
            print(f'Saldo atual: R$ {self.saldo:.2f}')


class Usuario:
    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome


class Banco:
    def __init__(self):
        self.contas = []
        self.usuarios = []

    def criar_conta(self, agencia, numero_conta, cpf_usuario):
        usuario = self.buscar_usuario(cpf_usuario)
        if usuario:
            conta = ContaBancaria(agencia, numero_conta, usuario)
            self.contas.append(conta)
            print(f'Conta criada com sucesso para o usuário {usuario.nome}.')
        else:
            print('Usuário não encontrado.')

    def criar_usuario(self, cpf, nome):
        usuario = Usuario(cpf, nome)
        self.usuarios.append(usuario)
        print(f'Usuário {nome} cadastrado com sucesso.')

    def buscar_usuario(self, cpf):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None

    def listar_contas(self):
        print('\nLista de Contas:')
        for conta in self.contas:
            print(f'Agência: {conta.agencia} | Conta: {conta.numero_conta} | Saldo: R$ {conta.saldo:.2f}')

    def listar_usuarios(self, cpf):
        usuario = self.buscar_usuario(cpf)
        if usuario:
            print(f'\nInformações do Usuário:')
            print(f'CPF: {usuario.cpf}')
            print(f'Nome: {usuario.nome}')
        else:
            print('Usuário não encontrado.')


def main():
    banco = Banco()

    while True:
        print('\n1. Criar Conta')
        print('2. Criar Usuário')
        print('3. Depositar')
        print('4. Sacar')
        print('5. Exibir Extrato')
        print('6. Listar Contas')
        print('7. Listar Usuários')
        print('8. Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            agencia = input('Digite o número da agência: ')
            numero_conta = input('Digite o número da conta: ')
            cpf_usuario = input('Digite o CPF do usuário: ')
            banco.criar_conta(agencia, numero_conta, cpf_usuario)
        elif opcao == '2':
            cpf = input('Digite o CPF do usuário: ')
            nome = input('Digite o nome do usuário: ')
            banco.criar_usuario(cpf, nome)
        elif opcao == '3':
            numero_conta = input('Digite o número da conta: ')
            valor = float(input('Digite o valor a ser depositado: '))
            for conta in banco.contas:
                if conta.numero_conta == numero_conta:
                    conta.depositar(valor)
                    break
            else:
                print('Conta não encontrada.')
        elif opcao == '4':
            numero_conta = input('Digite o número da conta: ')
            valor = float(input('Digite o valor a ser sacado: '))
            for conta in banco.contas:
                if conta.numero_conta == numero_conta:
                    conta.sacar(valor)
                    break
            else:
                print('Conta não encontrada.')
        elif opcao == '5':
            numero_conta = input('Digite o número da conta: ')
            for conta in banco.contas:
                if conta.numero_conta == numero_conta:
                    conta.exibir_extrato()
                    break
            else:
                print('Conta não encontrada.')
        elif opcao == '6':
            banco.listar_contas()
        elif opcao == '7':
            cpf = input('Digite o CPF do usuário: ')
            banco.listar_usuarios(cpf)
        elif opcao == '8':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')


if __name__ == "__main__":
    main()
