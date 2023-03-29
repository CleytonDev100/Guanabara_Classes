gasto = 0
maiores = 0
lista = []

while True:
    nome = input("Nome do produto: ")
    preco = int(input("Preço do produto: "))
    op = input("Continuar [S/N]: ").upper()
    gasto += preco
    if preco > 1000:
        maiores += 1
    lista.append([nome, preco])
    if op == "S":
        continue
    else:
        break

print(f"O total gasto foi {gasto}")
print(f"{maiores} produtos custaram mais de 1000R$")
print(f"O produto mais barato foi {min(lista)}")
