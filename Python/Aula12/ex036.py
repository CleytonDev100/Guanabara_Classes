valor_casa = int(input("Valor da casa: "))
salario_pessoal = int(input("Digite seu salario: "))
anos = int(input("Em quantos anos quer financiar: "))
prestacao = valor_casa / (anos * 12)
minimo = salario_pessoal * 30 / 100

print(f"Para pagar uma casa de R${valor_casa:.2f} em {anos:.2f}")
print(f"A prestação será de R${prestacao:.2f}")
if prestacao <= minimo:
    print("Aceito")
else:
    print("Recusado")
