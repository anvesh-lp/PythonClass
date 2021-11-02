def getSubstringsInList(iterable):
    # initializing an Array
    listOfSubStrings = []
    for times in range(1, len(iterable) + 1):
        for k in range(0, len(iterable) - times + 1):
            # Getting the substring using slicing
            subString = iterable[k:k + times]
            # Adding the substring to the list
            listOfSubStrings.append(subString)
    # Returning the list
    return listOfSubStrings


def getSubstringsWithNoDubs(iterable):
    # initializing an Array
    listOfSubStrings = []
    for times in range(1, len(iterable) + 1):
        for k in range(0, len(iterable) - times + 1):
            # Getting the substring using slicing
            subString = iterable[k:k + times]
            # Adding the substring to the list after checking if its not already in the list
            if subString not in listOfSubStrings:
                listOfSubStrings.append(subString)
    # Returning the final list

    return listOfSubStrings


s = "abac"
print(getSubstringsInList(s))
print(getSubstringsWithNoDubs(s))
