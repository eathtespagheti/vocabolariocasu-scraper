from ProgressStatus import ProgressStatus
from getRequests import *
from printingFunctions import *
from fileIO import *
from shutil import rmtree
from time import sleep
import gc
import itertools


def get_download_links(webpage_base: str, out_folder: str, status: ProgressStatus):
    """
    Get definition link for every word and save all the data on json files
    """
    print("Downloading all the words' definitions' links")
    letters_links = get_letters_links(webpage_base)
    number_of_letters = len(letters_links)
    for i, letter in enumerate(letters_links, start=1):
        print_progress(i, number_of_letters)
        print("Downloading links for letter " + letter)
        # Parse all the words from page
        words = get_words(webpage_base, letters_links[letter])
        # Save words to a json file
        jsonpath = save_dict_to_json(words, "__words.json",
                                     path.join(out_folder, letter))
        # Add jsonpath to list
        status.json_words_reference.append(jsonpath)
        # Update number of definitions
        words_number = len(words)
        status.number_of_definitions += words_number
        # Time verbose
        status.time.update_and_print()
        status.time.print_remaining_time(number_of_letters - i)
        del words
        gc.collect()
    # Free memory again
    del letters_links
    status.save_links()
    gc.collect()


def download_definitions(webpage_base: str, status: ProgressStatus, start_from_last_index: bool = False):
    """
    Download and save all the words definitions
    """
    print("Downloading definitions")

    # Adjust start set
    sliced_letters = 0
    if start_from_last_index:
        letters_dataset = itertools.islice(
            status.json_words_reference, status.last_word_source_index, None)
        sliced_letters = status.last_word_source_index
    else:
        letters_dataset = status.json_words_reference

    # For every letter
    for i, letter in enumerate(letters_dataset):
        # Parse all the words from json
        words = get_item_from_json(letter)
        # Update status variable
        status.last_word_source_index = i + sliced_letters
        # Adjust start set
        sliced_items = 0
        if start_from_last_index:
            words_dataset = itertools.islice(
                words, status.last_word_processed_index + 1, None)
            start_from_last_index = False
            sliced_items = status.last_word_processed_index + 1
        else:
            words_dataset = words
        for j, word in enumerate(words_dataset):
            # Verbose
            processed_items = status.processed_definitions + 1
            print_progress(processed_items, status.number_of_definitions, True)
            print("Working on word " + word)
            # Get definition
            try:
                definition = get_definition(webpage_base, words[word])
                # Save definition
                directory = get_directory_path(letter)
                save_dict_to_json(definition.to_dict(),
                                  word + ".json", directory)
                del definition
            except:
                print("Error downloading definition for: " +
                      word + ", skipping...")
                # Add to skipped words
                status.skip(word)
                print("Waiting " + str(WAIT_TIME) + " seconds...")
                sleep(WAIT_TIME)
            # Update status variable
            status.last_word_processed_index = j + sliced_items
            status.processed_definitions = processed_items
            status.save_progress()
            # Time remaining
            status.time.update_and_print()
            status.time.print_remaining_time(status.remaining_items())
            # Garbage collector
            gc.collect()


# VARIABLES
webpage_base = "http://vocabolariocasu.isresardegna.it"
OUT_FOLDER = "output"
WAIT_TIME = 10

status = ProgressStatus(OUT_FOLDER)  # Progress variables
load = False
if status.check_saved():
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
    get_download_links(webpage_base, OUT_FOLDER, status)

print("")
download_definitions(webpage_base, status, load)

print("Downloading complete, skipped words are:")
for word in status.skipped_words:
    print(word)
