tabela = ("Palmeiras", "Internacional", "Fluminense", "Corinthians", "Flamengo",
          "Athletico-PR", "Atlético-MG", "América-MG", "Botafogo", "São Paulo",
          "Fortaleza", "Bragantino", "Goiás", "Chapecoense", "Ceará SC", "Coritiba",
          "Cuiabá", "Atlético-GO", "Avaí", "Juventude")
tabelas = sorted(tabela)

print("=-" * 20)
print(f"{'Os 5 primeiros colocados: ':.<20}", end='')
for c in range(0, 5):
    print(f'{tabela[c]}', end=' ')

print('')
print("=-" * 20)
print(f"Os ultimos 4 colocados: ", end='')
for i in tabela[-4:]:
    print(i, end=' ')

print('')
print("=-" * 20)
print(f"Forma alfabetica: ", end='')
for r in tabelas:
    print(r, end=' ')

print('')
print("=-" * 20)
print(f"O Chapecoense esta na {tabela.index('Chapecoense')} posição")
print("=-" * 20)