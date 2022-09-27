import random

while True:
    Escolhas = ["pedra", "papel", "tesoura"]

    Computador = random.choice(Escolhas)
    Jogador = None

    while Jogador not in Escolhas:
        Jogador = input("pedra, papel, ou tesoura?: ").lower()

    if Jogador == Computador:
        print("Computador: ", Computador)
        print("Jogador: ", Jogador)
        print("Empate!")

    elif Jogador == "pedra":
        if Computador == "papel":
            print("Computador: ", Computador)
            print("Jogador: ", Jogador)
            print("Você perdeu!")
        if Computador == "tesoura":
            print("Computador: ", Computador)
            print("Jogador: ", Jogador)
            print("Você ganhou!")

    elif Jogador == "tesoura":
        if Computador == "pedra":
            print("Computador: ", Computador)
            print("Jogador: ", Jogador)
            print("Você perdeu!")
        if Computador == "papel":
            print("Computador: ", Computador)
            print("player: ", Jogador)
            print("Você ganhou!")

    elif Jogador == "papel":
        if Computador == "tesoura":
            print("Computador: ", Computador)
            print("Jogador: ", Jogador)
            print("Você perdeu!")
        if Computador == "pedra":
            print("Computador: ", Computador)
            print("Jogador: ", Jogador)
            print("Você ganhou!")

    Jogar_novamente = input("Quer jogar novamente? (sim/não): ").lower()

    if Jogar_novamente != "sim":
        break

print("Obrigado por jogar! Tchau!!")
