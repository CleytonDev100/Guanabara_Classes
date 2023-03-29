from datetime import datetime

ano = int(input("Seu ano de nascimento: "))
check = datetime.today().year - ano

if check <= 16:
    print("Ainda falta um tempinho")
elif check == 17:
    print("Ja esta na hora de se alistar")
elif check >= 18:
    print(f"Você deveria se alistar a {check - (datetime.today().year - ano)+1} anos!")

