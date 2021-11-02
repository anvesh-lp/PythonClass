# Taking input from user
string = input("Enter the string")
# Printing the lenth of the string
print(len(string))
modifiedString = ""
for i in string:
    # Checking if it is lower
    if i.lower() in ["a", "e", "i", "o", "u"]:
        modifiedString += i.upper()
    else:
        modifiedString += i
print(modifiedString)
# Converting it into list
listString = list(string)
print(listString)
print(len(listString))
