import random

a = random.randint(1, 10)
strzał = 0
while strzał != a and strzał != "exit":
    strzał = int(input("Odgadnij co to za liczba (wpisz od 1 do 9)"))

    if strzał == a:
        print("Brawo zgadłeś! Jak ty to zrobiłeś?")
        break
    elif strzał > a:
        print("Za duża liczba!")
        continue
    else:
        print("Za mała liczba!")
        continue
