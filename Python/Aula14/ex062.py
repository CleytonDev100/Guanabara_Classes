numero = int(input("Primeiro fator: "))
razao = int(input("Razão da PA: "))
termo = numero
cont = 0
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{termo}", end=" ")
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos mostrar a mais: "))
print("FIM")
