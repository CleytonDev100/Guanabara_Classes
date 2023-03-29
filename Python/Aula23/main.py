try:
    n = int(input("Num1: "))
    n2 = int(input("Num2: "))
    soma = n / n2
except ValueError:
    print(f"Os dados não se coincidem!")
except ZeroDivisionError:
    print(f"Não é possivel dividir um numero por 0!")
except KeyboardInterrupt:
    print(f"OK!")
else:
    print(f"O resultado é {soma}")
finally:
    print("Volte sempre!")
