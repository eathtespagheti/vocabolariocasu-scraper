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
    outputPath = path.join(Directory, Filename)
    createDirectory(Directory)
    with open(outputPath, "w") as out:
        json.dump(Dict, out, indent=4)
    return outputPath


def getDictFromJSON(Filename: str, Directory: str = ""):
    """
    Parse a Dict from a JSON
    """
    if Directory == "":
        FilePath = Filename
    else:
        FilePath = path.join(Directory, Filename)

    with open(FilePath, "r") as input:
        return json.load(input)


def checkIfPathExist(Filename: str, Directory: str = ""):
    """
    Check if a file or a directory exist
    """
    if Directory == "":
        FilePath = Filename
    else:
        FilePath = path.join(Directory, Filename)
    return path.exists(FilePath)


def getDirectoryPath(filepath: str):
    """
    Get the directory path from a file path
    """
    return path.dirname(filepath)
