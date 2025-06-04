import random

tabuleiro_humano = [['🌊' for _ in range(10)] for _ in range(10)]
tabuleiro_computador = [['🌊' for _ in range(10)] for _ in range(10)]

def exibir_tabuleiro(jogador, tabuleiro, ocultar=False):
    print("    " + "  ".join(str(i) for i in range(10)))
    for i, linha in enumerate(tabuleiro):
        if ocultar:
            print(f"{i}  " + " ".join(["🌊" if celula == "⛵" else celula for celula in linha]))
        else:
            print(f"{i}  " + " ".join(linha))
    print()

def posicao():

    exibir_tabuleiro("Tabuleiro", tabuleiro_humano)  

    print("Escolha a posição das suas embarcações!")
    for i in range(5):
        while True:
            linha = int(input(f"Escolha a linha para embarcação {i+1} (0-9): "))
            coluna = int(input(f"Escolha a coluna para embarcação {i+1} (0-9): "))
                
            if 0 <= linha < 10 and 0 <= coluna < 10:
                if tabuleiro_humano[linha][coluna] == "🌊":
                    tabuleiro_humano[linha][coluna] = "⛵"
                    break
                else:
                    print("Você já tem um navio nesta coordenada! 🧭")
            else:
                print("Fora dos limites do mapa! 🗺️")

def posicao_computador():
    for _ in range(5):
        while True:
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)
            
            if tabuleiro_computador[linha][coluna] == "🌊":
                tabuleiro_computador[linha][coluna] = "⛵"
                break

posicao()
posicao_computador()
exibir_tabuleiro("Humano", tabuleiro_humano)
exibir_tabuleiro("Computador", tabuleiro_computador, ocultar=True)  
