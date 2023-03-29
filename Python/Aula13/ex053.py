frase = input("Frase: ").strip().lower()
frase.split()
junto = ''.join(frase)
inverso = ''

for c in range(len(junto) -1, -1, -1):
    inverso += junto[c]

if inverso == junto:
    print("Essa palavra é um palindromo")
else:
    print("Essa palavra não é um palindromo")

