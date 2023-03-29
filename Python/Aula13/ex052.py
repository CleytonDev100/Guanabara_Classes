num = int(input("Numero: "))

for c in range(1, num+1):
    if num % c == 0:
        print(f"\033[31;1m{c}\033[m - O numero é primo")
    else:
        print(f"{c} - O numero não é primo")
