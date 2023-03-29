def area(largura, comprimento):
    areatotal = largura * comprimento
    print(f"A área total do terreno é {areatotal}M")


area(float(input("Largura [m]: ")), float(input("Comprimento [m]: ")))
