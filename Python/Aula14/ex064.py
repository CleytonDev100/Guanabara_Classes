acu = 0
soma = 0

while True:
    num = int(input("Numero [999 para]: "))
    acu += 1
    soma += num
    if num == 999:
        break

print(f"Foram digitador {acu} numeros a soma entre eles é {soma}")
