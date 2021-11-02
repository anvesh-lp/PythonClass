# Reading a file
numfile = open("nums.txt")
# initializing a list
li = []
# Operating through the contents of the file
for i in numfile.readlines():
    i = int(i)
    li.append(i)
#     Finding max, min, sum, average of the numbers in the file
mi = min(li)
ma = max(li)
s = sum(li)
av = s / len(li)
print("minimum number in the file : ", mi)
print("maximum number in the file : ", ma)
print("total of the numbers in the file : ", s)
print("average of the numers in the file : ", av)
