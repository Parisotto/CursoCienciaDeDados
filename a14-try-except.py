def dividir(a, b):
    a = int(a)
    b = int(b)
    if b != 0: 
        quociente = a / b 
        print(f"{a} dividido por {b} é igual a {quociente}")
    else: 
        print("Impossivel dividir por 0")
    
a = input("SEM TRY - Digite o dividendo: ")
b = input("SEM TRY - Digite o dividor: ")
dividir(a, b)

def dividirComTry():
    try:
        dividendo = int(input("COM TRY - Digite o dividendo: "))
        divisor = int(input("COM TRY - Digite divisor: "))
        quociente = dividendo / divisor
        print(f"{dividendo} dividido por {divisor} é igual a {quociente}")
    except ValueError:
        print("Você não digitou um número válido.")
    except ZeroDivisionError:
        print("Impossível dividir por 0")
    else:
        print("Nenhum erro ocorreu.")
    finally:
        print("Este bloco sempre será executado.")

dividirComTry()
