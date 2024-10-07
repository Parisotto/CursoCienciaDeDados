def exercicio(anos):
    meses = anos * 12
    dias = meses * 30
    horas = dias * 24
    minutos = horas * 60
    segundos = minutos * 60

    print(f"{anos} equivalem a:")
    print(f"    {meses} meses")
    print(f"    {dias} dias")
    print(f"    {horas} horas")
    print(f"    {minutos} minutos")
    print(f"    {segundos} segundos")
    
anos = int(input("Digite uma quantidade de anos: "))
exercicio(anos)
