import datetime as dt


class TimeManager:
    """
    Manage time in the script
    """
    start: dt.datetime
    last: dt.datetime
    elapsed: dt.timedelta
    records: list
    maxRecords: int
    __totalRecords__: dt.timedelta

    def __init__(self, maxRecords: int = 500):
        """
        Set the starting time for the timeManager
        """
        self.records = []
        self.maxRecords = maxRecords
        self.start = dt.datetime.now()
        self.last = self.start
        self.records.append(self.last - self.start)
        self.elapsed = self.last - self.start
        self.__totalRecords__ = self.elapsed

    def __adjustRecords__(self):
        """
        Clean the first element of the list if needed and adjust elapsed time
        """
        if len(self.records) >= self.maxRecords:
            tmp = self.records.pop(0)
            self.__totalRecords__ -= tmp

    def updateElapsedTime(self):
        """
        Update the elapsed time
        """
        self.__adjustRecords__()
        tmp = dt.datetime.now()
        timeElapsed = tmp - self.last
        self.last = tmp

        self.elapsed += (timeElapsed)
        self.records.append(timeElapsed)
        self.__totalRecords__ += timeElapsed
        return self.elapsed

    def printTime(self):
        """
        Print start time and how much time is elapsed
        """
        print("Started at", end=' ')
        print(self.start, end=' ')
        print("- Time elapsed", end=' ')
        print(self.elapsed)

    def updateAndPrint(self):
        self.updateElapsedTime()
        self.printTime()

    def printRemainingTime(self, remainingItems: int):
        """
        Print the remaining time based on the medium elapsed time
        """
        mediumTime = (self.__totalRecords__ / len(self.records))
        remainingTime = mediumTime * remainingItems
        print("Remaining time about " + str(remainingTime))
