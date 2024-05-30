menu = """

[1]  Novo deposito
[2]  Novo saque
[3]  Extrato
[4]  Sair do sistema 

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3
saques = 0

while True:

    opcao = input(menu)

    if opcao == "1":
        valor_deposito = float(input("Qual valor deseja depositar?")) 

        if valor_deposito <= 0:
            print(f"{valor_deposito} é um valor invalido por ser negativo, por favor, tente novamente.")
            valor_deposito = 0
        else:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
    
    elif opcao == "2":
        valor_saque = float(input("Qual valor deseja sacar?")) 

        if valor_saque > limite:
            print(f"{valor_saque} exede seu limite para saque nesta conta, por favor, entre com outro valor.")
        elif valor_saque > saldo:
            print(f"{valor_saque} é maior que o saldo nesta conta, saldo insuficiente, entre com outro valor.")
        elif saques > limite_saques:
            print("voce exedeu o numero de saque permitidos.")
        elif valor_saque <= 0:
            print(f"{valor_deposito} é um valor invalido por ser negativo, por favor, tente novamente.")
            valor_deposito = 0    
        else:
            saldo -= valor_saque
            extrato += f"saque: R$ {valor_saque:.2f}\n"
            saques = saques + 1

    elif opcao == "3":
        print("\n---------------------EXTRATO--------------------------")
        print("Exrato vazio, nao foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n------------------------------------------------------")

    elif opcao == "4":
        break
    else:
        print("operacao invalida, tente novamente.")                 


