import random

linha = 10
coluna = 10

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




