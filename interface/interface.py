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
            strings = []
            strings.append(string)
        else:
            _help_message('If you want to use m1, pass --file or --string')

        # Run mode_1
        modes.mode_1(is_verbose, strings)

    if mode == 'm2':
        if string_length is not None and number_of_generations is not None:
            # Run mode 2
            modes.mode_2(is_verbose, string_length, number_of_generations)
        else:
            _help_message('If you want to use the m2, pass --string_length '
                          + 'and --number_of_generations')

    if mode == 'm3':
        if (start_n is not None and stride is not None and
                number_of_strides is not None and
                number_of_generations is not None):
            # Run mode 3
            modes.mode_3(start_n, stride, number_of_strides,
                         number_of_generations)
        else:
            _help_message('If you want to use the m3, pass --start_n '
                          + 'and --stride '
                          + 'and --number_of_strides '
                          + 'and --number_of_generations')
