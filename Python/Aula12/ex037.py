n1 = int(input("Num: "))

op = input("[Binario/Octal/Hexadecimal]: ").lower()
if op == "binario":
    print(f"O numero {n1} - {bin(n1)}")
elif op == "octal":
    print(f"O numero {n1} - {oct(n1)}")
elif op == "hexadecimal":
    print(f"O numero {n1} - {hex(n1)}")
else:
    print(f"Informação invalida!")
