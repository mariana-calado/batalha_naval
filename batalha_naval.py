import random
import time

tabuleiro_humano = [['🌊' for _ in range(10)] for _ in range(10)]
tabuleiro_computador = [['🌊' for _ in range(10)] for _ in range(10)]
exibir_computador = [['🌊' for _ in range(10)] for _ in range(10)]
exibir_humano = [['🌊' for _ in range(10)] for _ in range(10)]

estado = {
    'restante_humano': 5,
    'restante_computador': 5
}

print('')
print('   ⚔️ 🚢   BATALHA NAVAL   🚢 ⚔️')
print('')

def mostrar_menu():
    while True:
        print('1. Iniciar Jogo')
        print('2. Ver Regras')
        print('3. Sair')
        escolha = input('\nDigite uma das opções (1-3): ')
        print()

        if escolha == '1':
            return
          
        elif escolha == '2':

            print('📜 REGRAS DO JOGO 📜\n')
            print('🌊 O objetivo do jogo é afundar todas as embarcações inimigas antes que ele afunde as suas.\n')
            
            print('🚢 POSICIONAMENTO:')
            print('- O tabuleiro tem o tamanho de 10 linhas por 10 colunas (10x10).')
            print('- Você e o computador terão 5 embarcações cada, de tamanho 1 (ou seja, ocupam 1 célula).')
            print('- Para posicionar cada embarcação, você informará duas coisas:')
            print('   1️⃣  A linha (número entre 0 e 9).')
            print('   2️⃣  A coluna (número entre 0 e 9).')
            print('- As embarcações não podem ocupar o mesmo espaço, então preste atenção! ⛵\n')

            print('🎯 ATAQUES:')
            print('- Depois do posicionamento, o jogo começa em rodadas alternadas.')
            print('- Em cada rodada, você informará:')
            print('   🗣️  A linha e a coluna do local que deseja atacar.')
            print('- O computador também atacará automaticamente na vez dele.')
            print('- Um acerto será marcado com 💥 e um erro com ❌.\n')

            print('🏁 VITÓRIA:')
            print('- O primeiro a atingir todas as 5 embarcações do oponente vence a batalha! 🏆\n')

            input('Pressione Enter para voltar ao menu...')

        elif escolha == '3':
            print('Saindo do jogo... Até a próxima! 👋')
            exit()
        else:
            print('Opção inválida! Tente novamente.\n')


def exibir_tabuleiro(tabuleiro, ocultar=False):
    print("    " + "  ".join(str(i) for i in range(10)))
    for i, linha in enumerate(tabuleiro):
        if ocultar:
            print(f"{i}  " + " ".join(["🌊" if celula == "⛵" else celula for celula in linha]))
        else:
            print(f"{i}  " + " ".join(linha))
    print()

def posicao():
    exibir_tabuleiro(tabuleiro_humano)
    time.sleep(1.5)
    print("Escolha a posição das suas 5 embarcações! ⛵\n")
    time.sleep(1.5)
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

def posicao_computador():
    for _ in range(5):
        while True:
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)
            if tabuleiro_computador[linha][coluna] == "🌊":
                tabuleiro_computador[linha][coluna] = "⛵"
                break

def ataque(estado):
    while True:
        print('')
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
        
def tabuleiros_lado(tab1, tab2, ocultar_tab2=False):
    print("Seu Tabuleiro:" + " " * 34 + "Tabuleiro do computador:")
    cabecalho = "     " + "   ".join(str(i) for i in range(10)) + "          " + "   ".join(str(i) for i in range(10))
    print(cabecalho)
    
    for i in range(10):
        linha_tab1 = "  ".join(tab1[i])
        if ocultar_tab2:
            linha_tab2 = "  ".join(["🌊" if cel == "⛵" else cel for cel in tab2[i]])
        else:
            linha_tab2 = "  ".join(tab2[i])
        print(f"{i:<2}  {linha_tab1}     {i:<2}  {linha_tab2}")

def verificar_vitoria(estado):
    if estado['restante_humano'] == 0:
        print("O computador venceu a partida! 🏆")
        return True
    elif estado['restante_computador'] == 0:
        print("Você venceu a partida! Parabéns! 🏆")
        return True
    return False


mostrar_menu()

posicao()
posicao_computador()

while True:
    time.sleep(1)

    print("\nRodada Atual:")
    print('')

    time.sleep(0.5)

    tabuleiros_lado(tabuleiro_humano, exibir_computador, ocultar_tab2=True)

    time.sleep(1.5)

    ataque(estado)

    if verificar_vitoria(estado):
        break

    time.sleep(1.5)

    ataque_computador(estado)

    if verificar_vitoria(estado):
        break

    time.sleep(0.5)

    print(f"\n📊 Embarcações restantes:")

    time.sleep(0.5)

    print(f"👤 Você: {estado['restante_humano']} embarcações")
    
    time.sleep(0.5)

    print(f"💻 Computador: {estado['restante_computador']} embarcações\n")
