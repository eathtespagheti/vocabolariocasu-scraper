import datetime as dt


class timeManager:
    """
    Manage time in the script
    """
    startTime: dt.datetime
    timeElapsed: dt.timedelta
    lastTime: dt.datetime

    def start(self):
        """
        Set the starting time for the timeManager
        """
        self.startTime = dt.datetime.now()
        self.lastTime = self.startTime
        self.timeElapsed = self.lastTime - self.startTime

    def updateElapsedTime(self):
        """
        Update the elapsed time
        """
        tmpTime = dt.datetime.now()
        self.timeElapsed += (tmpTime - self.lastTime)
        self.lastTime = tmpTime
        return self.timeElapsed

    def printTime(self):
        """
        Print start time and how much time is elapsed
        """
        print("Started at", end=' ')
        print(self.startTime, end=' ')
        print("Time elapsed", end=' ')
        print(self.timeElapsed)
