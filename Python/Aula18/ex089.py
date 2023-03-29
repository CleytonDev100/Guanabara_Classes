matriz = []
dados = []
des = 'y'

while des == 'y':
    dados.append(input("Nome do aluno: "))
    dados.append(int(input("Nota 1 do aluno: ")))
    dados.append(int(input("Nota 2 do aluno: ")))
    matriz.append(dados.copy())
    dados.clear()
    des = input("[Y/N]: ").lower()

des = input("Gostaria de ver as notas de algum aluno [Y/N]: ").lower()
if des == "y":
    while des == "y":
        for c in range(0, len(matriz)):
            print("-"*20)
            print(f"\033[31;1mAluno: {matriz[c][0]}\033[m")
            print(f"Média do aluno: {matriz[c][1] + matriz[c][2] / 2}")
            print("-"*20)
        op = input("Gostaria de ver a nota de qual aluno? ")
        for c in matriz:
            if op == c[0]:
                print(f"As notas de {c[0]} foram {c[1]}, {c[2]}")
        des = input("Gostaria de ver as de outro [Y/N]: ").lower()
else:
    print("ok!")
