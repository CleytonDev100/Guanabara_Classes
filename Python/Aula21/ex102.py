def fatorial(fator, show=""):
    """
    =>>Calcula o fatorial de um numero<==
    :param fator: numero a ser calculado
    :param show: (Opcional) usado para dar um ''show'', caso for verdadeiro
    :return: retorna um numero
    :Criador:Cleyton Bezerra Miguel
    """
    if show == "S":
        from time import sleep
        lista = []
        print(f"Numero {fator}: ")
        for c in range(fator-1, 0, -1):
            print(f"    {c}! = ", end=" ")
            fator *= c
            print(fator)
            lista.append(fator)
            sleep(0.5)
        print("Somando: ", end="")
        for c in lista:
            print(f"{c}", end=" ")
            sleep(0.5)
        print(f"\n  Temos \033[31;1m{fator}!\033[m")
    else:
        from math import factorial
        print(f"O fatorial do numero é {factorial(fator)}")


fatorial(int(input("Num: ")), input("Show [S/N]?").upper())
