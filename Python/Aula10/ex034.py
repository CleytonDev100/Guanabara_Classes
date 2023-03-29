salario = float(input("Salario: "))

if salario > 1250:
    salario = salario + (salario * (10 / 100))
    print(f"Seu salario teve um aumento de 10% se tornando {salario}R$")
else:
    salario = salario + (salario * (15 / 100))
    print(f"Seu salario teve um aumento de 15% se tornando {salario}R$")
