import Definition
from getRequests import *
from printingFunctions import *

# Website base URL
WEBPAGE_BASE = "http://vocabolariocasu.isresardegna.it"

lettersLinks = getLettersLinks(WEBPAGE_BASE)

# For every letter
numberOfLetters = len(lettersLinks)
for i, letter in enumerate(lettersLinks, start=1):
    printPercentage(i, numberOfLetters)
    print("Working on letter " + letter)
    words = getWords(WEBPAGE_BASE, lettersLinks[letter])
    numberOfWords = len(words)
    for j, word in enumerate(words, start=1):
        printTab(1)
        printPercentage(j, numberOfWords)
        print("Working on word " + word)
    # definition = getDefinition(WEBPAGE_BASE, words[word])
    # print(definition.word)
