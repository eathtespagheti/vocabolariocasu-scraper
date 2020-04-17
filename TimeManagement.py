import datetime as dt
from printingFunctions import print_tab


class TimeManager:
    """
    Manage time in the script
    """
    start: dt.datetime
    last: dt.datetime
    elapsed: dt.timedelta
    records: list
    max_records: int
    __total_records__: dt.timedelta

    def __init__(self, max_records: int = 500):
        """
        Set the starting time for the timeManager
        """
        self.records = []
        self.max_records = max_records
        self.start = dt.datetime.now()
        self.last = self.start
        self.records.append(self.last - self.start)
        self.elapsed = self.last - self.start
        self.__total_records__ = self.elapsed

    def __adjust_records__(self):
        """
        Clean the first element of the list if needed and adjust elapsed time
        """
        if len(self.records) >= self.max_records:
            tmp = self.records.pop(0)
            self.__total_records__ -= tmp

    def update_elapsed_time(self):
        """
        Update the elapsed time
        """
        self.__adjust_records__()
        tmp = dt.datetime.now()
        time_elapsed = tmp - self.last
        self.last = tmp
        self.elapsed += (time_elapsed)
        self.records.append(time_elapsed)
        self.__total_records__ += time_elapsed
        return self.elapsed

    def print_time(self, tabs: int = 1):
        """
        Print start time and how much time is elapsed
        """
        print_tab(tabs)
        print("Started at", end=' ')
        print(self.start)
        print_tab(tabs)
        print("Time elapsed", end=' ')
        print(self.elapsed)

    def update_and_print(self, tabs: int = 1):
        self.update_elapsed_time()
        self.print_time(tabs)

    def print_remaining_time(self, remaining_items: int, tabs: int = 1):
        """
        Print the remaining time based on the medium elapsed time
        """
        medium_time = (self.__total_records__ / len(self.records))
        remaining_time = medium_time * remaining_items
        print_tab(tabs)
        print("Remaining time about " + str(remaining_time))
