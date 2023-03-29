from random import randint

palpites = 0

while True:
    computador = randint(0, 10)
    jogador = int(input("Adivinhe o numero que pensei: "))
    if jogador == computador:
        break
    else:
        palpites += 1


print(f"Acertou! Você precisou de {palpites} tentativas")
