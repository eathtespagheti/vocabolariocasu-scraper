from ProgressStatus import ProgressStatus
from getRequests import *
from printingFunctions import *
from fileIO import *
from shutil import rmtree
import gc
import itertools


def getDownloadLinks(WEBPAGE_BASE: str, OUT_FOLDER: str, status: ProgressStatus):
    """
    Get definition link for every word and save all the data on json files
    """
    print("Downloading all the words' definitions' links")
    lettersLinks = getLettersLinks(WEBPAGE_BASE)
    numberOfLetters = len(lettersLinks)
    for i, letter in enumerate(lettersLinks, start=1):
        printProgress(i, numberOfLetters)
        print("Downloading links for letter " + letter)
        # Parse all the words from page
        words = getWords(WEBPAGE_BASE, lettersLinks[letter])
        # Save words to a json file
        jsonpath = saveDictToJSON(words, "__words.json",
                                  path.join(OUT_FOLDER, letter))
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
    status.save()
    gc.collect()


def downloadDefinitions(WEBPAGE_BASE: str, status: ProgressStatus):
    """
    Download and save all the words definitions
    """
    print("Downloading definitions")
    # For every letter
    for i, letter in enumerate(status.jsonWordsReference):
        # Parse all the words from json
        words = getDictFromJSON(letter)
        # Array of definitions
        definitions = []
        # Dict with the definitions associated to the letter
        wordsDict = {str(letter): definitions}
        # Number of words
        numberOfWords = len(words)
        # Update status variable
        status.lastWordSource = str(letter)
        for j, word in enumerate(words, start=1):
            # Verbose
            processedItems = i + j
            printProgress(processedItems, status.numberOfDefinitions, True)
            print("Working on word " + word)
            # Get definition
            definition = getDefinition(WEBPAGE_BASE, words[word])
            definitions.append(definition)
            # Update status variable
            status.lastWordProcessed = word
            status.processedDefinitions = processedItems
            status.save()
            # Time remaining
            printTab(1)
            status.time.updateAndPrint()
            printTab(1)
            status.time.printRemainingTime(status.remainingItems())


# VARIABLES
WEBPAGE_BASE = "http://vocabolariocasu.isresardegna.it"
OUT_FOLDER = "output"

status = ProgressStatus(OUT_FOLDER)  # Progress variables
load = False
if status.checkSaved():
    answer = None
    while answer not in ("Y", "y", "", "no"):
        answer = input(
            "A previous run data has been found, do you want to load it? [Y/n]: ")
        if answer == "Y" or answer == "y" or answer == "":
            load = True
        elif answer == "n":
            load = False
            rmtree(OUT_FOLDER)
            break
        else:
            print("Please enter y or n.")
            answer = None
if load:
    status.load()
else:
    print("")
    getDownloadLinks(WEBPAGE_BASE, OUT_FOLDER, status)

print("")
downloadDefinitions(WEBPAGE_BASE, status)
