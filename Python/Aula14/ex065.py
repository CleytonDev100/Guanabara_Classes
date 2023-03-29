acu = 0
soma = 0
lista = []

while True:
    num = int(input("Numero: "))
    op = input("Continuar? [S/N]: ").upper()
    acu += 1
    soma += num
    lista.append(num)
    if op == "S":
        continue
    else:
        break

print(f"A media entre todos é {soma/acu}")
print(f"O maior numero foi {max(lista)} o menor foi {min(lista)}")
