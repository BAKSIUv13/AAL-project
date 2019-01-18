# unique-variables
# Bartlomiej Kulik

"""The main module responsible for the tests."""

from algorithms import brute_force
from algorithms import optimum

class SingleTest:
    """Class responsible for one test."""

    def __init__(self, string):
        self._string = string
        self._brute_force_list = list()
        self._optimum_list = list()
        self._is_the_same = None

    def get_brute_force_list(self):
        """Return brute force list."""

        return self._brute_force_list.copy()

    def get_optimum_list(self):
        """Return optimum list."""

        return self._optimum_list.copy()

    def run_single_test(self):
        """Run signle test.

Return True, if the optimum result is the same as the brute force result.
"""

        self._brute_force_list = brute_force.brute_force(self._string)
        self._optimum_list = optimum.Optimum(self._string).optimum()

        # compare sorted lists
        self._is_the_same = (self._brute_force_list.sort()
                             == self._optimum_list.sort())

        return self._is_the_same

    def get_size(self):
        """Return the solution(optimum) size"""

        return len(self._optimum_list)
