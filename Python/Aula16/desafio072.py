numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze'
           , 'dezesseis', 'dezessete', 'dezoito', 'dezenovo', 'vinte')

indice = int(input("Digite um numero entre 0 e 20: "))
while indice < 0 or indice > 20:
    indice = int(input("Digite apenas numeros entre 0 e 20: "))

print(f"Você digitou o numero {numeros[indice]}")
