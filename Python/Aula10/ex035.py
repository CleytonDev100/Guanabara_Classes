s1 = float(input("Segmento 1: "))
s2 = float(input("Segmento 2: "))
s3 = float(input("Segmento 3: "))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print("É possivel formar um triangulo!")
else:
    print("Não é possivel formar um triangulo!")
