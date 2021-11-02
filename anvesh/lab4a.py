# Taking input from the user
string = input("Enter a String\n")
# initializing the dictionary
count = {}
times = 0
# using a for loop to iterate over the string
for i in string:
    # converting it to lower
    k = i.lower()
    if k in ["a", "e", "i", "o", "u"]:
        # Checking if it is already in dictionary
        if count.get(k) is None:
            count[k] = 1
        else:
            count[k] = count.get(k) + 1
        #     incrementing the count of the vowels
        times += 1
#         Printing the results
print(count)
print("total count of vowels : ", times)
