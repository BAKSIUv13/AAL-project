# unique-variables
# Bartlomiej Kulik

"""Implementation of the optimal algorithm."""

from data_structures import rle

# helpful functions
def _is_special_case(rle_previous, rle_middle, rle_next):
    """Check if a given rle elements are special case."""

    return (rle_previous.letter == rle_next.letter
            and rle_middle.letter != rle_previous.letter
            and rle_middle.counter == 1)

class Optimum:
    """Class implementation of the optimal algorithm."""

    def __init__(self, string):
        self._string = string
        self._rle_element_list = rle.str_to_rle_element_list(self._string)

    def _get_special_cases_list(self):
        """Return special cases list"""

        special_cases = []
        for i, _ in enumerate(self._rle_element_list):
            if 0 < i < len(self._rle_element_list) - 1:
                rle_previous = self._rle_element_list[i - 1]
                rle_middle = self._rle_element_list[i]
                rle_next = self._rle_element_list[i + 1]
                if _is_special_case(rle_previous, rle_middle, rle_next):
                    special_cases.append(i)
        return special_cases

    def optimum(self):
        """Function implementing the optimal algorithm.

    Return a list of unique variables.
        """
        list_to_return = []
        # check special cases

        # empty self._rle_element_list
        if not self._rle_element_list:
            return list_to_return

        # only two letters
        if len(self._string) == 2:
            return list_to_return

        # only one group

        # 'aa', 'bb', ...
        if (len(self._rle_element_list) == 1
                and self._rle_element_list[0].counter < 3):
            return list_to_return
        # 'aaa', 'aaaaaaa'
        if (len(self._rle_element_list) == 1
                and self._rle_element_list[0].counter > 2):
            unique_variable = rle.rle_element_list_to_str(
                self._rle_element_list,
                0,
                0)
            list_to_return.append(unique_variable)

            return list_to_return

        special_cases = self._get_special_cases_list()
        # main algorithm
        for a_index, item in enumerate(self._rle_element_list):
            if item.counter > 1:
                unique_variable = rle.rle_element_list_to_str(
                    self._rle_element_list,
                    a_index, a_index)
                list_to_return.append(unique_variable)

            for b_index in range(a_index + 1, len(self._rle_element_list)):
                if a_index not in special_cases:
                    unique_variable = rle.rle_element_list_to_str(
                        self._rle_element_list,
                        a_index,
                        b_index)
                    list_to_return.append(unique_variable)
                else:
                    if (a_index > 0 and
                            self._rle_element_list[b_index].letter
                            == self._rle_element_list[a_index - 1].letter and
                            a_index == b_index - 1):
                        continue
                    else:
                        unique_variable = rle.rle_element_list_to_str(
                            self._rle_element_list,
                            a_index, b_index)
                        list_to_return.append(unique_variable)

        return list_to_return
