Sistema Bancário em Python

Este é um projeto de um Sistema Bancário Simples desenvolvido em Python, que implementa funcionalidades básicas de gerenciamento de contas bancárias e usuários.

Funcionalidades

1. Criar Conta: Cadastra uma nova conta bancária associada a um usuário existente.


2. Criar Usuário: Registra um novo usuário no sistema.


3. Depositar: Permite realizar depósitos em uma conta bancária.


4. Sacar: Realiza saques de até R$ 500 por operação, com limite de 3 saques diários.


5. Exibir Extrato: Mostra o extrato detalhado de uma conta bancária.


6. Listar Contas: Exibe todas as contas cadastradas no banco.


7. Listar Usuários: Mostra as informações de um usuário cadastrado.


8. Encerrar: Finaliza a execução do sistema.



Estrutura do Projeto

ContaBancaria: Representa uma conta bancária com funcionalidades de saque, depósito e exibição de extrato.

Usuario: Representa um cliente do banco com CPF e nome.

Banco: Gerencia as contas e usuários do sistema, possibilitando o cadastro e a busca.

main: Interface interativa para o usuário executar as funcionalidades do sistema.


Requisitos

Python 3.7 ou superior.


Como Executar

1. Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio


2. Execute o script:

python sistema_bancario.py


3. Siga as instruções do menu para utilizar o sistema.



Exemplo de Uso

Criar Usuário

1. Escolha a opção 2. Criar Usuário.


2. Insira o CPF e o nome do usuário.


3. O sistema confirmará o cadastro.



Criar Conta

1. Escolha a opção 1. Criar Conta.


2. Insira o número da agência, número da conta e o CPF do usuário.


3. O sistema confirmará a criação da conta.



Realizar Depósito

1. Escolha a opção 3. Depositar.


2. Informe o número da conta e o valor do depósito.


3. O sistema confirmará a operação.



Realizar Saque

1. Escolha a opção 4. Sacar.


2. Informe o número da conta e o valor do saque.


3. O sistema verificará os limites e confirmará a operação.



Exibir Extrato

1. Escolha a opção 5. Exibir Extrato.


2. Insira o número da conta.


3. O sistema mostrará o extrato detalhado e o saldo.



Limitações

O limite de saque por operação é de R$ 500,00.

Cada conta tem um limite de 3 saques diários.

Não há integração com bancos reais, sendo apenas um sistema local.


Contribuições

Sinta-se à vontade para contribuir com melhorias para o projeto. Para isso:

1. Faça um fork do repositório.


2. Crie uma branch para sua funcionalidade:

git checkout -b minha-melhoria


3. Envie um Pull Request.



Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais informações.


---

Desenvolvido com 💻 por Seu Nome.

