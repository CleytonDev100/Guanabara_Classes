tupla = ("Guanabara", "Mae", "Curso", "Gratis", "Break", "While", "For", "Rodrigo"
         , "Danone", "Simba", "Guanaba")
color = '\033[31;1m'

for c in range(0, len(tupla)):
    print(f"\n{tupla[c]} = ", end='')
    for x in tupla[c][0:]:
        if x == 'a':
            print(color, end='a \033[m')
        elif x == 'e':
            print(color, end='e \033[m')
        elif x == 'i':
            print(color, end='i \033[m')
        elif x == 'o':
            print(color, end='o \033[m')
        elif x == 'u':
            print(color, end='u \033[m')
