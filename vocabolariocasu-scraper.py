from getRequests import *
from printingFunctions import *
from fileIO import *
from timeManagment import *
import gc


TIME_VALUES_FOR_CHECK = 50
# Website base URL
WEBPAGE_BASE = "http://vocabolariocasu.isresardegna.it"
OUT_FOLDER = "output"

time = timeManager()

jsonWordsReference = []
numberOfDefinitions = 0
processedDefinitions = 0

# Get all the links and words
print("Downloading all the words' definitions' links")
lettersLinks = getLettersLinks(WEBPAGE_BASE)
numberOfLetters = len(lettersLinks)
for i, letter in enumerate(lettersLinks, start=1):
    printProgress(i, numberOfLetters)
    print("Downloading links for letter " + letter)
    # Parse all the words from page
    words = getWords(WEBPAGE_BASE, lettersLinks[letter])
    # Save words to a json file
    jsonpath = saveDictToJSON(words, "__words", path.join(OUT_FOLDER, letter))
    # Add jsonpath to list
    jsonWordsReference.append(jsonpath)
    # Update number of definitions
    wordsNumber = len(words)
    numberOfDefinitions += wordsNumber
    # Time verbose
    printTab(1)
    print('   ', end='')  # Just because OCD
    time.updateAndPrint()
    printTab(1)
    print('   ', end='')  # Just because OCD
    time.printRemainingTime(numberOfLetters - i)
    del words
    gc.collect()
# Free memory again
del lettersLinks
gc.collect()

print("\nDownloading definitions")
# For every letter
for i, letter in enumerate(jsonWordsReference, start=1):
    # Parse all the words from json
    words = getDictFromJSON(letter)
    # Array of definitions
    definitions = []
    # Dict with the definitions associated to the letter
    wordsDict = {str(letter): definitions}
    # Number of words
    numberOfWords = len(words)
    for j, word in enumerate(words, start=1):
        # Verbose
        printProgress(i + j, numberOfDefinitions, True)
        print("Working on word " + word)
        # Get definition
        definition = getDefinition(WEBPAGE_BASE, words[word])
        definitions.append(definition)
        # Time remaining
        printTab(1)
        time.updateAndPrint()
        printTab(1)
        time.printRemainingTime(numberOfDefinitions - (i + j))
