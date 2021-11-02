import re

# Defining  global dictionaries
wordsDict = {}
lettersDict = {}


def cleanupLine(line):
    """this function will remove characters that are not needed from the line-string. Unwanted characters are all characters except a-z, A-Z, 0-9 and ' and should be replaced with a space
        long-term -> long term
        It's amazing, isn't it? -> Is's amazaing  isn't it
        Note, if you are familiar with regex, you can use that, otherwise a loop is fine"""

    # Stripping unwanted characters using regex
    stripped_line = re.sub("[^A-Za-z0-9\']", " ", line)
    return stripped_line


def countWords(line):
    """For a stripped line, this function counts the words and updates
        the globla variable wordsDict{}.
        Note, we convert upper case words to lower case words"""
    global wordsDict
    w = line.lower().split(" ")
    for word in w:
        if len(word) != 0:
            # Checking if the word is in dictionary
            if word in wordsDict:
                wordsDict[word] += 1
            else:
                wordsDict[word] = 1
    return wordsDict


def countLetters(line):
    """For a stripped line, this function counts the letters and updates
        the globla variable lettersDict{}.
        Note, we convert upper case letters to lower case
        Note2, numbers and ' should be ignored"""
    global lettersDict
    words = line.lower()
    # Removing unwanted characters
    let = re.sub("[0-9\']", "", words)
    for word in let:
        for letter in word:
            if len(word) != 0:
                # Counting each letter and updating the dict
                if letter in lettersDict:
                    lettersDict[letter] = lettersDict[letter] + 1
                else:
                    lettersDict[letter] = 1
    return lettersDict


def readFiles(filename):
    handle = open(filename, 'r')
    for line in handle:
        # calling functions to do operations
        stripped_line = cleanupLine(line)
        countWords(stripped_line)
        countLetters(stripped_line)


def results():
    # Declaring the text files in the tuple
    files = ("text1.txt", "text2.txt", "text3.txt")
    aplha = ('e', "t", "w")
    str = ("to", "the", "computer")
    let = []
    wor = []
    inde = 0
    for i in files:
        # Calling readFiles function to read files
        readFiles(i)
        # Adding the results to the list
        let.append(lettersDict.get(aplha[inde]))
        wor.append(wordsDict.get(str[inde]))
        inde += 1
        # clearing the dictionary after each iteration
        wordsDict.clear()
        lettersDict.clear()
    return [let, wor]


print()
print("The total frequencies   ", results())
