# Importing the modules
import random
import sys

# Capturing teh initial state of the random generator
state = random.getstate()
# Checking if the module being used is imported or run as file
if __name__ == "__main__":
    print("Sorry, but this module can only be imported!")
    sys.exit()


def randWord(string, setSeed=None):
    if setSeed is not None:
        # Setting the seed for the random generator
        random.seed(setSeed)
    #     Splitting the string into words
    string = string.split(" ")
    # Returning a random word from the string
    return random.choice(string)


def strMixer(string, setSeed=None):
    # Resetting the seed to its initial state before setting the seed
    random.setstate(state)
    wordArray = string.split(" ")
    if setSeed is not None:
        # Setting the seed for the random generator
        random.seed(setSeed)
    #     Checking if the given string has multiple words in it
    if len(wordArray) == 1:
        l = list(string)
        # Shuffling the list using shuffle method
        random.shuffle(l)
        # Returning the word after concatenating all the letters in the string
        return "".join(l)
    random.shuffle(wordArray)
    # Resetting the seed to its initial state before setting the seed
    return " ".join(wordArray)


def randIntForWord(string, setSeed=None):
    # Checking if the seed is none.
    if setSeed is not None:
        # setting the seed
        random.seed(setSeed)
        # returning the random int
        return random.randint(0, 100000)
    # Setting the seed as string
    random.seed(string)
    return random.randint(0, 100000)
