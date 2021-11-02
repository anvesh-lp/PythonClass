# Defining the max function
def max(num1, num2):
    # Checking the greater
    if num1 > num2:
        return num1
    return num2


# Taking inputs from the user
a = int(input("Enter number one\n"))
b = int(input("Enter number two\n"))
print("The max of two number is ",max(a, b))
