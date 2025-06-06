import random

tabuleiro_humano=[['🌊' for _ in range(10)] for _ in range(10)]
tabuleiro_computador=[['🌊' for _ in range(10)] for _ in range(10)]
exibir_computador=[['🌊' for _ in range(10)] for _ in range(10)]
exibir_humano=[['🌊' for _ in range(10)] for _ in range(10)]

def exibir_tabuleiro(tabuleiro, ocultar=False):
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
    exibir_tabuleiro(tabuleiro_humano)  
    print("Escolha a posição das suas 5 embarcações! ⛵")
    print('')
    for i in range(5):
        while True:
            linha=int(input("Escolha a linha que deseja: "))
            coluna=int(input("Escolha a coluna que deseja: "))
            print('')
            
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
    restante_computador = 5
    while True:
            linha=int(input("Escolha a linha do ataque: "))
            coluna=int(input("Escolha a coluna do ataque: "))

            if 0<=linha < 10 and 0<= coluna < 10:
                if tabuleiro_computador[linha][coluna] == "⛵":
                    tabuleiro_computador[linha][coluna] = "💥"
                    exibir_computador[linha][coluna]="💥"
                    restante_computador-=1
                    print(restante_computador)
                    print("Você acertou a embarcação inimiga! 😁")
                elif tabuleiro_computador[linha][coluna] == "🌊":
                    tabuleiro_computador[linha][coluna] = "❌"
                    print("Você errou! Mas não desista 💪")
                else:
                    print("Você já atacou essa posição!")
                    continue
                break
            else:
                print("Fora dos limites do mapa! 🗺️")

def ataque_computador():
    restante_humano = 5
    linha=random.randint(0,9)
    coluna=random.randint(0,9) 

    if 0<=linha < 10 and 0<= coluna < 10:
        if tabuleiro_humano[linha][coluna] == "⛵":
            tabuleiro_humano[linha][coluna] = "💥"
            exibir_humano[linha][coluna]="💥"
            restante_humano-=1
            print(restante_humano)
            print("O computador acertou sua embarcação! 😬")
        elif tabuleiro_humano[linha][coluna] == "🌊":
            tabuleiro_humano[linha][coluna] = "❌"
            print("O computador errou sua embarcação! 😰")
        
def verificar_vitoria(humano,computador):
    if humano==0:
        print("O computador venceu a partida! 🏆")
        return True
    elif computador==0:
        print("Você venceu a partida! Parabéns! 🏆")
        return True
    else:
        return False



#Jogo:

posicao()
posicao_computador()

while True:
    exibir_tabuleiro(tabuleiro_computador)
    exibir_tabuleiro(tabuleiro_humano)

    ataque()
    ataque_computador()
    
    if verificar_vitoria(restante_humano,restante_computador):
        break
    



        
