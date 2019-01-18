# unique-variables
# Bartlomiej Kulik

"""Main program module."""

import click

from interface import interface

@click.command()

@click.option('--mode',
              type=str,
              default='m1',
              show_default=True,
              help='Program execution mode.')

@click.option('--is_verbose',
              type=bool,
              default=False,
              show_default=True,
              help='(m1 | m2) The flag allows you to enable the verbose mode.')

@click.option('--file',
              type=str,
              default='None',
              show_default=True,
              help='(m1) Test mode 1 with this file.')

@click.option('--string',
              type=str,
              default=None,
              show_default=True,
              help='(m1) Test mode 1 with this string.')

@click.option('--string_length',
              type=int,
              default=None,
              show_default=True,
              help='(m2 | m3) Length of the generated string.')

@click.option('--number_of_generations',
              type=int,
              default=None,
              show_default=True,
              help='(m2 | m3) Number of generations.')

@click.option('--start_n',
              type=int,
              default=None,
              show_default=True,
              help='(m3) The starting size of the problem.')

@click.option('--stride',
              type=int,
              default=None,
              show_default=True,
              help='(m3) Stride.')

@click.option('--number_of_strides',
              type=int,
              default=None,
              show_default=True,
              help='(m3) Number of strides.')


def main_interface(mode,
                   is_verbose,
                   file,
                   string,
                   string_length,
                   number_of_generations,
                   start_n,
                   stride,
                   number_of_strides):
    """
    Some options are not allowed for some modes.
    """

    interface.interface(mode,
                        is_verbose,
                        file,
                        string,
                        string_length,
                        number_of_generations,
                        start_n,
                        stride,
                        number_of_strides)

main_interface()
