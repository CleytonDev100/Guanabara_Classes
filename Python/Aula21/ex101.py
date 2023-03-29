idade = 0


def voto(anonascimento):
    from datetime import date
    """
    =>> VERIFICA SE O USUARIO É OBRIGADO, OU NÃO, A VOTAR <<=
    :param anonascimento: Ano de nascimento do usuario
    :return: Returna os valores "Negado" caso for de menor "Obrigatorio" caso for de maior e "Opcional" caso for idoso
    """
    global idade
    ano = date.today().year
    idade = ano - anonascimento
    if idade < 16:
        return "NEGADA!"
    elif 17 <= idade <= 60:
        return "OBRIGATORIA!"
    elif idade > 60:
        return "OPCIONAL"


op = int(input("Qualé seu ano de nascimento: "))
retornador = voto(op)
print(f"O usuario tem {idade} anos de idade então a votação é {retornador}")
