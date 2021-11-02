try:
    num = int(input("enter a  number\n"))
#     Catching the value error exception if the input is an invalid.
except ValueError:
    print("Enter value is not a number please enter a number")
else:
    if not 1 < num < 120:
        print("number is not valid")
