# unique-variables
# Bartlomiej Kulik

"""Implementation of the brute force algorithm."""

def brute_force(string):
    """Function implementing the brute force algorithm.

Return a set of unique variables.
    """
    set_to_return = set()
    # check special cases
    if len(string) < 3:
        return set()

    for a_index in range(len(string)):
        for b_index in range(a_index + 1, len(string)):
            new_string = (string[:a_index]
                          + string[a_index + 1:b_index]
                          + string[b_index + 1:])
            set_to_return.add(new_string)

    return set_to_return
