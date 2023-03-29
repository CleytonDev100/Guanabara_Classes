while True:
    numero = int(input("Tabuada [numero negativo para]: "))
    if numero < 0:
        break
    for c in range(0, 11):
        print(f"{numero}x{c:^3} = {numero*c:^3}")
