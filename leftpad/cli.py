""":mod:`leftpad.cli` --- Left Pad Command Line Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import argparse

from .func import leftpad

__all__ = 'arg_parser', 'main'


def arg_parser():
    parser = argparse.ArgumentParser(description='String left pad.')
    parser.add_argument('--length', '-l', metavar='LENGTH', type=int,
                        help='A length of result.', default=0)
    parser.add_argument('--fill', '-f', metavar='FILLVALUE',
                        help='A value that filled in padded space.',
                        default=None)
    parser.add_argument('source', help='A string or integer.')
    return parser


def main():
    parser = arg_parser()
    args = parser.parse_args()
    print(leftpad(args.source, args.length, args.fill))
