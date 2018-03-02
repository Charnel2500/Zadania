print('''Witamy w naszym słowniku urodzeń. Znamy datę urodzin trzech osób:
Einstein, Musk, Jobs''')
urodziny = {"Einstain":'22.07.1922', "Musk":'17.04.1961', "Jobs":'15.12.1955'}
wpis = input("Czyją datę urodzin chcesz poznać?")
if wpis == "Einstain":
    print(urodziny["Einstain"])
elif wpis == "Musk":
    print(urodziny["Musk"])
elif wpis == "Jobs":
    print(urodziny["Jobs"])
else:
    print("Zły wpis")
