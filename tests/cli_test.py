import argparse

from pytest import mark, raises

from leftpad.cli import arg_parser


@mark.parametrize('arg, namespace', [
    ('foo', argparse.Namespace(source='foo', fill=None, length=0)),
    ('--length 1 foo', argparse.Namespace(source='foo', fill=None, length=1)),
    ('--l 1 foo', argparse.Namespace(source='foo', fill=None, length=1)),
    ('--fill a foo', argparse.Namespace(source='foo', fill='a', length=0)),
    ('-f a foo', argparse.Namespace(source='foo', fill='a', length=0)),
])
def test_arg_parser(arg, namespace):
    parser = arg_parser()
    actual = parser.parse_args(arg.split(' '))
    assert actual == namespace


@mark.parametrize('arg', [
    '',
    '-l 1',
    '-f a',
    '-l 1 -f a',
])
def test_arg_parser_error(arg):
    parser = arg_parser()
    with raises(SystemExit):
        parser.parse_args(arg)
