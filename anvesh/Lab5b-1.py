# Checking if the num is even or odd

def is_even(num):
    if num % 2 == 0:
        return True
    return False


# Taking input from user
number = int(input("Enter the num to check if it even or odd"))
# Calling the function
result = is_even(number)
# Checking the result
if result:
    print("Number is even")
else:
    print("Number is odd")


