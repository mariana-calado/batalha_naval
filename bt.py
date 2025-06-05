import random

tabuleiro_humano=[['🌊' for _ in range(10)] for _ in range(10)]
tabuleiro_computador=[['🌊' for _ in range(10)] for _ in range(10)]
exibir_computador=[['🌊' for _ in range(10)] for _ in range(10)]
exibir_humano=[['🌊' for _ in range(10)] for _ in range(10)]

def exibir_tabuleiro(jogador, tabuleiro, ocultar=False):
    print("    " + "  ".join(str(i) for i in range(10)))
    for i, linha in enumerate(tabuleiro):
        if ocultar:
            print(f"{i}  " + " ".join(["🌊" if celula == "⛵" else celula for celula in linha]))
        else:
            print(f"{i}  " + " ".join(linha))
    print()

restante_humano= 5
restante_computador=5

def posicao ():
    exibir_tabuleiro("Tabuleiro", tabuleiro_humano)  
    print("Escolha a posição das suas embarcações ")
    for i in range(5):
        while True:
            linha=int(input("Escolha a linha "))
            coluna=int(input("Escolha a coluna "))
            
            if 0<=linha < 10 and 0<= coluna < 10:
                if tabuleiro_humano[linha][coluna] == "🌊":
                    tabuleiro_humano[linha][coluna] = "⛵"
                    break
                else:
                    print("Indisponível")
            else:
                print("Fora dos limites")  

def posicao_computador ():
    for i in range(5):
        while True:
            linha=random.randint(0,9)
            coluna=random.randint(0,9)  
            if tabuleiro_computador[linha][coluna] == "🌊":
                tabuleiro_computador[linha][coluna] = "⛵"
                break

def ataque():
    while True:
            linha=int(input("Escolha a linha do ataque "))
            coluna=int(input("Escolha a coluna do ataque "))

            if 0<=linha < 10 and 0<= coluna < 10:
                if tabuleiro_computador[linha][coluna] == "⛵":
                    tabuleiro_computador[linha][coluna] = "X"
                    exibir_computador[linha][coluna]="X"
                    restante_computador-=1
                    print("Acertou")
                elif tabuleiro_computador[linha][coluna] == "🌊":
                    tabuleiro_computador[linha][coluna] = "X"
                    print("Errou")
                else:
                    print("Já atacou essa posição")
                    continue
                break
            else:
                print("Fora dos limites do mapa! 🗺️")

def ataque_computador():
        while True:
            linha=random.randint(0,9)
            coluna=random.randint(0,9) 

            if 0<=linha < 10 and 0<= coluna < 10:
                if tabuleiro_humano[linha][coluna] == "⛵":
                    tabuleiro_humano[linha][coluna] = "X"
                    exibir_humano[linha][coluna]="X"
                    restante_humano-=1
                    print("O computador acertou")
                elif tabuleiro_humano[linha][coluna] == "🌊":
                    tabuleiro_humano[linha][coluna] = "X"
                    print("O computador errou")



posicao()
posicao_computador()
exibir_tabuleiro(tabuleiro_humano)
exibir_tabuleiro(tabuleiro_computador, ocultar=True)




        
