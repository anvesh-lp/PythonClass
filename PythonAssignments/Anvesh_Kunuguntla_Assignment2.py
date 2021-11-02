
# Function to generate the hex code with base 16
def number_converter_16(numbers):
    # Intializing list of hex
    hexa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
    l = []
    base = numbers[0]
    # Looping through each number in the list
    for i in range(1, len(numbers)):
        bite = ""
        tempNum = numbers[i]
        # Checking if the number is decimal or not
        if len(str(tempNum).split(".")) != 1:
            bite = "NA"
            l.append(bite)
            continue
            #  Looping through the number to generate the bite
        while tempNum > 0:
            # print(tempNum % base)
            extractedBite = hexa[tempNum % base]
            tempNum = tempNum // base
            bite = str(extractedBite) + bite
        # adding the generated hex code to the list
        l.append(bite)
    l.insert(0, "base=" + str(base))
    return l


# Function to generate the hex code with base 16

'''

 This function iterates over the each element in the list 
 For each element, it extracts the bite and add the final binary code to the list
 process is repeated for all the elements

'''


# Function to generate the binary code with base 1-15

def number_converter(*numbers):
    base = numbers[0]
    l = []
    # Checking if it is a valid base or not
    if base > 16 or base <= 1:
        return ['Wrong base']
    if base >= 10:
        return number_converter_16(numbers)
    for i in range(1, len(numbers)):
        bite = ""
        tempNum = numbers[i]
        # Checking if the number is decimal or not
        if len(str(tempNum).split(".")) != 1:
            bite = "NA"
            l.append(bite)
            continue
        #     Looping through the number to generate the bite
        while tempNum > 0:
            extractedBite = tempNum % base
            # print(extractedBite)
            tempNum = tempNum // base
            # Appending to the previous bite generated
            bite = str(extractedBite) + bite
        #     Appending the bite to list
        l.append(bite)
    l.insert(0, "base=" + str(base))
    return l


print(number_converter(14, 44, 12))


