from pathlib import Path
import json
from os import path


def create_directory(dir: str):
    """
    Safely create a directory
    """
    Path(dir).mkdir(parents=True, exist_ok=True)


def save_dict_to_json(dict: dict, filename: str, directory: str):
    """
    Save a dictionary to a JSON file
    """
    output_path = path.join(directory, filename)
    create_directory(directory)
    with open(output_path, "w") as out:
        json.dump(dict, out, indent=4)
    return output_path


def save_list_to_json(list: list, filename: str, directory: str):
    """
    Save a list to a JSON file
    """
    output_path = path.join(directory, filename)
    create_directory(directory)
    with open(output_path, "w") as out:
        json.dump(list, out, indent=4)
    return output_path


def get_item_from_json(filename: str, directory: str = ""):
    """
    Parse a Dict from a JSON
    """
    if directory == "":
        filepath = filename
    else:
        filepath = path.join(directory, filename)

    with open(filepath, "r") as input:
        return json.load(input)


def check_if_path_exist(filename: str, directory: str = ""):
    """
    Check if a file or a directory exist
    """
    if directory == "":
        filepath = filename
    else:
        filepath = path.join(directory, filename)
    return path.exists(filepath)


def get_directory_path(filepath: str):
    """
    Get the directory path from a file path
    """
    return path.dirname(filepath)
