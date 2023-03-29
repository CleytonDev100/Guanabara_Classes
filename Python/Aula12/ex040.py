n1 = float(input("Nota1: "))
n2 = float(input("Nota2: "))
media = n1 + n2 / 2

if media < 5.0:
    print("\033[31;1mReprovado!\033[m")
elif 5.0 <= media < 6.9:
    print("\033[33;1mRecuperação\033[m")
elif 7.0 < media:
    print("\033[32;1mAprovado\033[m")


