a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = int(input("Choose a number: "))

nowa_lista = []

for i in a:
    if i < num:
        nowa_lista.append(i)

print(nowa_lista)
