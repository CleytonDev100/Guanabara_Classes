acu = 0

for c in range(1, 500, 2):
    print(c, end=" ")
    if c % 3 == 0:
        acu += c
print(f"\nA soma de todos os divisiveis por 3 é {acu}")
