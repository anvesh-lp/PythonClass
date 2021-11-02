amount = input("enter the sales of the each day in a week separated with a space\n")
listOfAmounts = amount.split(" ")
count = 0
newList = []
for i in range(len(listOfAmounts)):
    if listOfAmounts[i].isdigit():
        newList.append(int(listOfAmounts[i]))
tupleOfAmount = tuple(newList)
s = 0
for i in tupleOfAmount:
    s += i
print("Total sales of the week " + str(s))
