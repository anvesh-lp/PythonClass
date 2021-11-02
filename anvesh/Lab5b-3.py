# Defining the function
def falling_distance(time):
    # Calculating the distance using the formula
    return (9.8 * time * time) / 2


# passing the values to the function using a for loop
for i in range(1, 11):
    print("The falling distance at the time interval of  " + str(i) + " is " + str(falling_distance(i)) + " meters")
