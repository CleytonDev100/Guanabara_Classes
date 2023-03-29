from datetime import datetime
maior = 0
menor = 0

for c in range(0, 8):
    ano = int(input("Ano de nascimento: "))
    idade = datetime.today().year - ano
    print(idade)
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print(f"{maior} pessoas são maiores")
print(f"{menor} pessoas são menores")
