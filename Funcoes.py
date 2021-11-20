def menu():
    return input("O que deseja realizar?\n" +
              "<I> - Para Inserir um usuário\n" +
              "<P> - Para Pesquisar um usuário\n" +
              "<E> - Para Excluir um usuário\n" +
              "<L> - Para Listar um usuário\n" +
              "<S> - Para Sair").upper()

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                       input("Digite a última data de acesso: "),
                                                       input("Qual a última estação acessada: ").upper()]

def excluir(dicionario):
    usuario = input("Digite o usuário que deseja excluir:").upper()
    dicionario.pop(usuario)




