def leiaint(msg):
    while True:
        num = str(input(msg)).strip()
        if num.isnumeric():
            int(num)
            break
        else:
            print("\033[31;1mErro! Valor invalido!\033[m")
    return num


num = leiaint("Digite um valor: ")
print(f"Você digitou o numero {num}")
