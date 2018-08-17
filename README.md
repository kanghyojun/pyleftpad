pyleftpad
=========

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
