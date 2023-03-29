numeros = []


def sorteio(lista):
    from random import randint
    for c in range(0, 5):
        lista.append(randint(0, 10))
    print(f"Somando os valores pares da lista {lista}.")


def somapar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(soma)


sorteio(numeros)
somapar(numeros)
