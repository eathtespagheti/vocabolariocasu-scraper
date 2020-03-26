from getRequests import *
from printingFunctions import *
from fileIO import *
import gc

# Website base URL
WEBPAGE_BASE = "http://vocabolariocasu.isresardegna.it"
OUT_FOLDER = "output"

jsonWordsReference = []
numberOfDefinitions = 0
processedDefinitions = 0

# Get all the links and words
print("Downloading all the words' definitions' links")
lettersLinks = getLettersLinks(WEBPAGE_BASE)
numberOfLetters = len(lettersLinks)
for i, letter in enumerate(lettersLinks, start=1):
    printProgress(i, numberOfLetters)
    print("Downloading links for letter " + letter, end=' ')
    # Parse all the words from page
    words = getWords(WEBPAGE_BASE, lettersLinks[letter])
    # Save words to a json file
    jsonpath = saveDictToJSON(words, "__words", path.join(OUT_FOLDER, letter))
    # Add jsonpath to list
    jsonWordsReference.append(jsonpath)
    # Update number of definitions
    wordsNumber = len(words)
    numberOfDefinitions += wordsNumber
    print(str(wordsNumber) + " links found, for a total of " +
          str(numberOfDefinitions))
    # Free memory
    del words
    gc.collect()
# Free memory again
del lettersLinks
gc.collect()


# # For every letter
# numberOfLetters = len(lettersLinks)
# for i, letter in enumerate(lettersLinks, start=1):
#     # Verbose
#     printProgress(i, numberOfLetters)
#     print("Working on letter " + letter)
#     # Parse all the words from page
#     words = getWords(WEBPAGE_BASE, lettersLinks[letter])
#     # Array of definitions
#     definitions = []
#     # Dict with the definitions associated to the letter
#     wordsDict = {str(letter): definitions}
#     dictionary.append(definitions)
#     # Number of words
#     numberOfWords = len(words)
#     for j, word in enumerate(words, start=1):
#         # Verbose
#         printTab(1)
#         printProgress(j, numberOfWords)
#         print("Working on word " + word)
#         # Get definition
#         definition = getDefinition(WEBPAGE_BASE, words[word])
#         definitions.append(definition)
#         definition.print()
