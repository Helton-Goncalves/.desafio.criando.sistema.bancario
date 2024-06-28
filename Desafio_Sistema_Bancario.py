menu = """"

[d] Depositar   
[s] Sacar
[e] Extrato
[q] Sair 

=> """
saldo = 10
limite = 6000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float (input("Informe o valor:"))

        if valor > 0 :
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else :
            print ("Operação falhou! O valor informado é inválido.")

    elif opcao == "s" :
        valor = float (input ("Informe o valor:"))
     
        excedeu_saldo = valor > saldo 

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo :
            print("Operação falhou! Saldo Insufuciente.")
        
        if excedeu_limite :
            print("Operação falhou! O valor de saque excedeu o limite.")

        if excedeu_saques :
            print("Operação falhou! Excedeu o limite de saques diários. ")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else :
            print("Operação falhou! Valor informado é inválido.")

    elif opcao == "e":
        print ("\n========Extrato=========")
        print ("Não foram realizadas movimentações." if not extrato else extrato)
        print (f"\nSaldo: R$ {saldo:.2f}")
        print ("===================================")
     
    elif opcao == "q":
         break

    else:
       print("Operação inválida, por favor selecione novamente a opção desejada. ")

