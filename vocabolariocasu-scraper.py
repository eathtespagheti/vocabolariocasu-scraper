from getRequests import *
from printingFunctions import *

# Website base URL
WEBPAGE_BASE = "http://vocabolariocasu.isresardegna.it"

lettersLinks = getLettersLinks(WEBPAGE_BASE)
dictionary = []

# For every letter
numberOfLetters = len(lettersLinks)
for i, letter in enumerate(lettersLinks, start=1):
    # Verbose
    printPercentage(i, numberOfLetters)
    print("Working on letter " + letter)
    # Parse all the words from page
    words = getWords(WEBPAGE_BASE, lettersLinks[letter])
    # Array of definitions
    definitions = []
    # Dict with the definitions associated to the letter
    wordsDict = {str(letter): definitions}
    dictionary.append(definitions)
    # Number of words
    numberOfWords = len(words)
    for j, word in enumerate(words, start=1):
        # Verbose
        printTab(1)
        printPercentage(j, numberOfWords)
        print("Working on word " + word)
        # Get definition
        definition = getDefinition(WEBPAGE_BASE, words[word])
        definitions.append(definition)
        definition.print()
