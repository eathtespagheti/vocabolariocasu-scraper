from TimeManagment import TimeManager
from fileIO import saveDictToJSON, getDictFromJSON


class ProgressStatus:
    """
    Class containing all the status variables for the script execution
    """
    time: TimeManager
    jsonWordsReference: list
    numberOfDefinitions: int
    processedDefinitions: int
    saveFolder: str

    def __init__(self, saveFolder: str = ""):
        self.time = TimeManager()
        self.jsonWordsReference = []
        self.numberOfDefinitions = 0
        self.processedDefinitions = 0
        self.saveFolder = saveFolder

    def __toDict__(self):
        """
        Store and return the important class data to a dict
        """
        data = {
            "jsonWordsReference": self.jsonWordsReference,
            "numberOfDefinitions": self.numberOfDefinitions,
            "processedDefinitions": self.processedDefinitions
        }
        return data

    def save(self, filename: str = "status.json"):
        """
        Save the class to a json file
        """
        saveDictToJSON(self.__toDict__(), filename, self.saveFolder)

    def load(self, filename: str = "status.json"):
        """
        Load the status istance from a json file
        """
        data = getDictFromJSON(filename, self.saveFolder)
        self.jsonWordsReference = data.get("jsonWordsReference")
        self.numberOfDefinitions = data.get("numberOfDefinitions")
        self.processedDefinitions = data.get("processedDefinitions")
