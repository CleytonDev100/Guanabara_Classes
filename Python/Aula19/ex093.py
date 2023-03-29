dicionario = {}
lista = []
somador = 0

dicionario['Nome'] = input("Nome do jogador: ")
dicionario["Jogos"] = int(input("Quantas partidas ele jogou: "))
fim = dicionario["Jogos"]

for c in range(0, fim):
    lista.append(int(input(f"Gols feitos na partida {c}: ")))
    dicionario['GolsFeitos'] = lista.copy()

for c in lista:
    somador += c
dicionario['Somadegols'] = somador

print("=-"*20)
print(dicionario)
for k, i in dicionario.items():
    print(f"{k} tem valor {i}")
print("=-"*20)


print(f"O jogador {dicionario['Nome']} jogou {dicionario['Jogos']} partidas")
for c in range(0, len(lista)):
    print(f"    Na partida {c}, fez {lista[c]} gols")
print(f"Total de {dicionario['Somadegols']} gols")
print("=-"*20)
