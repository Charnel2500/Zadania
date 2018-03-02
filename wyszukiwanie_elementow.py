list1 = ["1","8","12","5","23","4","17","11"]
list1 = [int(x) for x in list1]
list1.sort()
print(list1)
list1 = [str(x) for x in list1]
x = input("Wpisz liczbę, żeby sprawdzić czy znajduje się w liście: ")
if x in list1:
    print("Znajduje się w liście.")
else:
    print("Nie znajduje się w liście")
