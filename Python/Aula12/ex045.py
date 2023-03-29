from random import choice
lista = ["pedra", "papel", "tesoura"]

jogador = input("[pedra/papel/tesoura]: ")
computador = choice(lista)
print(computador)

if jogador == "pedra" and computador == "tesoura":
    print("O jogador ganhou!")
elif jogador == "tesoura" and computador == "papel":
    print("O jogador ganhou!")
elif jogador == "papel" and computador == "pedra":
    print("O jogador ganhou!")
else:
    if jogador == computador:
        print("Empate!")
    else:
        print("O computador ganhou!")
