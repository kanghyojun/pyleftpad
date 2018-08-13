from pytest import mark, raises

from leftpad.func import leftpad


@mark.parametrize(
    'source, length, fill_value, expected',
    [
        # If length lesser than 4, then actual is equivalent to 'foo'.
        ('foo', -1, None, 'foo'),
        ('foo', 0, None, 'foo'),
        ('foo', 1, None, 'foo'),
        ('foo', 2, None, 'foo'),
        ('foo', 3, None, 'foo'),
        # If length lesser than 4, then actual is equivalent to 123.
        (123, -1, None, '123'),
        (123, 0, None, '123'),
        (123, 1, None, '123'),
        (123, 2, None, '123'),
        (123, 3, None, '123'),
        # If fill_value is None, then fill_value has to be 1 space.
        ('foo', 4, None, ' foo'),
        ('foo', 5, None, '  foo'),
        # If fill_value is '', then fill_value has to be 1 space.
        ('foo', 4, '', ' foo'),
        ('foo', 5, '', '  foo'),
        # If fill_value is None, then fill_value has to be 1 space with int.
        (123, 4, None, ' 123'),
        (123, 5, None, '  123'),
        # When fill_value is given.
        ('foo', 4, '*', '*foo'),
        ('foo', 5, '*', '**foo'),
        # When fill_value is 0.
        (123, 4, 0, '0123'),
        (123, 5, 0, '00123'),
        # When fill_value's length is longer.
        ('foo', 4, 'bar', 'barfoo'),
        ('foo', 5, 'bar', 'barbarfoo'),
        (123, 4, 777, '777123'),
        (123, 5, 777, '777777123'),
        # When mixed str and int
        ('foo', 4, 0, '0foo'),
        ('foo', 5, 0, '00foo'),
        (123, 4, 'c', 'c123'),
        (123, 5, 'c', 'cc123'),
    ]
)
def test_leftpad(source, length, fill_value, expected):
    actual = leftpad(source, length, fill_value)
    assert actual == expected


@mark.parametrize('arg, expected_message', [
    ((1.1, 0), '`source` expected to be one of str, int: 1.1'),
    (('bar', 'foo'), '`length` expected to be int: foo'),
    (
        ('bar', 1, 2.1),
        '`fill_value` expected to be one of str, int: 2.1'
    ),
])
def test_leftpad_type_error(arg, expected_message):
    with raises(TypeError) as error:
        leftpad(*arg)
    assert error.value.args[0] == expected_message
