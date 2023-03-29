n1 = int(input("Digite o 0 valor: "))
n2 = int(input("Digite o 1 valor: "))
n3 = int(input("Digite o 2 valor: "))
n4 = int(input("Digite o 3 valor: "))
tupla = (n1, n2, n3, n4)
    
print(f"O numeros 9 apareceu {tupla.count(9)} vezes")

if 3 in tupla:
    print(f"O numero 3 apareceu na posição {tupla.index(3)}")
else:
    print("O numero 3 não foi encontrado em nenhuma posição")

print("Os numeros pares foram:", end='')
for x in tupla[0:]:
    if x % 2 == 0:
        print(end=f' {x}')
