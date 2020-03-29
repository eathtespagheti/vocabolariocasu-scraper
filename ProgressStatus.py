from TimeManagment import TimeManager
from fileIO import saveDictToJSON, getDictFromJSON, checkIfPathExist


class ProgressStatus:
    """
    Class containing all the status variables for the script execution
    """
    # Time
    time: TimeManager
    # Links
    jsonWordsReference: list
    numberOfDefinitions: int
    # Progress
    processedDefinitions: int
    lastWordSourceIndex: str
    lastWordProcessedIndex: str
    # Save location informations
    filename: str
    saveFolder: str
    __linksSubname__: str
    __progressSubname__: str

    def __init__(self, saveFolder: str = "", filename: str = "status"):
        self.time = TimeManager()
        self.jsonWordsReference = []
        self.numberOfDefinitions = 0
        self.processedDefinitions = 0
        self.saveFolder = saveFolder
        self.filename = filename
        self.lastWordSourceIndex = 0
        self.lastWordProcessedIndex = -1
        self.__linksSubname__ = "links"
        self.__progressSubname__ = "progress"

    def __getFilename__(self, dataType: str):
        """
        Return the composed filename for saving
        """
        return self.filename + "_" + dataType + ".json"

    def __toDictLink__(self):
        """
        Store and return the links class data to a dict
        """
        data = {
            "jsonWordsReference": self.jsonWordsReference,
            "numberOfDefinitions": self.numberOfDefinitions
        }
        return data

    def __toDictProgress__(self):
        """
        Store and return the progress class data to a dict
        """
        data = {
            "processedDefinitions": self.processedDefinitions,
            "lastWordSourceIndex": self.lastWordSourceIndex,
            "lastWordProcessedIndex": self.lastWordProcessedIndex
        }
        return data

    def saveLinks(self):
        """
        Save the links to the json file
        """
        saveDictToJSON(self.__toDictLink__(),
                       self.__getFilename__(self.__linksSubname__), self.saveFolder)

    def saveProgress(self):
        """
        Save the links to the json file
        """
        saveDictToJSON(self.__toDictProgress__(),
                       self.__getFilename__(self.__progressSubname__), self.saveFolder)

    def save(self):
        """
        Save all the reusable data to json
        """
        self.saveLinks()
        self.saveProgress()

    def loadLinks(self):
        """
        Load the links data from the json file
        """
        data = getDictFromJSON(self.__getFilename__(
            self.__linksSubname__), self.saveFolder)
        self.jsonWordsReference = data.get("jsonWordsReference")
        self.numberOfDefinitions = data.get("numberOfDefinitions")

    def loadProgress(self):
        """
        Load the progress data from the json file
        """
        data = getDictFromJSON(self.__getFilename__(
            self.__progressSubname__), self.saveFolder)
        self.processedDefinitions = data.get("processedDefinitions")
        self.lastWordSourceIndex = data.get("lastWordSourceIndex")
        self.lastWordProcessedIndex = data.get("lastWordProcessedIndex")

    def load(self):
        """
        Load all the data from the json files
        """
        if checkIfPathExist(self.__getFilename__(self.__linksSubname__), self.saveFolder):
            self.loadLinks()
        if checkIfPathExist(self.__getFilename__(self.__progressSubname__), self.saveFolder):
            self.loadProgress()

    def checkSaved(self):
        """
        Check if there's a saved istance of ProgressStatus
        """
        return checkIfPathExist(self.__getFilename__(self.__linksSubname__), self.saveFolder)

    def remainingItems(self):
        """
        Return the number of remaining items
        """
        return self.numberOfDefinitions - self.processedDefinitions
