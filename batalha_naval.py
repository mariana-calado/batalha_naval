import random

def criar_tabuleiro(tamanho=10):
    return [['🌊' for _ in range(tamanho)] for _ in range(tamanho)]

def exibir_tabuleiro(nome_jogador, tabuleiro):
    print(f"\nTabuleiro de {nome_jogador}:")
    for linha in tabuleiro:
        print(' '.join(linha))
    print()

tabuleiro_humano = criar_tabuleiro()
tabuleiro_computador = criar_tabuleiro()

exibir_tabuleiro("Humano", tabuleiro_humano)
exibir_tabuleiro("Computador", tabuleiro_computador)

restante_humano= 5
restente_computador=5

def posicao ():
    print("Escolha a posição das suas embarcações ")
    for i in range(5):
        
        linha=int(input("Escolha a linha "))
        coluna=int(input("Escolha a coluna "))
        S
