# unique-variables
# Bartlomiej Kulik

"""Implementation of the brute force algorithm."""

def brute_force(string):
    """Function implementing the brute force algorithm.

Return the list of unique variables.
    """

    # check special cases

    # list is empty when given string has less than 3 chatacters
    if len(string) < 3:
        return list()

    # main algorithm
    list_to_return = list()
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            new_string = (string[:i]
                          + string[i + 1:j]
                          + string[j + 1:])
            if new_string not in list_to_return:
                list_to_return.append(new_string)
                list_to_return.sort()

    return list_to_return
