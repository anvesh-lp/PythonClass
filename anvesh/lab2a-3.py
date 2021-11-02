# initializing the list
lis = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
# taking input form the user
num = int(input("Enter the number in a range of 1 to 10\n"))
if num < 1 or num > 10:
    print("invalid number!!!")
else:
    print(lis[num - 1])