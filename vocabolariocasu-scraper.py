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
    status.saveLinks()
    gc.collect()


def downloadDefinitions(WEBPAGE_BASE: str, status: ProgressStatus, startFromLastIndex: bool = False):
    """
    Download and save all the words definitions
    """
    print("Downloading definitions")

    # Adjust start set
    if startFromLastIndex:
        lettersDataset = itertools.islice(
            status.jsonWordsReference, status.lastWordSourceIndex, None)
    else:
        lettersDataset = status.jsonWordsReference

    # For every letter
    for i, letter in enumerate(lettersDataset):
        # Parse all the words from json
        words = getDictFromJSON(letter)
        # Number of words
        numberOfWords = len(words)
        # Update status variable
        status.lastWordSourceIndex = i
        # Adjust start set
        slicedItems = 0
        if startFromLastIndex:
            wordsDataset = itertools.islice(
                words, status.lastWordProcessedIndex + 1, None)
            startFromLastIndex = False
            slicedItems = status.lastWordProcessedIndex + 1
        else:
            wordsDataset = words
        for j, word in enumerate(wordsDataset):
            # Verbose
            processedItems = status.processedDefinitions + 1
            printProgress(processedItems, status.numberOfDefinitions, True)
            print("Working on word " + word)
            # Get definition
            definition = getDefinition(WEBPAGE_BASE, words[word])
            # Save definition
            directory = getDirectoryPath(letter)
            saveDictToJSON(definition.toDict(), word + ".json", directory)
            del definition
            # Update status variable
            status.lastWordProcessedIndex = j + slicedItems
            status.processedDefinitions = processedItems
            status.saveProgress()
            # Time remaining
            printTab(1)
            status.time.updateAndPrint()
            printTab(1)
            status.time.printRemainingTime(status.remainingItems())
            # Garbage collector
            gc.collect()


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
downloadDefinitions(WEBPAGE_BASE, status, load)
