# Taking inout from user
number = int(input("Enter the pocket number\n"))
pocketcolour = ""
# Checking conditions
if number == 0:
    pocketcolour = "green"
elif 1 <= number <= 10:
    if number % 2 == 0:
        pocketcolour = "black"
    else:
        pocketcolour = "red"
elif 11 <= number <= 18:
    if number % 2 == 0:
        pocketcolour = "red"
    else:
        pocketcolour = "black"
elif 19 <= number <= 28:
    if number % 2 == 0:
        pocketcolour = "black"
    else:
        pocketcolour = "red"
elif 29 <= number <= 36:
    if number % 2 == 0:
        pocketcolour = "red"
    else:
        pocketcolour = "black"
else:
    print("invalid number!!! enter a number between 0 and 36 inclusive")
if pocketcolour != "":
    print("The pocket colour is "+pocketcolour)
