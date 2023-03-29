nome = str(input("Nome: ")).strip().upper()

print("Tem Silva no nome: ", end="")
if nome.__contains__("SILVA"):
    print("True")
else:
    print("False")
