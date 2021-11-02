# Defining the fucntion to check if a string is palindrome or not
def check_palindrome(string):
    # Reversing a string
    reversedString = string[::-1]
    # print(reversedString)
    if string == reversedString:
        return True
    return False


# Taking the input from the user
strin = input("Enter the string to check if it is a palindrome\n")
if check_palindrome(strin):
    print("The entered string is a palindrome")
else:
    print("the entered string is not a palindrome")
