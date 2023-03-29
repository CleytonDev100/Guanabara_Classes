from random import randint

tupla = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

print("Os valores sorteados foram: ", end='')
for c in tupla:
    print(c, end=' ')

print(f"\nO maior valor sorteado foi {max(tupla)}")
print(f"O menor valor sorteado foi {min(tupla)}")