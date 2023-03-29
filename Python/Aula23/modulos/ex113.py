def leiaint(txt):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print("\033[31;1m Erro! \033[m Valor invalido! (Não é um numero inteiro)")
            continue
        except KeyboardInterrupt:
            print("\n\033[31;1m Erro! \033[m O usuario preferiu não informar os dados")
            return 0
        else:
            return num


def leiaFloat(txt):
    while True:
        try:
            num = float(input(txt))
        except (ValueError, TypeError):
            print("\033[31;1m Erro! \033[m Valor invalido! (Não é um numero real)")
            continue
        except KeyboardInterrupt:
            print("\n\033[31;1m Erro! \033[m O usuario preferiu não informar os dados")
            return 0
        else:
            return num
