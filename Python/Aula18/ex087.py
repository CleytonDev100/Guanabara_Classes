matriz = [[], [], []]
somadorpares = somadorcoluna = x = y = maiorlinha = 0

for c in range(0, 9):
    matriz[x].append(int(input(f"Digite um valor para o campo {x, y}: ")))
    y += 1
    if y == 3 or y == 6 or y == 9:
        x += 1
        y = 0

for v in matriz:
    print(f" [ {v[0]} ] ", end="")
    print(f" [ {v[1]} ] ", end="")
    print(f" [ {v[2]} ] ")


print("A soma dos valores pares é: ", end="")
for v in matriz:
    for x in range(0, len(matriz)):
        num = v[x]
        if num % 2 == 0:
            somadorpares += num
print(somadorpares)

print("A terceira coluna tem a soma de: ", end="")
for v in matriz:
    num = v[2]
    somadorcoluna += num
print(somadorcoluna)

print("O maior valor da segunda linha é: ", end="")
for v in range(0, len(matriz)):
    maiorlinha = matriz[1][v]
    if matriz[1][v] > maiorlinha:
        maiorlinha = matriz[1][v]
print(maiorlinha)

