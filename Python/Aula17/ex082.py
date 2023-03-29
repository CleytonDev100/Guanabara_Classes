lista = []
listapar = []
listaimpar = []
des = 'y'

while des == "y":
    num = int(input("Insert a number: "))
    if num % 2 == 0:
        listapar.append(num)
    elif num % 2 == 1:
        listaimpar.append(num)
    lista.append(num)
    des = input("Continue? [Y/N] ")

print(lista)
print(listapar)
print(listaimpar)
