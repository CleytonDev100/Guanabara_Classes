x = 0
y = 0
lista = [[], [], []]

for c in range(0, 9):
    lista[x].append(str(input(f"Digite um valor para {x, y}: ")))
    y += 1
    if y == 3 or y == 6 or y == 9:
        x += 1
        y = 0

for v in lista:
    print(f"[ {v[0]} ]", end=" ")
    print(f"[ {v[1]} ]", end=" ")
    print(f"[ {v[2]} ]")
