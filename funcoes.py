"""Funções da aplicação"""

#imports
from entidades import Conta
import os

# Função para limpar o console para as entradas em cada menu

console_clear = lambda: os.system('cls')
# Se seu sistema for Linux/Mac comente a de cima e descomente a debaixo.
#console_clear = lambda: os.system('clear')


# Variáveis estáticas
quantidade_selecionada = 0

# Criada a lista para armazenamento das contas
lista = []

# Funções do Menu principal
def cadastro():
    print("- Cadastrar -\n")
    print("Selecione a quantidade de usuários que você deseja cadastrar: ")
    
    try:
        quantidade_selecionada = int(input())
    except:
        print("Erro: Digite um número inteiro!\n")
        print_voltar_ao_menu()

    contador = 0

    try:

        while(contador < quantidade_selecionada):
            print()
            print("Digite o nome, telefone, email, twitter e facebook\n")
            print("Exemplo:")
            print("nome telefone email twitter facebook\n")

            escolha = input()
            escolha_array = escolha.split(' ')
            usuario = Conta(escolha_array[0], escolha_array[1], escolha_array[2], escolha_array[3], escolha_array[4])
            
            lista.append(usuario)

            contador += 1

            if contador == quantidade_selecionada:
                print("\nTodos os usuários foram cadastrados!\n")
                print_voltar_ao_menu()
    except:
        print("\nErro: Faltou informação\n")
        print_voltar_ao_menu()


def remover():

    print("- Remover - \n")
    listar_por_item()
    print("\nDigite o número do ID correspondente ao nome do usuário que deseja remover: ")

    try:
        id = int(input())
        print("Tem certeza que deseja remover? Digite 's' ou 'n' ")
        certeza = input()
        if(certeza == 's'):
            del(lista[id])
            print("\nRemovido com sucesso!\n")
            print_voltar_ao_menu()
        else:
            print("\nRemoção cancelada.\n")
            print_voltar_ao_menu()
    except:
        print("ID não encontrado.")
        print_voltar_ao_menu()


def alterar():
    print("- Alterar - \n")
    listar_por_item()
    print("\nDigite o número do ID correspondente ao nome do usuário que deseja alterar: \n")
    
    try:
        id = int(input())
        print("Digite o nome, telefone, email, twitter e facebook\n")

        print("Exemplo:")
        print("nome telefone email twitter facebook")

        escolha = input()
        escolha_array = escolha.split(' ')
        usuario = Conta(escolha_array[0], escolha_array[1], escolha_array[2], escolha_array[3], escolha_array[4])
            
        lista[id] = usuario

        print("Usuário alterado com sucesso!")
        print_voltar_ao_menu()
    except:
        print("\nID inválido.\n")
        print_voltar_ao_menu()


def consultar():
    nome = ""
    try:
        print("- Consultar - \n")
        print("Digite o nome: ")

        nome = input()
        index = listar_por_nome().index(nome)

        print()
        printar_por_id(index)
        print_voltar_ao_menu()
    except:
        print("\nErro: Usuário não encontrado")
        print_voltar_ao_menu()


def relatorio():
    print("- Relatório - \n")
    print("Número, Nome, E-mail, Twitter, Facebook\n")
    listar_por_item()
    print_voltar_ao_menu()
    


#UTEIS

# Função para printar por item na função 'relatorio()' e 'alterar()'
def listar_por_item():
    for cadastro in lista:
        print(str(listar_por_nome().index(cadastro.nome)) + ", " + str(cadastro.nome) + ", " + str(cadastro. email) + ", " + str(cadastro.twitter) + ", " + str(cadastro.facebook))

# Função para criar uma lista só com os nomes para serem pesquisados na função 'consultar()'
def listar_por_nome():
    lista_nomes = []
    for item in lista:
        lista_nomes.append(item.nome)
    return lista_nomes

# Função para printar por ID na função 'consultar()'
def printar_por_id(index):
    print("Nome, E-mail, Twitter, Facebook\n")
    print(str(lista[index].nome) + ", " + str(lista[index].email) + ", " + str(lista[index].twitter) + ", " + str(lista[index].facebook))

# Função apenas para printar. Já que ela se repete várias vezes, preferi criar um método para o código não ficar repetitivo.
def print_voltar_ao_menu():
    return input("\nPressione ENTER para voltar ao Menu.")
