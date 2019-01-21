# unique-variables
# Bartlomiej Kulik

"""RLE representation support module."""

class RLEelement:
    """Store information about one RLE element like '4A' or '5B'."""

    def __init__(self, counter, letter):
        self.counter = counter
        self.letter = letter

    def __str__(self):
        return str(self.counter) + self.letter

    def rle_element_to_str(self):
        """Return the string based on RLE representation."""

        return self.counter * self.letter

def str_to_rle_element_list(string):
    """Return the list of RLEelements."""

    # check special cases

    # list is empty when given string has less than 1 chatacters
    if not string:
        return []

    # main algorithm
    previous = string[0]
    counter = 1
    list_to_return = []
    for i in range(1, len(string)):
        current = string[i]
        if current == previous:
            counter += 1
        else:
            list_to_return.append(RLEelement(counter, previous))
            counter = 1
        previous = current
    # append last or first sequence of letters
    list_to_return.append(RLEelement(counter, previous))

    return list_to_return

def rle_element_list_to_str(rle_element_list, index_a=None, index_b=None):
    """
    Return the string.
    If index_a or/and index_b are given, function returns string based on a list
    with decremented counters in rle_element in rle_element_list[index_a]
    and/or rle_element_list[index_b]. Function does not modify rle_element_list.
    """

    string_to_return = ""
    if index_a is None and index_b is None:
        # no decrement counter
        for rle_element in rle_element_list:
            string_to_return += rle_element.rle_element_to_str()
    else:
        # decrement counter
        for i, rle_element in enumerate(rle_element_list):
            # double decrement counter
            if i == index_a == index_b:
                string_to_return += rle_element.rle_element_to_str()[2:]
            # single decrement counter
            elif i in (index_a, index_b):
                string_to_return += rle_element.rle_element_to_str()[1:]
            # no decrement counter
            else:
                string_to_return += rle_element.rle_element_to_str()

    return string_to_return
