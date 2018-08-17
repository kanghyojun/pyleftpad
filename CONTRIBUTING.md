# Contributing to pyleftpad

Thanks for your contribution!


## Documentation

- It would be recommended to write documentation.
- Use docstring to write documentation.
- It would be great if there is example code on documentation.
- We use [Sphinx] to build documentation.
- Write a changelog.
  - We believe logging changes is a part of making software.

[Sphinx]: http://www.sphinx-doc.org/en/master/


## Coding styles

- Follow [PEP 8][pep8].
  - It would be always checked on CI with [flake8]
- In general stdlib comes first, then 3rd party, then local packages,
  and that each group is individually alphabetized.
  - See detail, [flake8-import-order-spoqa]
- It is recommend to run `hooks/pre-commit` before you make a commit.
  To run the script automatically, add `hooks` directory on your
  `core.hooksPath`.

  ```bash
  $ ./hooks/pre-commit
  $ # or
  $ git config core.hooksPath "$PWD/hooks"
  $ git commit
  ```

[pep8]: https://www.python.org/dev/peps/pep-0008/
[flake8]: http://flake8.pycqa.org/en/latest/
[flake8-import-order-spoqa]: https://pypi.org/project/flake8-import-order-spoqa/
