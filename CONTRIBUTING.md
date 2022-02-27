# Contributing

First off, thanks! You can contribute to the repo via the following steps.

1. Fork this repository and clone your fork into a local machine.
2. Install poetry with: `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - --version 1.1.13`
3. Open a terminal in the cloned folder and create a virtual environment using: `poetry shell` and install dependencies with `poetry install`
4. You can put the environment variable in a local `.env` file
5. Test the program `python -m unittest discover`. Read [main.py:L289](main.py#L289) before step 6.
6. Finally run it in development mode with `python -m main --dev`.

## Resources

- [All about git](https://stackoverflow.com/q/315911)
- [Poetry](https://python-poetry.org/)
- [Unit testing](https://docs.python.org/3/library/unittest.html)
