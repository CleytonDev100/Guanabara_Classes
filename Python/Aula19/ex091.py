from random import randint
from time import sleep
dicionario = {}

for c in range(0, 4):
    dicionario[f"jogada{c}"] = randint(0, 100)

print("Valores sorteados: ")
for c in range(0, 4):
    print(f"    Jogador {c}: {dicionario[f'jogada{c}']}")
    sleep(1)

print("Ranking dos jogadores: ")
ranking = sorted(dicionario.values(), reverse=True)
for c in range(0, 4):
    print(f"     Lugar {c}: {ranking[c]}")
    sleep(1)
