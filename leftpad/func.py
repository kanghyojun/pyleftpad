""":mod:`leftpad.func` --- Left Pad functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Define left pad functions.
"""
__all__ = 'leftpad',


def leftpad(source, length, fill_value=None):
    """String left pad.

    .. code-block:: python

       >>> leftpad('foo', 5)
       '  foo'
       >>> leftpad('foobar', 6)
       'foobar'
       >>> leftpad(1, 2, '0')
       '01'
       >>> leftpad(17, 5, 0)
       '00017'

    :param source: A string or integer.
    :type source: :class:`str` or :class:`int`
    :param length: A length of result.
    :type length: :class:`int`
    :param fill_value: A value that filled in padded space.
    :type fill_value: :class:`str` or :class:`int`
    :return: A padded string.
    :rtype: :class:`str`

    """
    if not isinstance(source, (str, int)):
        raise TypeError(
            '`source` expected to be one of str, int: {}'.format(source)
        )
    if not isinstance(length, int):
        raise TypeError(
            '`length` expected to be int: {}'.format(length)
        )
    if not (fill_value is None or isinstance(fill_value, (str, int))):
        raise TypeError(
            '`fill_value` expected to be one of str, int: {}'.format(
                fill_value
            )
        )
    source = str(source)
    length -= len(source)
    if length <= 0:
        return source
    if fill_value != 0 and not fill_value:
        fill_value = ' '
    fill_value = str(fill_value)
    return fill_value * length + source
