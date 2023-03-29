frase = str(input("Frase: ")).strip().upper()

print(f"{frase.count('A')}")
print(f"{frase.index('A')}")
print(f"{frase.index('A', frase.index('A')+1)}")
