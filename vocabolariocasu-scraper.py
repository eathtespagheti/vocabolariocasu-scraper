from ProgressStatus import ProgressStatus
from getRequests import *
from printingFunctions import *
from fileIO import *
import gc


TIME_VALUES_FOR_CHECK = 50
# Website base URL
WEBPAGE_BASE = "http://vocabolariocasu.isresardegna.it"
OUT_FOLDER = "output"

status = ProgressStatus()  # Progress variables

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
    status.jsonWordsReference.append(jsonpath)
    # Update number of definitions
    wordsNumber = len(words)
    status.numberOfDefinitions += wordsNumber
    # Time verbose
    printTab(1)
    print('   ', end='')  # Just because OCD
    status.time.updateAndPrint()
    printTab(1)
    print('   ', end='')  # Just because OCD
    status.time.printRemainingTime(numberOfLetters - i)
    del words
    gc.collect()
# Free memory again
del lettersLinks
gc.collect()

print("\nDownloading definitions")
# For every letter
for i, letter in enumerate(status.jsonWordsReference, start=1):
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
        printProgress(i + j, status.numberOfDefinitions, True)
        print("Working on word " + word)
        # Get definition
        definition = getDefinition(WEBPAGE_BASE, words[word])
        definitions.append(definition)
        # Time remaining
        printTab(1)
        status.time.updateAndPrint()
        printTab(1)
        status.time.printRemainingTime(status.numberOfDefinitions - (i + j))
