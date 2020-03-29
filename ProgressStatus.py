from TimeManagment import TimeManager
from fileIO import saveDictToJSON, getDictFromJSON, checkIfPathExist


class ProgressStatus:
    """
    Class containing all the status variables for the script execution
    """
    time: TimeManager
    jsonWordsReference: list
    numberOfDefinitions: int
    processedDefinitions: int
    saveFolder: str
    filename: str
    lastWordSource: str
    lastWordProcessed: str

    def __init__(self, saveFolder: str = "", filename: str = "status.json"):
        self.time = TimeManager()
        self.jsonWordsReference = []
        self.numberOfDefinitions = 0
        self.processedDefinitions = 0
        self.saveFolder = saveFolder
        self.filename = filename
        self.lastWordSource = ""
        self.lastWordProcessed = ""

    def __toDict__(self):
        """
        Store and return the important class data to a dict
        """
        data = {
            "jsonWordsReference": self.jsonWordsReference,
            "numberOfDefinitions": self.numberOfDefinitions,
            "processedDefinitions": self.processedDefinitions,
            "lastWordSource": self.lastWordSource,
            "lastWordProcessed": self.lastWordProcessed
        }
        return data

    def save(self):
        """
        Save the class to a json file
        """
        saveDictToJSON(self.__toDict__(), self.filename, self.saveFolder)

    def load(self):
        """
        Load the status istance from a json file
        """
        data = getDictFromJSON(self.filename, self.saveFolder)
        self.jsonWordsReference = data.get("jsonWordsReference")
        self.numberOfDefinitions = data.get("numberOfDefinitions")
        self.processedDefinitions = data.get("processedDefinitions")
        self.lastWordSource = data.get("lastWordSource")
        self.lastWordProcessed = data.get("lastWordProcessed")

    def checkSaved(self):
        """
        Check if there's a saved istance of ProgressStatus
        """
        return checkIfPathExist(self.filename, self.saveFolder)

    def remainingItems(self):
        return self.numberOfDefinitions - self.processedDefinitions
