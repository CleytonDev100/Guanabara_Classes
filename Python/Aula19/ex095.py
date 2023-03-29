dados = {}
lista = []
gols = []
op = int(input("Quantos jogadores adicionar: "))
total = 0

for c in range(0, op):
    dados['nome'] = input("Nome do jogador: ")
    dados['partidas'] = int(input("Partidas jogadas: "))
    for e in range(0, dados['partidas']):
        gols.append(int(input(f"Gols na partida {e}: ")))
    dados['gols'] = gols.copy()
    gols.clear()
    lista.append(dados.copy())


for c in range(0, len(lista[0]['gols'])):
    print(lista[0]['gols'][c])

des = 'y'
while des == 'y':
    print(f"cod nome {'gols':^10} {'total':>10}")
    print("_"*40)
    for c in range(0, len(lista)):
        for e in range(0, len(lista[c]['gols'])):
            total += lista[c]['gols'][e]
        print(f"{c:>3} {lista[c]['nome']:^1} {lista[c]['gols']} {total:^13}")
        total = 0
    op = int(input("Fazer o levantamento de qual jogador [999 para]: "))
    if op > len(lista):
        while op > len(lista):
            op = int(input("Tenta denovo [999 para]: "))
    elif op < len(lista):
        print(f"Levantamento de {lista[op]['nome']}")
        for c in range(0, len(lista[op]['gols'])):
            print(f"    No {c} jogo fez {lista[op]['gols'][c]} gols")
    elif op == 999:
        des = 'aipaipara'
    des = input("Mais algum jogador? [Y/N]: ").lower()
