class Banco:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser positivo.')

    def sacar(self, valor):
        if valor <= 0:
            print('O valor do saque deve ser positivo.')
            return
        if valor > 500:
            print('O valor máximo de saque é R$ 500.00.')
            return
        if self.saldo >= valor:
            self.saldo -= valor
            self.saques.append(valor)
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('Saldo insuficiente para realizar o saque.')

    def extrato(self):
        print('Extrato:')
        if not self.depositos and not self.saques:
            print('Não foram realizadas movimentações.')
        else:
            print('Depósitos:')
            for deposito in self.depositos:
                print(f'Depósito de R$ {deposito:.2f}')
            print('Saques:')
            for saque in self.saques:
                print(f'Saque de R$ {saque:.2f}')
            print(f'Saldo atual: R$ {self.saldo:.2f}')


def main():
    banco = Banco()

    while True:
        print('\n1. Depositar')
        print('2. Sacar')
        print('3. Visualizar Extrato')
        print('4. Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            valor = float(input('Digite o valor a ser depositado: '))
            banco.depositar(valor)
        elif opcao == '2':
            valor = float(input('Digite o valor a ser sacado: '))
            banco.sacar(valor)
        elif opcao == '3':
            banco.extrato()
        elif opcao == '4':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')


if __name__ == "__main__":
    main()
