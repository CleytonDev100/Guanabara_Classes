x = 0
y = 0

expression = input("Insert: ")
for c in expression:
    if c == "(":
        y += 1
    elif c == ")":
        x += 1

if x == y:
    print("Boa expressão!")
else:
    print("Expressão errada!")
