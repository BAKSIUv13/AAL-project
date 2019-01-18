# unique-variables
# Bartlomiej Kulik

"""Implementation of the optimal algorithm."""

from data_structures import rle

# helpful function
def _is_special_case(rle_element_previous,
                     rle_element_middle,
                     rle_element_next):
    """Check if a given rle elements are special case."""

    return (rle_element_previous.letter == rle_element_next.letter
            and rle_element_middle.letter != rle_element_previous.letter
            and rle_element_middle.counter == 1)

class Optimum:
    """Class implementation of the optimal algorithm."""

    def __init__(self, string):
        self._string = string
        self._rle_element_list = rle.str_to_rle_element_list(self._string)

    def get_string(self):
        """Return the string."""

        return self._string

    def _get_special_cases_list(self):
        """Return the special cases list."""

        special_cases = []
        for i, _ in enumerate(self._rle_element_list):
            if 0 < i < len(self._rle_element_list) - 1:
                rle_element_previous = self._rle_element_list[i - 1]
                rle_element_middle = self._rle_element_list[i]
                rle_element_next = self._rle_element_list[i + 1]

                if _is_special_case(rle_element_previous,
                                    rle_element_middle,
                                    rle_element_next):
                    special_cases.append(i)

        return special_cases

    def optimum(self):
        """
        Function implementing the optimal algorithm.
        Return the list of unique variables.
        """
        # check special cases

        # list is empty when given string has less than 3 characters
        if len(self._string) < 3:
            return []

        # main algorithm
        special_cases = self._get_special_cases_list()
        list_to_return = []
        for i, item in enumerate(self._rle_element_list):
            # 'aaaabcde'
            #  i   b
            #
            # i index refers to RLEelement which counter is > 1
            if item.counter > 1:
                unique_variable = rle.rle_element_list_to_str(
                    self._rle_element_list,
                    i,
                    i)
                list_to_return.append(unique_variable)
            # the deepest loop
            for j in range(i + 1, len(self._rle_element_list)):
                if i not in special_cases:
                    unique_variable = rle.rle_element_list_to_str(
                        self._rle_element_list,
                        i,
                        j)
                    list_to_return.append(unique_variable)
                else:
                    if (i > 0 and
                            self._rle_element_list[j].letter
                            == self._rle_element_list[i - 1].letter and
                            i == j - 1):
                        # we checked it before
                        continue
                    else:
                        unique_variable = rle.rle_element_list_to_str(
                            self._rle_element_list,
                            i,
                            j)
                        list_to_return.append(unique_variable)

        return list_to_return
