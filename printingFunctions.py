def printTab(numberOfTabs: int):
    """
    Print some tabs in stdout
    """
    for val in range(numberOfTabs):
        print('    ', end='')


def printProgress(index: int, total: int, printPercentage: bool = False):
    """
    Draw a simple progress value in the stdout
    """
    if printPercentage:
        percentageValue = (100 * index) / total
        percentageValue = "{0:.2f}".format(percentageValue)
        print(percentageValue + "%", end=' ')
    print("[" + str(index) + "/" + str(total) + "]", end=' ')


def printRemainingTime(values: list, remainingItems: int):
    """
    Print the remaining time based on the medium elapsed time
    """
    total = 0
    for value in values:
        total += value

    timeUnits = ['ms', 's', 'm', 'h', ' days']

    mediumTime = (total / len(values)) / 1000
    unit = 1
    remainingTime = mediumTime * remainingItems

    # Convert in milliseconds
    if remainingTime < 0:
        remainingTime *= 1000
        unit = 0
    # Convert in minutes
    if remainingTime > 60:
        remainingTime /= 60
        unit = 2
    # Convert in hours
    if remainingTime > 60:
        remainingTime /= 60
        unit += 1
    # Convert in days
    if remainingTime > 24:
        remainingTime /= 24
        unit += 1

    print("Remaining time about " + str(int(remainingTime)) + timeUnits[unit])
