# Taking inputs from user
year = int(input("enter the year\n"))
isLeap = False
# Checking if it is a leap year
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            isLeap = True
    else:
        isLeap = True
print("the year is " + ("a leap year" if isLeap else "not a leap year"))