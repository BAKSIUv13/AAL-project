# unique-variables
# Bartlomiej Kulik

"""Module responsible for execution modes."""

import string
import random
import itertools
import time
import matplotlib.pyplot as plt

from tests import main_tests
from algorithms import brute_force
from algorithms import optimum

def _generate_string(string_length):
    return ''.join(random.SystemRandom().choice(string.ascii_lowercase)
                   for _ in range(string_length))

def mode_1(is_verbose, strings):
    """Mode 1 implementation. strings argument is iterable object."""

    for _string in strings:
        test = main_tests.SingleTest(_string)
        is_ok = test.run_single_test()

        print('string:', _string)
        if is_ok:
            print('TEST PASSED:', test.get_size(), 'unique variables\n')
            if is_verbose:
                print('unique variables:')
                for unique_variable in test.get_optimum_list():
                    print(unique_variable)
                print()
        else:
            print('TEST FAILED\n')

def mode_2(is_verbose, string_length, number_of_generations):
    """Mode 2 implementation."""

    generated_strings = []
    for _ in itertools.repeat(None, number_of_generations):
        generated_strings.append(_generate_string(string_length))

    mode_1(is_verbose, generated_strings)

def _theoretical_evaluation(n_size):
    # n^3 + n
    return (n_size ** 3) + n_size

def mode_3(start_n, stride, number_of_strides,
           number_of_generations, is_m3_fast):
    """Mode 3 implementation."""

    # lists to generate chart
    x_arg = []
    y_optimum = []
    y_brute_force = []
    q_n = []
    for n_size in range(start_n, start_n + stride * number_of_strides, stride):
        # main mode loop
        y_optimum_raw = []
        y_brute_force_raw = []
        for _ in itertools.repeat(None, number_of_generations):
            # number_of_generations - number of problem instances for
            # the fixed n_size
            generated_string = _generate_string(n_size)
            # prepare optimum algorithm - intialize instance of the problem
            optimum_instance = optimum.Optimum(generated_string)

            start = time.time()
            optimum_instance.optimum()
            end = time.time()
            result = end - start

            y_optimum_raw.append(result)

            if not is_m3_fast:
                start = time.time()
                brute_force.brute_force(generated_string)
                end = time.time()
                result = end - start

                y_brute_force_raw.append(result)

        y_optimum.append(sum(y_optimum_raw) / float(len(y_optimum_raw)))
        if not is_m3_fast:
            y_brute_force.append(sum(y_brute_force_raw)
                                 / float(len(y_brute_force_raw)))

        x_arg.append(n_size)

    # q_n
    n_median = len(x_arg) // 2
    t_divided_t_median = (_theoretical_evaluation(x_arg[n_median])
                          / y_optimum[n_median])
    for i, arg in enumerate(x_arg):
        q_n.append((y_optimum[i] / _theoretical_evaluation(arg))
                   * t_divided_t_median)

    plt.plot(x_arg, y_optimum, color='green')
    if not is_m3_fast:
        plt.plot(x_arg, y_brute_force, color='red')
    plt.xlabel('N')
    plt.ylabel('Time[s]')
    if not is_m3_fast:
        plt.title('Comparison between brute force(red) and optimum(green)')
    else:
        plt.title(' Optimum algorithm with asymptote n^3 + n')

    # Table displayed on the screen
    print('Algorithm with asymptote n^3 + n')
    print('{0:16}{1:16}{2:16}'.format('n', 't(n)[s]', 'q(n)'))
    print()

    print('{0:16}{1:16}{2:16}'.format(str(x_arg[0]),
                                      str(round(y_optimum[0], 10)),
                                      str(q_n[0])))

    print('{0:16}{1:16}{2:16}'.format(str(x_arg[1]),
                                      str(round(y_optimum[1], 10)),
                                      str(q_n[1])))

    print('{0:16}{1:16}{2:16}'.format('....', '....', '....'))


    print('{0:16}{1:16}{2:16}'.format(str(x_arg[n_median]),
                                      str(round(y_optimum[n_median], 10)),
                                      str(q_n[n_median])))

    print('{0:16}{1:16}{2:16}'.format('....', '....', '....'))

    n_last = len(x_arg) - 1
    print('{0:16}{1:16}{2:16}'.format(str(x_arg[n_last - 1]),
                                      str(round(y_optimum[n_last - 1], 10)),
                                      str(q_n[n_last - 1])))

    print('{0:16}{1:16}{2:16}'.format(str(x_arg[n_last]),
                                      str(round(y_optimum[n_last], 10)),
                                      str(q_n[n_last])))

    plt.show()
