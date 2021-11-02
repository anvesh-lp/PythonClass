# Defining the hamming distance function
def hammingDistance(string1, string2):
    count = 0
    # using a for loop to iterate over the characters of the two strings
    for i in range(len(string1)):
        # Checking if the characters at two strings is equal
        if string2[i] != string1[i]:
            count += 1
    return count


# Taking inputs from the user
str1 = input("Enter the string one")
str2 = input("enter the string two")
# Checking the length of the strings entered by the user
if len(str2) != len(str1):
    print("len of the strings is not equal")
else:
    print("The hamming distance between the two string is :", hammingDistance(str1, str2))
