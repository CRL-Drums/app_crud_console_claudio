#Métodos

from entidades import *
import os
try:
    console_clear = lambda: os.system('clear')
except:
    console_clear = lambda: os.system('cls')

quantidade_selecionada = 0
lista = []

def cadastro():
    print("- Cadastrar -\n")
    print("Selecione a quantidade de usuários que você deseja cadastrar: ")
    
    try:
        quantidade_selecionada = int(input())
    except:
        print("Erro: Digite um número inteiro!\n")
        input("Pressione qualquer tecla para continuar.")

    contador = 0

    try:

        while(contador < quantidade_selecionada):
            print()
            print("Digite o nome, telefone, email, twitter e instagram")
            print("Exemplo:")
            print("nome telefone email twitter instagram")

            escolha = input()
            escolha_array = escolha.split(' ')
            contador += 1
            usuario = Conta(contador, escolha_array[0], escolha_array[1], escolha_array[2], escolha_array[3], escolha_array[4])
            
            lista.append(usuario)
    except:
        print("Erro: Faltou informação")
        input("Pressione qualquer tecla para voltar ao Menu.")
        
        

def remover():

    print("- Remover - \n")

    relatorio()

    print("Digite o número do ID correspondente ao nome do usuário que deseja remover: ")

    try:
        id = int(input())
        print("Tem certeza que deseja remover? Digite 's' ou 'n' ")
        certeza = input()
        if(certeza == 's'):
            del(lista[id - 1])
            input("Pressione qualquer tecla para voltar.")
        else:
            print("Pressione qualquer tecla para voltar.")

    except:
        print("ID não encontrado.")
        input("Pressione qualquer tecla para voltar.")


def alterar():
    print("- Alterar - \n")
    print("Digite o número do ID correspondente ao nome do usuário que deseja alterar: \n")
    
    try:
        id = int(input())
        
        print("Digite o nome, telefone, email, twitter e instagram\n")

        print("Exemplo:")
        print("nome telefone email twitter instagram")

        escolha = input()
        escolha_array = escolha.split(' ')
        usuario = Conta(lista[id - 1], escolha_array[0], escolha_array[1], escolha_array[2], escolha_array[3], escolha_array[4])
            
        lista[id - 1] = usuario
    except:
        print("ID inválido.")
        print("Pressione qualquer tecla para voltar.")


def procurar_por_nome():
    lista_nomes = []
    for item in lista:
        lista_nomes.append(item.nome)
    return lista_nomes

def printar_por_id(index):
    print("Número, Nome, E-mail, Twitter, Facebook\n")
    print(str(lista[index].id) + ", " + str(lista[index].nome) + ", " + str(lista[index]. email) + ", " + str(lista[index].twitter) + ", " + str(lista[index].facebook))


def consultar():
    nome = ""
    try:
        print("- Consultar - \n")
        print("Digite o nome: ")

        nome = input()
        index = procurar_por_nome().index(nome)

        print()

        printar_por_id(index)

        input("\nPressione qualquer tecla para voltar.")
    except:
        print("\nErro: Usuário não encontrado")
        input("Pressione qualquer tecla para voltar.")


def relatorio():
    print("- Consultar - \n")
    print("Número, Nome, E-mail, Twitter, Facebook\n")
    
    for cadastro in lista:
        print(str(cadastro.id) + ", " + str(cadastro.nome) + ", " + str(cadastro. email) + ", " + str(cadastro.twitter) + ", " + str(cadastro.facebook))
