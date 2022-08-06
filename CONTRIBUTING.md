# Contributing

![python_ver](https://img.shields.io/badge/python-%5E3.10-blue.svg)

First off, thank you! Please follow along.

1. Fork this repository and clone your fork into a local machine.
2. Install poetry with: `curl -sSL https://install.python-poetry.org | python -`
3. Open a terminal in the cloned folder and create a virtual environment using: `poetry shell` and install dependencies with `poetry install`
4. Put environment variables in a local `.env` file
5. Test the program `python -m unittest discover`.
6. Read [main.py:L389](main.py#L389) before step 7.
7. Finally run it in development mode with `python -m main --dev`.

## Resources

- [All about git](https://stackoverflow.com/q/315911)
- [Poetry](https://python-poetry.org/)
- [Unit testing](https://docs.python.org/3/library/unittest.html)
