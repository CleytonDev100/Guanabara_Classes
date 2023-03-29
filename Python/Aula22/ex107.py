from modulos import moeda

num = float(input("Digite um preço:  "))
aumento = moeda.aumentar(num)
diminu = moeda.diminuir(num)
dobro = moeda.dobrar(num)
metade = moeda.metade(num)
print(f"A metade de {num} é {metade}")
print(f"O dobro de {num} é {dobro}")
print(f"Aumentando {num} em 10% = {aumento}")
print(f"Reduzindo em 10% nos temos {diminu}")

