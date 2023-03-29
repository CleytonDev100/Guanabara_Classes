dicionario = {}
dados = []

op = int(input("Quantas pessoas gostaria de adicionar: "))
for c in range(0, op):
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Idade: ")))
    dicionario[f'nome{c}'] = dados[0]
    dicionario[f'idade{c}'] = dados[1]
    dados.clear()

for c in range(0, op):
    print(f"A pessoa {dicionario[f'nome{c}']} tem {dicionario[f'idade{c}']} anos")
