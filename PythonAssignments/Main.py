# importing randstr module
from randStr import randWord, strMixer, randIntForWord

# Calling functions

print(randWord("hello there this is Karthik"))
print(randWord("hello there this is Kathik"))
print(randWord("hello there this is Karthik", 1))
print(randWord("hello there this is vamshi", 2))
print(randWord("hello there this is Karhtik", 3))

print()

print(strMixer("Karhik"))
print(strMixer("hello Karthik this is python"))
print(strMixer("hello Karthik this is python", 2))
print(strMixer("vamshi", 1))
print(strMixer("Karthik", 3))

print()

print(randIntForWord("Karthik"))
print(randIntForWord("vamshi"))
print(randIntForWord("Karthik", 2))
print(randIntForWord("vamshi", 2))
print(randIntForWord("Karthik", 3))
