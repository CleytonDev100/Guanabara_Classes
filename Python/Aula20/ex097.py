def linha(tamanhodotxt):
    print("-"*tamanhodotxt)


def escreva(txt):
    linha(len(txt)+5)
    print(f"{txt:^{len(txt)+5}}")
    linha(len(txt)+5)


escreva("Cleyton552")
escreva("LKASDLKASJDLADJSALDJASLDJSALDLASJDASLKDJSALDJASLDJASLKJD")
