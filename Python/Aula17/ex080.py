lista = []

for c in range(0, 5):
    num = int(input("Digite um valor: "))
    if c == 0:
        print("Numero adicionado no final da lista")
        lista.append(num)
    else:
        for i, v in enumerate(lista):
            if num > v:
                lista.insert(i+1, num)
                print(f"Adicionei no indice {i+1}")
