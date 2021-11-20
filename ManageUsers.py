from Exercicio_Dicionario.Funcoes import *

usuarios = {}
opcao = menu()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L" or opcao == "S":
    if opcao == "I":
        inserir(usuarios)
        print(usuarios)
    if opcao == "E":
        excluir(usuarios)
        print(usuarios)
    if opcao == "S":
        break
    opcao = menu()
print(usuarios)
