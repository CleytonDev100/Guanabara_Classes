while True:
    n1 = int(input("Valor1: "))
    n2 = int(input("Valor2: "))
    op = int(input("[1] - Somar \n[2] - Multiplicar\n[3] - maior \n[4] - novos números \n[5] - sair do programa\n"
                   "Escolha: "))
    if op == 1:
        print(f"A soma é {n1+n2}")
    elif op == 2:
        print(f"A soma é {n1 * n2}")
    elif op == 3:
        if n1 > n2:
            print(f"O maior é {n1}")
        elif n2 > n1:
            print(f"O maior é {n2}")
        else:
            print("Ambos são iguais")
    elif op == 4:
        continue
    elif op == 5:
        break
