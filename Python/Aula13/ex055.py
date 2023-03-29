maior = 0
menor = 0

for c in range(0, 5):
    peso = int(input("Peso: "))
    if c == 0:
        maior = c
        menor = c
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f"O maior peso lido foi {maior}")
print(f"O menor peso lido foi {menor}")
