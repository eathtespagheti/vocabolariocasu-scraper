from pathlib import Path
import json
from os import path


def createDirectory(DIR: str):
    """
    Safely create a directory
    """
    Path(DIR).mkdir(parents=True, exist_ok=True)


def saveDictToJSON(Dict: dict, Filename: str, Directory: str):
    """
    Save a dictionary to a JSON file
    """
    Filename += ".json"
    outputPath = path.join(Directory, Filename)
    createDirectory(Directory)
    with open(outputPath, "w") as out:
        json.dump(Dict, out, indent=4)
    return outputPath


def getDictFromJSON(FilePath: str):
    """
    Parse a Dict from a JSON
    """
    with open(FilePath, "r") as input:
        return json.load(input)
