# importing randstr module
from randStr import randWord, strMixer, randIntForWord

# Calling functions

print(randWord("hello there this is anvesh"))
print(randWord("hello there this is vamshi"))
print(randWord("hello there this is anvesh", 1))
print(randWord("hello there this is vamshi", 2))
print(randWord("hello there this is anvesh", 3))

print()

print(strMixer("anvesh"))
print(strMixer("hello anvesh this is python"))
print(strMixer("hello anvesh this is python", 2))
print(strMixer("vamshi", 1))
print(strMixer("anvesh", 3))

print()

print(randIntForWord("anvesh"))
print(randIntForWord("vamshi"))
print(randIntForWord("anvesh", 2))
print(randIntForWord("vamshi", 2))
print(randIntForWord("anvesh", 3))
