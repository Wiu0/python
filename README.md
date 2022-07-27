<img src="docs/source/mypy_light.svg" alt="mypy logo" width="300px"/>

Python Study: Samples
=======================================


Got a question?
---------------

We are always happy to answer questions! Here are some good places to ask them:

- for anything you're curious about, try [gitter chat](https://gitter.im/python/typing)
- for general questions about Python typing, try [typing discussions](https://github.com/python/typing/discussions)

If you're just getting started,
[the documentation](https://mypy.readthedocs.io/en/stable/index.html)
and [type hints cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
can also help answer questions.

If you think you've found a bug:

- check our [common issues page](https://mypy.readthedocs.io/en/stable/common_issues.html)
- search our [issue tracker](https://github.com/python/mypy/issues) to see if
  it's already been reported
- consider asking on [gitter chat](https://gitter.im/python/typing)

To report a bug or request an enhancement:

- report at [our issue tracker](https://github.com/python/mypy/issues)
- if the issue is with a specific library or function, consider reporting it at
  [typeshed tracker](https://github.com/python/typeshed/issues) or the issue
  tracker for that library

To discuss a new type system feature:
- discuss at [typing-sig mailing list](https://mail.python.org/archives/list/typing-sig@python.org/)
- there is also some historical discussion [here](https://github.com/python/typing/issues)


What is this?
-------------

Here is a small example :

```python
number = input("What is your favourite number?")
print("It is", number + 1)  # error: Unsupported operand types for + ("str" and "int")
```


Quick start
-----------

Xxx can be installed using pip:

    python3 -m pip install -U xx

If you want to run the latest version of the code, you can install from the
repo directly:

Contributing
------------

Help in testing, development, documentation and other tasks is
highly appreciated and useful to the project. There are tasks for
contributors of all experience levels.

To get started with developing mypy, see [CONTRIBUTING.md](CONTRIBUTING.md).

If you need help getting started, don't hesitate to ask on [gitter](https://gitter.im/python/typing).


Development status
------------------

----------------------------------

