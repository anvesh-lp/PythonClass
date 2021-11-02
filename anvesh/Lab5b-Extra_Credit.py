# Defining the function to check password
def check_password(password):
    digit = False
    uppercase = False
    lowerCase = False
    # Checking if the password length is greater than 8
    if len(password) < 8:
        return False
    for i in password:
        # Checking if the character is digit or not
        if (i + "").isdigit():
            digit = True
        # Checking if the character is upper or not
        if i.isupper():
            uppercase = True
        # Checking if the character is lower or not
        if i.islower():
            lowerCase = True
    # returning the final validity of the password
    return digit and uppercase and lowerCase


# Writing the while loop to prompt the user to enter the valid password until it meets the requirements
while True:
    passw = input("enter the password\n")
    # Calling the check_password function function tp check the password
    if check_password(passw):
        print("It is a valid password")
        # Breaking the while loop if it is a valid password
        break
    else:
        print("Entered password does not meet the requirements, Try Again")
