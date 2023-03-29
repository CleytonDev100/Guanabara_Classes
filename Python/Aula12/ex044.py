valor = int(input("Valor do produto: "))
op = int(input("Forma de pagamento: \n[0] - À vista dinheiro \n[1] - À vista cartão \n[2] - 2x no cartão \n"
           "[3] - 3x no cartão \nEscolha: "))

if 0 == op:
    desconto = valor - (valor * 10 / 100)
    print(f"O valor final fica por {desconto}")
elif 1 == op:
    desconto = valor - (valor * 5 / 100)
    print(f"O valor final fica por {desconto}")
elif 2 == op:
    print(f"O preço continua normal {valor}")
elif 3 == op:
    juros = valor * (20 / 100) * 3
    print(f"O valor com 20% de juros fica {valor+juros}")
