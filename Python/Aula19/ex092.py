dicionario = {}

dicionario["nome"] = input("Nome: ")
dicionario["idade"] = 2023 - int(input("Ano de nascimento: "))
dicionario["ctps"] = int(input("ctps (não existe 0): "))
if dicionario["ctps"] != 0:
    dicionario["Ano de Contratação"] = input("Ano de contratação: ")
    dicionario["salario"] = int(input("Salario: "))

for k, i in dicionario.items():
    print(f"{k} tem {i}")
