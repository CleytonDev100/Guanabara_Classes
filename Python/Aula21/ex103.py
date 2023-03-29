def ficha(nome="<desconhecido>", gols=0):
    print(f"O jogador {nome} fez {gols} gols")


n = str(input("Nome do jogador: ")).strip()
g = str(input("Gols do jogador: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == "":
    ficha(gols=g)
else:
    ficha(n, g)
