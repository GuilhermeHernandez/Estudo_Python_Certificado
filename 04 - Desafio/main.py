'''

DESAFIO v1

    Fomos contratado por um grande banco para desenvolver o seu novo sistema . Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações : 
    
    **Apenas na minha conta

        Deposito 
            - Depositar valores positivos
            - Apenas na minha conta
            - Todos os depositos dever ser armazenado em uma variavel e exibido nas operações de extrato

        Saque 
            - Pode realizar apenas 3 saques por dia 
            - limite de R$ 500 por saque
            - Caso não tenha saldo em conta , o sistema deve exibir uma mensagem informando que não será possivel sacar o dinheiro por falta de saldo.
            - Todos os depositos dever ser armazenado em uma variavel e exibido nas operações de extrato


        Extrato
            - Listar todos os depositos e saques realizados na conta
            - No final da listagem deve ser exibido o saldo atual da conta
            - Os valores dever ser exibidos ultilizando o formato R$

'''

menu = '''
\tMenu Bank Soft

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Digite uma operação -> '''

extrato = '''

\tExtrato da Conta

'''

saldo = 0
limite = 500
numero_saque = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).lower()

    # ---> Opção de deposito
    if opcao == 'd':

        print("\n# --- > Deposito < --- #\n")
        valor = input("# --- > Qual valor que deseja depositar: ")

        if '-' in valor :
            print("\nOperação invalida -> Não depositamos valores negativo! ")

        else :
            valor = float(valor)
            saldo += valor
            extrato += f'\n -> Valor depositado : R$ {valor:.2f}\n'
    
    elif opcao == 's':

        print("\n# --- > Saque < --- #\n")
        valor = input("# --- > Qual valor que deseja sacar: ")

        if '-' in valor :
            print("\nOperação invalida -> Não Sacar valores negativo! ")
        
        else:

            if numero_saque < LIMITE_SAQUES:

                valor = int(valor)

                if valor <= 500:

                    if saldo >= valor :

                        saldo -= valor
                        extrato += f'\n -> Valor sacado : R$ {valor:.2f}\n'
                        numero_saque += 1

                    else:
                        print('Operação invalida -> Não pode sacar mais por falta de dinheiro! ')
                        quit()

                else :
                    print("\nOperação invalida -> Não pode sacar mais de R$ 500.00! ")
                    quit()

            else:
                print("Operação invalida -> Não pode sacar mais de 3 vezes! ")
                quit()

        

    elif opcao == 'e':

        extrato += f' -> Saldo atual : R$ {saldo:.2f}'

        print(extrato)

    elif opcao == 'q':
        quit()