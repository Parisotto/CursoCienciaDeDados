from time import sleep
from uteis.utilitarios import titulo

# 1. Faça uma função que simula um caixa eletrônico. Se o usuário quiser sacar uma certa quantia de dólares calcule quantas notas de US$ 50, de US$ 20, de US$ 10 e/ou de US$ 1 serão disponibilizadas ao sacador. Desconsidere os centavos na entrada, nos cálculos e na saída.
def sacarDolares(dolares):
    cedula = 50
    total = 0
    print(f"\nSaque de US$ {dolares}.00 em:")

    while True:
        if dolares >= cedula:
            dolares -= cedula
            total += 1
        else:
            if total > 0:
                sleep(1)
                print(f'{total} cédulas de US$ {cedula}.00')
                total = 0

            if cedula == 50:
                cedula = 20
            elif cedula == 20:
                cedula = 10
            elif cedula == 10:
                cedula = 5
            elif cedula == 5:
                cedula = 1

            if dolares == 0: break

# sacarDolares(163) // teste também 125

# 2. Desenvolva uma rotina que converta um determinado valor de Reais em Dolar. Considere que US$ 1.00 vale R$ 5,00. Imprima o valor convertido em doláres. Desconsidere os centavos.
def conversor(reais, dolar):
    dolares = int(reais / dolar)
    print(f"R$ {reais},00 equivalem à US$ {dolares}.00")
    return dolares  # refatorado

# conversor(500, 5)

# 3. Faça uma função que simule um depósito em Reais em uma conta que já possua R$ 1000,00 de saldo. Simule também um saque dentro do saldo dispinível. Apresente o saldo após o depósito ou saque. Desconsidere os centavos.
def conta(valor, saldo=1000, cotacao=0):
    saldo += valor

    if saldo < 0:
        print(f"\nSaldo insuficiente| ")
        saldo -= valor
        return saldo  # refatorado

    # print(f"Seu saldo é de R$ {saldo},00.")
    # refatorado
    if valor < 0:
        dolares = int(conversor(-valor, cotacao))
        sacarDolares(dolares)

    return saldo

# conta(750)

# 4. Desenvolva um programa faça um depósito em Reais em uma conta que já possua um saldo inicial de R$ 1000. Apos isso, o usuário deve sacar uma certa quantia desta conta, dentro do saldo. A quantia na conta estará em Reais, a solicitação do saque deverá ser feita em Reais, mas o saque deverá ser feito em dólares. Use as funções desenvolvidas anterirmente para fazer o saque, a conversão e a saída em dólares. Faça o refatoramento necessário nas outras funções.
def main():
    titulo("Sacar dólares do caixa eletrônico")
    deposito = int(input("Digite o valor do depósito R$ "))
    saldo = conta(deposito)
    print(f"Seu saldo após o depósito de R$ {deposito},00 é de R$ {saldo},00.")

    sleep(1)
    saque = int(input("\nDigite o valor do saque R$ "))
    cotacao = int(input("Digite a cotação do dólar US$ "))
    saldo = conta(-saque, saldo, cotacao)

    print(f"\nSeu saldo após o saque é de R$ {saldo},00.")
    sleep(1)
    print("Obrigado por usar o Banco Escolar")

main()
