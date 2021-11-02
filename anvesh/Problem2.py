# Taking inputs from user
month = int(input("enter month\n"))
date = input("enter date\n")
year = int(input("enter last two digit of the year\n"))
# Checking whether it is a magic number or not
mul = int(date) * int(month)
if mul == year:
    print("The date is magic")
else:
    print("The date is not a magic number")
