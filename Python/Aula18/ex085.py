lista = [[], []]

for c in range(0, 7):
    num = int(input("N: "))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

print(f"Impares: {sorted(lista[1][:])}")
print(f"Pares :{sorted(lista[0][:])}")
