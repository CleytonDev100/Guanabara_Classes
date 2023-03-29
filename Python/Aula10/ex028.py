from random import randint

print("Vou pensar em um numero...")
pc = randint(0, 5)
gamer = int(input("Escolha um numero: "))

if gamer == pc:
    print("O jogador ganhou!")
else:
    print("O computador ganhou!")
