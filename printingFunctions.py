def printTab(numberOfTabs: int):
    """
    Print some tabs in stdout
    """
    for val in range(numberOfTabs):
        print('    ', end='')


def printPercentage(index: int, total: int):
    """
    Draw a simple progress value in the stdout
    """
    percentageValue = (100 * index) / total
    percentageValue = "{0:.2f}".format(percentageValue)
    print(percentageValue + "% [" + str(index) +
          "/" + str(total) + "]", end=' ')
