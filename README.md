pyleftpad
=========

[![PyPI version](https://badge.fury.io/py/pyleftpad.svg)](https://badge.fury.io/py/pyleftpad)
[![Build Status](https://travis-ci.org/admire93/pyleftpad.svg?branch=master)](https://travis-ci.org/admire93/pyleftpad)
[![Documentation Status](https://readthedocs.org/projects/pyleftpad/badge/?version=latest)](https://pyleftpad.readthedocs.io/en/latest/?badge=latest)

Python version of [left pad][leftpad].

[leftpad]: https://www.npmjs.com/package/left-pad


## Install

```bash
$ pip install pyleftpad
```


## Usage

There are two way to use pyleftpad. First of all, you can use `leftpad()`
function from `leftpad` module in your Python script.

```python
from leftpad import leftpad

def main():
    print(leftpad('hello world', 40))


main()
```

Second of all, you can use directly `leftpad` command in your shell.

```bash
$ leftpad -l 40 "hello world"
```
