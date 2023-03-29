def maior(* num):
    print("*"*20)
    print("Analisando os valores...")
    for c in num:
        print(f"{c}", end=" ")
    print(f"Foram {len(num)} os valores passados")
    big = 0
    for c in range(0, len(num)):
        if num[c] > big:
            big = num[c]
    print(f"O maior valor é {big}")
    print("*" * 20)


maior(3, 4, 9, 8, 7)
maior(1, 2)
maior(0)
maior()
