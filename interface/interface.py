# unique-variables
# Bartlomiej Kulik

"""The module responsible for user interface."""

import sys

from interface import modes

def _help_message(message):
    print(message)
    print()
    print('To get more information, run: main.py --help')

    sys.exit(0)

def interface(mode,
              is_verbose,
              file_name,
              string,
              string_length,
              number_of_generations,
              start_n,
              stride,
              number_of_strides):
    """The function responsible for running modes."""

    # check if given mode is valid
    if mode not in ('m1', 'm2', 'm3'):
        _help_message('Available modes: m1 | m2 | m3')

    if mode == 'm1':
        if file_name is not None:
            with open(file_name) as file:
                strings = file.readlines()
                strings = [x.strip() for x in strings]
        elif string is not None:
            strings = list()
            strings.append(string)
        else:
            _help_message('If you want to use the first mode, pass file_name '
                          + 'or string')

        # Run mode_1
        modes.mode_1(is_verbose, strings)

    if mode == 'm2':
        pass

    if mode == 'm3':
        pass
