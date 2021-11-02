# Initializing a list
li = []
# Iterating throught he range
for i in range(424, 1074):
    # Validating the condition
    if i % 6 == 0 and i % 11 == 0:
        # Adding to the list
        li.append(i)

# Printing the list
print("Number divisible by 6 and 11 in range 424-1073(inclusive) are")
print(li)
