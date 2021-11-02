# Defining a count vowel function
def count_vowels(strin):
    count = 0
    for i in strin:
        k = i.lower()
        if k in ["a", "e", "i", "o", "u"]:
            count += 1
    return count


# Taking inputs from the user
string = input("Enter the string to count vowels\n")
# Calling the fcunction and printing the result
print("No of vowels in the given string are ", count_vowels(string))
