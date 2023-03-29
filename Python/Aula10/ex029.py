velo = int(input("Velocidade do carro: "))

if velo > 80:
    multa = (velo - 80) * 7
    print(f"Você foi multado no valor de {multa}R$")
else:
    print("Tudo nos conformes!")
