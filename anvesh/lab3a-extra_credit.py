# Declaring a list
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
li = []
# Taking inputs from the user
for i in range(12):
    print("enter the rainfall for the month ", months[i])
    # Adding to the list
    li.append(int(input()))

print("Total rainfall of the year : ", sum(li))
print("Average monthly rainfall : ", sum(li) / len(li))
# Getting highest and lowest rainfalls
highest = max(li)
hindex = li.index(highest)
loswets = min(li)
lindex = li.index(loswets)
print("Hiighest rainfall of the year is " + str(highest) + " in " + months[hindex])
print("Lowest rainfall of the year is " + str(loswets) + " in " + months[lindex])
