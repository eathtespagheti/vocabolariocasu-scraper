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
