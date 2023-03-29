from random import randint
from time import sleep

matriz = []
dados = []
op = int(input("Quantos jogos devo fazer: "))

for c in range(0, op):
    dados = [randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60),
             randint(0, 60)]
    matriz.append(dados.copy())
    dados.clear()

print(f"Matriz: {matriz}\n")

print("Esses foram seus jogos: ")
for c in range(0, len(matriz)):
    print(f"Jogo {c}: {matriz[c]}")
    sleep(1)
