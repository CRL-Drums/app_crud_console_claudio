# Atividade agenda telefônica by: Cláudio Lima

import os
from metodos import *
try:
    console_clear = lambda: os.system('clear')
except:
    console_clear = lambda: os.system('cls')


print("-= Agenda -=\n")


opcao_selecionada_menu = 0

while(not opcao_selecionada_menu == 6):

    opcao_selecionada_menu = 0

    try:
        print("Selecione uma das opções abaixo: \n")

        print("1 - Cadastrar")
        print("2 - Alterar")
        print("3 - Remover")
        print("4 - Consultar")
        print("5 - Relatório")
        print("6 - Sair")

        opcao_selecionada_menu = int(input())

        if opcao_selecionada_menu == 1:
            console_clear()
            cadastro()

        if opcao_selecionada_menu == 2:
            console_clear()
            alterar()

        if opcao_selecionada_menu == 3:
            console_clear()
            remover()

        if opcao_selecionada_menu == 4:
            console_clear()
            consultar()

        if opcao_selecionada_menu == 5:
            console_clear()
            relatorio()
            voltar = input("\nPressione qualquer tecla para voltar")

    except:
        console_clear()
        print("Digite uma opção válida.")
            
    console_clear()
