import Definition
from getRequests import *

# Website base URL
WEBPAGE_BASE = "http://vocabolariocasu.isresardegna.it"

lettersLinks = getLettersLinks(WEBPAGE_BASE)

# For every letter
numberOfLetters = len(lettersLinks)
lettersIndex = 1
for letter in lettersLinks:
    print("[" + str(lettersIndex) + "/" + str(numberOfLetters) +
          "] Working on letter " + letter)
    lettersIndex += 1
    words = getWords(WEBPAGE_BASE, lettersLinks[letter])
    numberOfWords = len(words)
    wordsIndex = 0
    for word in words:
        print()
        # definition = getDefinition(WEBPAGE_BASE, words[word])
        # print(definition.word)
