acuidade = 0
acumulheres = 0
lista = []

for c in range(0, 4):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ")
    acuidade += idade
    if sexo == "M":
        lista.append([nome, idade])
    elif sexo == "F" and idade < 20:
        acumulheres += 1

print(f"A média de idade é {acuidade/4}")
print(f"O homem com a maior idade é {max(lista)}")
print(f"Temos {acumulheres} mulheres com menos de 20 anos")
