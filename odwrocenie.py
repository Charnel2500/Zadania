wyraz = input("Wpisz jakiś wyraz: ")
wyraz=str(wyraz)
odwrócenie=wyraz[::-1]
print(odwrócenie)
if wyraz == odwrócenie:
    print("Ten wyraz jest lustrzany")
else:
    print("Ten wyraz nie jest lustrzany")
