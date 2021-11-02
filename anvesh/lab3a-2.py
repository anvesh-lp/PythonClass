# Taking input from the user
noOfDays = int(input("Enter the number of days\n"))
amount = 1
days = 1
print("day      salary")
while days <= noOfDays:
    print(str(days) + "         " + str(amount))
    days += 1
    amount += amount
print("total amount in dollars = ", (amount/2)/100)
