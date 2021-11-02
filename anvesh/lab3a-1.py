while True:
    # Taking nput from the user
    num = int(input("Enter a number in range 0-100\n"))
    # Checking the condition
    if 0 <= num <= 100:
        print("Number is a valid number")
        # Breaking the loop if the condition is met
    elif num == 666:
        break
    else:
        print("Number is not in range..Try again")
