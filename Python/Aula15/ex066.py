acu = 0
valor = 0

while True:
    numero = int(input("Num: "))
    if numero == 999:
        break
    acu += 1
    valor += numero
    print(valor)

print(f"Foram digitados {acu} numeros é a soma entre eles é {valor}")
