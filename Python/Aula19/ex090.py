dicionario = {}

dicionario['nome'] = str(input("Nome: "))
dicionario['media'] = float(input("Média: "))

if dicionario['media'] > 5:
    dicionario['situacao'] = "boa"
elif dicionario['media'] <= 5:
    dicionario['situacao'] = "ruim"

for k, v in dicionario.items():
    print(f"{k} é {v}")
