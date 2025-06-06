import random

# Criação dos tabuleiros
tabuleiro_humano = [['🌊' for _ in range(10)] for _ in range(10)]
tabuleiro_computador = [['🌊' for _ in range(10)] for _ in range(10)]
exibir_computador = [['🌊' for _ in range(10)] for _ in range(10)]
exibir_humano = [['🌊' for _ in range(10)] for _ in range(10)]

# Estado do jogo
estado = {
    'restante_humano': 5,
    'restante_computador': 5
}

# Função para exibir os tabuleiros
def exibir_tabuleiro(tabuleiro, ocultar=False):
    print("    " + "  ".join(str(i) for i in range(10)))
    for i, linha in enumerate(tabuleiro):
        if ocultar:
            print(f"{i}  " + " ".join(["🌊" if celula == "⛵" else celula for celula in linha]))
        else:
            print(f"{i}  " + " ".join(linha))
    print()

# Colocar barcos do jogador
def posicao():
    exibir_tabuleiro(tabuleiro_humano)
    print("Escolha a posição das suas 5 embarcações! ⛵\n")
    for _ in range(5):
        while True:
            linha = int(input("Escolha a linha que deseja: "))
            coluna = int(input("Escolha a coluna que deseja: "))
            print()
            if 0 <= linha < 10 and 0 <= coluna < 10:
                if tabuleiro_humano[linha][coluna] == "🌊":
                    tabuleiro_humano[linha][coluna] = "⛵"
                    break
                else:
                    print("Indisponível.")
            else:
                print("Fora dos limites.")

# Colocar barcos do computador
def posicao_computador():
    for _ in range(5):
        while True:
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)
            if tabuleiro_computador[linha][coluna] == "🌊":
                tabuleiro_computador[linha][coluna] = "⛵"
                break

# Ataque do jogador
def ataque(estado):
    while True:
        linha = int(input("Escolha a linha do ataque: "))
        coluna = int(input("Escolha a coluna do ataque: "))
        print('')
        if 0 <= linha < 10 and 0 <= coluna < 10:
            if tabuleiro_computador[linha][coluna] == "⛵":
                tabuleiro_computador[linha][coluna] = "💥"
                exibir_computador[linha][coluna] = "💥"
                estado['restante_computador'] -= 1
                print("Você acertou a embarcação inimiga! 😁")
            elif tabuleiro_computador[linha][coluna] == "🌊":
                tabuleiro_computador[linha][coluna] = "❌"
                exibir_computador[linha][coluna] = "❌"
                print("Você errou! Mas não desista 💪")
            else:
                print("Você já atacou essa posição!")
                continue
            break
        else:
            print("Fora dos limites do mapa! 🗺️")

# Ataque do computador
def ataque_computador(estado):
    while True:
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)
        if tabuleiro_humano[linha][coluna] == "⛵":
            tabuleiro_humano[linha][coluna] = "💥"
            exibir_humano[linha][coluna] = "💥"
            estado['restante_humano'] -= 1
            print("O computador acertou sua embarcação! 😬")
            break
        elif tabuleiro_humano[linha][coluna] == "🌊":
            tabuleiro_humano[linha][coluna] = "❌"
            exibir_humano[linha][coluna] = "❌"
            print("O computador errou sua embarcação! 😰")
            break

def verificar_vitoria(estado):
    if estado['restante_humano'] == 0:
        print("O computador venceu a partida! 🏆")
        return True
    elif estado['restante_computador'] == 0:
        print("Você venceu a partida! Parabéns! 🏆")
        return True
    return False

posicao()
posicao_computador()

while True:
    print("\nTabuleiro do Computador:")
    exibir_tabuleiro(exibir_computador, ocultar=True)

    print("Seu Tabuleiro:")
    exibir_tabuleiro(tabuleiro_humano)

    ataque(estado)
    if verificar_vitoria(estado):
        break

    ataque_computador(estado)
    if verificar_vitoria(estado):
        break

    print(f"\n📊 Embarcações restantes:")
    print(f"👤 Você: {estado['restante_humano']} embarcações")
    print(f"💻 Computador: {estado['restante_computador']} embarcações\n")
