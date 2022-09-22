string = "cababd"

while True:
    l = len(string)
    string = string.replace("ba", "")
    string = string.replace("ab", "")
    string = string.replace("cd", "")
    string = string.replace("dc", "")
    if l == (len(string)):
        break
print(string)
