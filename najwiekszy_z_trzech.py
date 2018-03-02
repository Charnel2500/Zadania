# Największa liczba bez użycia funkcji max()
a = int(input("Wpisz liczbę: "))
b = int(input("Wpisz drugą liczbę: "))
c = int(input("Wpisz trzecią liczbę: "))

if a>b and a>c:
    print(a)
elif b>c and b>a:
    print(b)
else:
    print(c)
    
