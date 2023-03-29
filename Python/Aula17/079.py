lista = []
des = 'y'
while des == 'y':
    num = int(input("Num: "))
    if num not in lista:
        lista.append(num)
    else:
        print("Numero ja adicionado!")
    des = input("[Y/N]: ")

print(sorted(lista))
