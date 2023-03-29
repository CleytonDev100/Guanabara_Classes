def dobra(lista):
    print(f"Valores iniciais {valores}")
    print(f"Valores dobrados: ", end=" ")
    for c in range(0, len(valores)):
        valores[c] *= 2
    print(f"{valores} ")


valores = [1, 2, 3, 4, 5, 10]
dobra(valores)

