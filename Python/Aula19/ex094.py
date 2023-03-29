dados = {}
lista = []
des = 'y'
media = 0

while des == 'y':
    dados['nome'] = input("Nome: ")
    dados['sexo'] = input("Sexo: ").upper()
    if dados['sexo'] != "M" and dados['sexo'] != "F":
        while dados['sexo'] != "M" and dados['sexo'] != "F":
            dados['sexo'] = input("[M/F]: ").upper()
    dados['idade'] = int(input("Idade: "))
    lista.append(dados.copy())
    des = input("Continuar: [Y/N]: ").lower()

print(f"Foram cadastradas {len(lista)} pessoas!")

for c in range(0, len(lista)):
    media += lista[c]["idade"]

print(f"Média de idade = {media / len(lista)}")

print("As mulheres são: ", end="")
for c in range(0, len(lista)):
    if lista[c]["sexo"] == "F":
        print(lista[c]["nome"], end=" ")

print("\nPessoas com idade acima da média são: ", end="")
for c in range(0, len(lista)):
    if lista[c]["idade"] > media / len(lista):
        print(lista[c]["nome"], end=" ")
