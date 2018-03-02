liczba = int(input("Wprowadź liczbę: "))
nowa_lista = range(1, liczba+1)


dzielniki = []
for i in nowa_lista:
    if liczba % i == 0:
        dzielniki.append(i)
print(dzielniki)
