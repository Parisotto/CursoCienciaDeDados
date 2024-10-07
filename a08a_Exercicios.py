def calcularTempo(anos):
    meses = anos * 12
    dias = meses * 30
    horas = dias * 24
    minutos = horas * 60
    segundos = minutos * 60

    print(f"1) {anos} anos equivalem a:")
    print(f"\t{meses} meses")
    print(f"\t{dias} dias")
    print(f"\t{horas} horas")
    print(f"\t{minutos} minutos")
    print(f"\t{segundos} segundos")
    
def calcularTempo2(anos):
    print(f"2) {anos} anos equivalem a:")
    print(f"\t{anos * 12} meses")
    print(f"\t{anos * 12 * 30} dias")
    print(f"\t{anos * 12 * 30 * 24} horas")
    print(f"\t{anos * 12 * 30 * 24 * 60} minutos")
    print(f"\t{anos * 12 * 30 * 24 * 60 * 60} segundos")

def calcularTempo3(anos):
    r = f"3) {anos} anos equivalem a:\n"
    r += f"\t{anos * 12} meses\n"
    r += f"\t{anos * 12 * 30} dias\n"
    r += f"\t{anos * 12 * 30 * 24} horas\n"
    r += f"\t{anos * 12 * 30 * 24 * 60} horas\n"
    r += f"\t{anos * 12 * 30 * 24 * 60 * 60} horas"
    return r


calcularTempo(2)
print()

anos = int(input("Digite quantos anos: "))   
calcularTempo2(anos)   
print()

print(calcularTempo3(int(input("Digite quantos anos: "))))
print()