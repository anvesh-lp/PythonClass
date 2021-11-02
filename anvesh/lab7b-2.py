# Taking input from the user
while True:
    try:
        noOfDays = int(input("Enter the number of days\n"))
        break
    except ValueError:
        print("Invalid input..please try again")

amount = 1
days = 1
print("day      salary")
while days <= noOfDays:
    print(str(days) + "         " + str(amount))
    days += 1
    amount += amount
print("total amount in dollars = ", (amount/2)/100)
