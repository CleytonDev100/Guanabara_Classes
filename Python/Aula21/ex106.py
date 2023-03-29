def ajuda(msg):
    while True:
        op = input(msg).lower()
        if op == "fim":
            break
        print(f"\033[31;0;3mAcessando o manual do comando '{op}'\033[m")
        help(op)


ajuda("Escolha uma função: ")
