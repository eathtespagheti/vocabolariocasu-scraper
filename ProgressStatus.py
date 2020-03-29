from TimeManagment import TimeManager


class ProgressStatus:
    time: TimeManager
    jsonWordsReference: list
    numberOfDefinitions: int
    processedDefinitions: int

    def __init__(self):
        self.time = TimeManager()
        self.jsonWordsReference = []
        self.numberOfDefinitions = 0
        self.processedDefinitions = 0
