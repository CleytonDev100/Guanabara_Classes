def notas(* notas, situ=False):
    """

    :param notas: as notas dos alunos
    :param situ: (opcional) retorna se a situação da sala esta boa ou não
    :return: retorna um dicionario
    :criador: Cleyton Bezerra Miguel
    """
    dados = {}
    lista = []
    acumu = 0
    dados['total'] = len(notas)
    for c in notas:
        lista.append(c)
    big = small = lista[0]
    for c in lista:
        acumu += c
        if c > big:
            big = c
        elif c < small:
            small = c
    dados['maior'] = big
    dados['menor'] = small
    dados['media'] = acumu / len(lista)
    if situ == True:
        if dados['media'] > 5:
            dados['situacao'] = 'bom ne ai pai para'
        else:
            dados['situacao'] = 'ta uma bosta ne'
    else:
        pass
    return dados


valores = notas(5.5, 9, 10, 2, 4, 8)
print(valores)
