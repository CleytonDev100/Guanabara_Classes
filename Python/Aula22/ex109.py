from modulos import moeda

num = float(input("Num: "))
print(f"A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}")
print(f"O dobro de {moeda.moeda(num)} é {moeda.dobrar(num, True)}")
print(f"Aumentando 10%, temos {moeda.aumentar(num, op=False)}")
print(f"Diminuindo em 10%, temos {moeda.diminuir(num, True)}")
