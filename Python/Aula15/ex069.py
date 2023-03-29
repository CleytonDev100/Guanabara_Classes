acuidade = 0
acuhomens = 0
acumenores = 0

while True:
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ")
    op = input("Continuar [S/N]: ").upper()
    if idade > 18:
        acuidade += 1
    if sexo == "M":
        acuhomens += 1
    if sexo == "F" and idade < 18:
        acumenores += 1
    if op == "S":
        continue
    else:
        break

print(f"{acuidade} pessoas são maiores de 18")
print(f"{acuhomens} homens foram cadastrados")
print(f"{acumenores} mulheres são menores")
