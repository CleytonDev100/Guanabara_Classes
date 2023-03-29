from random import randint
acu = 0

while True:
    jogador = int(input("Diga um valor: "))
    op = input("[P/I]: ").upper()
    computador = randint(0, 11)
    total = jogador + computador
    print(f"Você jogou {jogador} e eu joguei {computador} somando {total}", end=" ")
    if total % 2 == 0:
        print("É PAR!")
    else:
        print("É Impar!")
    if op == "P" and total % 2 == 0:
        print("Você ganhou!")
        acu += 1
        continue
    elif op == "I" and total % 2 == 1:
        print("Você ganhou!")
        acu += 1
        continue
    else:
        print(f"Você perdeu! Ganhou {acu} vezes consecutivas")
        break

