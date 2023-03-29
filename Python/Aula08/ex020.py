from random import shuffle

al1 = str(input("Aluno: "))
al2 = str(input("Aluno: "))
al3 = str(input("Aluno: "))
al4 = str(input("Aluno: "))
lista = [al1, al2, al3, al4]
shuffle(lista)

print(f"A ordem será {lista}")
