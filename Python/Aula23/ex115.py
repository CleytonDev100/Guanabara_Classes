from ex115 import *
lista = []

while True:
    op = menu(["Cadastrar novas pessoas", "Listar pessoas cadastradas", "Sair do programa"])
    if op == 0:
        cabeça("Cadastrar nova pessoa")
        cadastrar()

    elif op == 1:
        cabeça("Pessoas ja cadastradas")
        dados = open("ex115.txt")
        lista = []
        lista2 = []
        cont = 0
        for c in dados:
            lista2.append(c.strip("\n"))
            cont += 1
            if cont % 2 == 0:
                lista.append(lista2.copy())
                lista2.clear()
        listar(lista)

    elif op == 2:
        cabeça("Volte sempre!")
        break
