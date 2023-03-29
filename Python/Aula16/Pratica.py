# Variavel simples
# lanche = 'Hamburger'
# lanche = 'Danone'
# lanche = 'Suco de Banana' A ultima atribuição será a printada!

# print(lanche)

# Variavel composta

lanche = ['Hamburger', 'Danone', "Suco de Banana"]
novol = lanche.append(input("Novo lanche: "))
precos = [30, 10, 10]
novop = precos.append(int(input("Preço desse lanche: ")))
matriz = [lanche, precos]
x = 0

print(f'{matriz[0][0]:.<30}', end=f'{matriz[1][0]}R$')
print(f'\n{matriz[0][1]:.<30}', end=f'{matriz[1][1]}R$')
print(f'\n{matriz[0][2]:.<30}', end=f'{matriz[1][2]}R$\n')

for c in range(0, len(matriz[0])+1):
    print(f"{matriz[x][c]:.<30}", end=' ')
    x = 1
    print(f"{matriz[x][c]}R$")
    x = 0
