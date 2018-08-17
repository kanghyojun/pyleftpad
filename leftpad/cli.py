""":mod:`leftpad.cli` --- Left Pad Command Line Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pyleftpad provide CLI called `leftpad` which one can use on your shell.

.. code-block:: bash

   $ pip install pyleftpad
   $ leftpad -n 10 foo
         foo
   $ leftpad -n 3 -f 0 7
   007

"""
import argparse

from .func import leftpad

__all__ = 'arg_parser', 'main'


def arg_parser():
    """Create argument parser using :class:`argparse.ArgumentParser`."""
    parser = argparse.ArgumentParser(description='String left pad.')
    parser.add_argument('--length', '-l', metavar='LENGTH', type=int,
                        help='A length of result.', default=0)
    parser.add_argument('--fill', '-f', metavar='FILLVALUE',
                        help='A value that filled in padded space.',
                        default=None)
    parser.add_argument('source', help='A string or integer.')
    return parser


def main():
    """Main function to be executed by CLI."""
    parser = arg_parser()
    args = parser.parse_args()
    print(leftpad(args.source, args.length, args.fill))
