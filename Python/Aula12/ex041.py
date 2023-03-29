from datetime import datetime

ano = int(input("Ano de nascimento do atleta: "))
idade = datetime.today().year - ano

if idade <= 9:
    print("Mirim")
elif 9 <= idade < 14:
    print("Infantil")
elif 14 < idade <= 19:
    print("Junior")
elif idade == 20:
    print("Senior")
else:
    print("Master")
