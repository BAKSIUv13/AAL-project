# unique-variables
# Bartlomiej Kulik

"""Implementation of the brute force algorithm."""

def brute_force(string):
    """Function implementing the brute force algorithm.

Return the set of unique variables.
    """

    # check special cases

    # set is empty when given string has less than 3 chatacters
    if len(string) < 3:
        return set()

    # main algorithm
    set_to_return = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            new_string = (string[:i]
                          + string[i + 1:j]
                          + string[j + 1:])
            set_to_return.add(new_string)

    return set_to_return
