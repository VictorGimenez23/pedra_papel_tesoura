from random import randint

jogador = 0
computador = 0
usuario = 0
empates = 0

def placar():
    print("=" * 8 + " PLACAR " + "=" * 8)
    print(f"Computador: {computador}")
    print(f"Usuario: {usuario}")
    print(f"Empates: {empates}")
    print("=" * 24)

def menu():
    print("=" * 9 + " MENU " + "=" * 9)
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    print("4 - Encerrar jogo")

def regras():
    print("=" * 8 + " REGRAS " + "=" * 8)
    print("- Pedra quebra Tesoura")
    print("- Papel embrulha Pedra")
    print("- Tesoura corta Papel")

menu()
regras()
jogadaUsu = 0

while (jogadaUsu != 4):
    placar()
    jogadaComp = randint(1,3)
    jogadaUsu = int(input("Digite a opção desejada: "))
    print("JO-KENNN-PÔOOO")

    print(f"Usuário jogou: {jogadaUsu}")
    print(f"Computador jogou: {jogadaComp}")

    if(jogadaComp == 1):
        if(jogadaUsu == 1):
            print("Empatou!!!")
            empates =empates + 1
        elif(jogadaUsu == 2):
            print("Usuário ganhou!!!")
            usuario = usuario + 1
        elif(jogadaUsu == 3):
            print("Computador ganhou!!!")
            computador = computador + 1

    elif(jogadaComp == 2):
        if(jogadaUsu == 1):
            print("Computador ganhou!!!")
            computador = computador + 1
        elif(jogadaUsu == 2):
            print("Empatou!!!")
            empates = empates + 1
            print("Usuário ganhou!!!")
        elif(jogadaUsu == 3):
            usuario = usuario + 1

    elif(jogadaComp == 3):
        if(jogadaUsu == 1):
            print("Usuário ganhou!!!")
            usuario = usuario + 1
        elif(jogadaUsu == 2):
            print("Computador ganhou!!!")
            computador = computador + 1
        elif(jogadaUsu == 3):
            print("Empatou!!!")
            empates = empates + 1

    if(jogadaUsu <= 0 or jogadaUsu > 4 ):
        print("Jogada inválida!!! Jogue de novo!!!")

print("Usuário encerrou o jogo!!!")