acu = 0

for c in range(0, 7):
    num = int(input(f"Num{c}: "))
    if num % 2 == 0:
        acu += num

print(f"A soma de todos os pares é {acu}")
