def aumentar(n, op=False):
    n = n * (10 / 100) + n
    if op:
        return moeda(n)
    else:
        return n


def diminuir(n, op=False):
    n = n * (10/100)
    if op:
        return moeda(n)
    else:
        return n


def dobrar(n, op=False):
    n = n * 2
    if op:
        return moeda(n)
    else:
        return n


def metade(n, op=False):
    n = n / 2
    if op:
        return moeda(n)
    else:
        return n


def lin(elemento, lentxt):
    lentxt += 5
    print(f"{elemento}"*lentxt)


def moeda(msg):
    return f"R${msg:.0f},00"


def resumo(n, aumen, redu):
    lin("-", len("Resumo do valor"))
    print(f"{'Resumo do valor':^{len('Resumo do valor')+5}} ")
    lin("-", len("Resumo do valor"))
    print(f"{f'O dobro do {n} é {dobrar(n, True)}':^{len('Resumo do valor')+5}}")
    print(f"A metade de {n} é {metade(n, True)}")
    print(f"O {n} aumentado em {aumen}% é {aumentar(n, True)}")
    print(f"o {n} reduzido em {redu}% é {diminuir(n, True)}")
