menor = 0
maior = 0
lista = []


for c in range(0, 5):
    num = int(input(f"{c}: "))
    lista.append(num)
    if c == 0:
        menor = maior = num
    else:
        if num > maior:
            maior = num
        elif num < menor:=
            menor = num

print(lista)
print(maior, menor)
print(f"O maior valor digitado foi {maior} nas posições: ", end="")
for i, v in enumerate(lista):
    if v == maior:
        print(i, end=" ")
print(f"\nO menor valor digitado foi {menor} nas posições: ", end="")
for i, v in enumerate(lista):
    if v == menor:
        print(i, end=" ")
