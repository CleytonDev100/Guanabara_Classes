lista = []
dados = []
nump = 0
maisp = menosp = 0
des = 'y'

while des == 'y':
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Peso: ")))
    lista.append(dados.copy())
    dados.clear()
    des = str(input("[Y/N]: ")).lower()

print("Foram cadastradas ", end="")
for c in lista[0:][0]:
    nump += 1
print(f"{nump} pessoas", end=" ")

print("\nO maior peso foi de ", end="")
for c in lista:
    maisp = lista[0][1]
    if c[1] > maisp:
        maisp = c[1]
print(f"{maisp}Kg. Peso de ", end="")
for v in lista:
    if v[1] == maisp:
        print(v[0], end=" ")

print("\nO menor peso foi de ", end="")
for c in lista:
    menosp = lista[0][1]
    if c[1] < menosp:
        menosp = c[1]
print(f"{menosp}Kg. Peso de ", end="")
for v in lista:
    if v[1] == menosp:
        print(v[0], end=" ")
