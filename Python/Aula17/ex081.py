lista = []
des = 'y'

while des == 'y':
    num = int(input("Insert the number: "))
    lista.append(num)
    des = input("Continue: [Y/N]").lower()

print(f"were placed {len(lista)} numbers")
print(sorted(lista, reverse=True))
if 5 in lista:
    print(f"The valor five was typed {lista.count(5)} times")
else:
    print("The valor five not in list")
