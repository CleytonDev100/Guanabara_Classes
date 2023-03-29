def leiaint(txt):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print("\033[31;1m Erro!\033[m Valor invalido!")
            continue
        except KeyboardInterrupt:
            print("\n\033[31;1m Erro!\033[m O usuario preferiu não informar os dados")
            return 0
        else:
            return num


def lin(txt=42):
    return "-" * txt


def cabeça(txt):
    print(lin())
    print(txt.center(42))
    print(lin())


def menu(lista):
    cabeça("Menu")
    for i, c in enumerate(lista):
        print(f"{i} - {c}")
    op = leiaint("Escolha: ")
    return op


def cadastrar():
    nome = input("Nome: ")
    idade = leiaint("Idade: ")
    with open("ex115.txt", "a") as arquivo:
        arquivo.write(f"{nome}\n")
        arquivo.write(f"{idade}\n")


def listar(lista):
    for c in range(0, len(lista)):
        print(f"Individuo - {lista[c][0]:<30} {lista[c][1]:>3} anos")
