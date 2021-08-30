"""Atividade agenda telefônica by: Cláudio Lima"""


#imports
import os
from funcoes import cadastro, alterar, remover, consultar, relatorio

# Função para limpar o console para as entradas em cada menu

console_clear = lambda: os.system('cls')
# Se seu sistema for Linux/Mac comente a de cima e descomente a debaixo.
#console_clear = lambda: os.system('clear')

# Inicio da aplicação

# Tela de boas-vindas
print("\n-=              Agenda              -=\n")
print("- Atividade Avaliativa de Cláudio Rocha Lima -\n")


opcao_selecionada_menu = 0

#Menu princial
while not opcao_selecionada_menu == 6:

    # Atribuido o valor da opcao a '0' para que sempre que retorne ao menu a opção não seja alguma possivel para entrar em outro menu.
    opcao_selecionada_menu = 0

    try:
        # Tela do menu
        print("Selecione uma das opções abaixo: \n")

        print("1 - Cadastrar")
        print("2 - Alterar")
        print("3 - Remover")
        print("4 - Consultar")
        print("5 - Relatório")
        print("6 - Sair")

        opcao_selecionada_menu = int(input())

        # Condicionais para cada opção selecionada
        # Todos os 'console_clear()'são invocados para que o console seja limpo.
        
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
    except:
        console_clear()
        print("Digite uma opção válida.")
            
    # Limpando novamente para o retorno do bloco do código chamando o 'Menu Principal'
    console_clear()
