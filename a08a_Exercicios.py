def calcularTempo(anos):
    meses = anos * 12
    dias = meses * 30
    horas = dias * 24
    minutos = horas * 60
    segundos = minutos * 60

    print(f"{anos} anos equivalem a:")
    print(f"    {meses} meses")
    print(f"    {dias} dias")
    print(f"    {horas} horas")
    print(f"    {minutos} minutos")
    print(f"    {segundos} segundos")
    
def calcularTempo2(anos):
    print(f"{anos} anos equivalem a:")
    print(f"    {anos * 12} meses")
    print(f"    {anos * 12 * 30} dias")
    print(f"    {anos * 12 * 30 * 24} horas")
    print(f"    {anos * 12 * 30 * 24 * 60} minutos")
    print(f"    {anos * 12 * 30 * 24 * 60 * 60} segundos")

calcularTempo(2)
print()    
calcularTempo2(3)   
