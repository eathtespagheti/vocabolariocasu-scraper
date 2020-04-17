def print_tab(number_of_tabs: int):
    """
    Print some tabs in stdout
    """
    for _ in range(number_of_tabs):
        print('    ', end='')


def print_progress(index: int, total: int, print_percentage: bool = False):
    """
    Draw a simple progress value in the stdout
    """
    if print_percentage:
        percentage_value = (100 * index) / total
        percentage_value = "{0:.2f}".format(percentage_value)
        print(percentage_value + "%", end=' ')
    print("[" + str(index) + "/" + str(total) + "]", end=' ')
