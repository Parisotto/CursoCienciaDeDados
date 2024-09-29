# Manipulando arquivos texto
import os

# CRIANDO E ESCREVENDO ARQUIVOS
with open('arquivo.txt', 'w') as arquivo:
    arquivo.write("Ola, mundo!\n")
    arquivo.write("Estou aqui!\n")
    linhas = ['Proxima linha', 'Outra linha']
    arquivo.writelines(linhas)

texto = "Aqui vai uma mensagem."
with open('outro-arquivo.txt', 'w') as arquivo:
    arquivo.write(texto)

arquivo = open('mais-um-arquivo.txt', 'w')
arquivo.write(texto + "\n")
arquivo.write("Outra linha" + "\n")
arquivo.write("Finalizei o  texto." + "\n")
arquivo.close()

# ABRINDO E LENDO ARQUIVOS
with open('mais-um-arquivo.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)

with open('arquivo.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)

conteudo = open('arquivoteste.txt', 'r')
print(conteudo.read())
conteudo.close()

lista = []
with open('arquivo.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    print(linhas)
    for linha in linhas:
        lista.append(linha)

for linha in lista:
    print(linha)
    
with open('vou-renomear.txt', 'w') as vr:
    vr.write("Olá, mundo!")

os.rename("vou-renomear.txt", "excluir.txt")
os.remove("excluir.txt")  

with open('vou-renomear.txt', 'w') as vr:
    vr.write("Olá, mundo!")

# os.rename("vou-renomear.txt", "./excluir/excluir.txt")

# caminho_pasta = "./excluir/"
# arquivos = os.listdir(caminho_pasta)
# for arquivo in arquivos:
#     print(arquivo)

# prefixo = "novo_"
# outra_pasta = "./outra/"
# for arquivo in arquivos:
#     caminho_atual = os.path.join(caminho_pasta, arquivo)
#     renomeado = os.path.join(outra_pasta, prefixo + arquivo)
#     os.rename(outra_pasta, renomeado)
