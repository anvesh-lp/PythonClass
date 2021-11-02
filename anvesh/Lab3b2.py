# Initial List
initialList = [2, 3, -1, -4, 0, 10, 3, 2]
# Adding the list
initialList.append(-3)
initialList.insert(0, -100)
count = 0
# Sorting the list
initialList.sort()
#Looping through the list
while count < len(initialList):
    print(initialList[count])
    count += 1
