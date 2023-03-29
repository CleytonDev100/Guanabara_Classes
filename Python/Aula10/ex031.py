kms = int(input("Kms rodados: "))

if kms > 200:
    valor = (kms - 200) * 0.45
    print(f"O valor da passagem foi {200 * 0.45 + valor}R$")
else:
    valor = (kms - 200) * 0.50
    print(f"O valor da passagem foi {200 * 0.50 + valor}R$")
