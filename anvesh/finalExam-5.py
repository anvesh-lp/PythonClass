# Defining the fucntion
def counterReturningList(mixeString):
    nonDigits = 0
    digits = 0
    d = []
    s = ""
    # iterating through the sting
    for i in mixeString:
        # Checking if it is a digit or not
        if i.isdigit():
            digits += 1
            # appending to the list
            d.append(i)
        else:
            nonDigits += 1
            s += i
    #         Converting the string to the tuple
    s = tuple(s)
    # Returning the list and tuple in a strig
    return [d, s]


def counterReturingCount(mixeString):
    nonDigits = 0
    digits = 0
    # Iterating through the list
    for i in mixeString:
        # Checking if it is a digit
        if i.isdigit():
            # incrementing the count of the digits
            digits += 1
        else:
            nonDigits += 1
    #  Returning the count of digits and non_digits
    return [nonDigits, digits]

# Printing the results


st=input("Enter a string to to count digits and non-Digits\n")
c = counterReturningList(st)
print("List of digits in the string", c[0])
print("tuple of non-Digits in the string", c[1])
print("Count of non-Digits and digits it the string ", counterReturingCount(st))

# print()
# c = counterReturningList("Rake67&*($%)sh123")
# print("List of digits in the string", c[0])
# print("tuple of non-Digits in the string", c[1])
# print("Count of non-Digits and digits it the string ", counterReturingCount("Rake67&*($%)sh123"))
