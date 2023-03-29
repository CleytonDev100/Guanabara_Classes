from modulos import moeda

num = float(input("Digite um preço:  "))
aumento = moeda.moeda(moeda.aumentar(num))
diminu = moeda.moeda(moeda.diminuir(num))
dobro = moeda.moeda(moeda.dobrar(num))
metade = moeda.moeda(moeda.metade(num))
print(f"A metade de {moeda.moeda(num)} é {metade}")
print(f"O dobro de {moeda.moeda(num)} é {dobro}")
print(f"Aumentando {moeda.moeda(num)} em 10% = {aumento}")
print(f"Reduzindo em 10% nos temos {diminu}")
