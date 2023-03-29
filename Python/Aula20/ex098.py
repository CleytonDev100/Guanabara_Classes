from time import sleep


def lin():
    print("")
    print("-"*30)


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo = passo + passo * (-2)
    elif inicio < fim:
        c = inicio
        print(f"De {passo} em {passo}: ", end="")
        while c <= fim:
            print(f"{c}", end=" ")
            sleep(0.5)
            c += passo
        lin()
    elif inicio > fim:
        c = inicio
        print(f"De {passo} em {passo}: ", end="")
        while c >= fim:
            print(f"{c}", end=" ")
            sleep(0.5)
            c -= passo
        lin()


contador(1, 10, 1)
contador(10, 0, 2)
print("Personalize sua contagem agora!")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
