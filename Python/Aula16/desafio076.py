tupla = ("Pizza - 1 Fatia", 5, "Pizza - 4 Fatias", 15, "Pizza - 8 Fatias", 35,
         "Pizza - 12 Fatias", 50, "Pizza - 16 Fatias", 70, "Calzones - Qualquer Saber",
         20)
i = 1

print("-" * 50)
print(f"{'LISTAGEM DE PREÇOS':^50}")
print("-" * 50)
for c in range(0, len(tupla), 2):
    print(F"{tupla[c]:.<30} \033[31;1m{tupla[i]}R$\033[m")
    i += 2
