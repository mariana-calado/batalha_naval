import random

tabuleiro_humano=[['🌊' for _ in range(10)] for _ in range(10)]
tabuleiro_computador=[['🌊' for _ in range(10)] for _ in range(10)]

def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))
    print()

exibir_tabuleiro(tabuleiro_humano)
exibir_tabuleiro(tabuleiro_computador)

restante_humano= 5
restente_computador=5

def posicao ():
    print("Escolha a posição das suas embarcações ")
    for i in range(5):
        
        linha=int(input("Escolha a linha "))
        coluna=int(input("Escolha a coluna "))
        
        
