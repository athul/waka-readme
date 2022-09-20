FROM python:slim-bullseye

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    # pip:
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # poetry:
    # POETRY_VERSION=1.1.14 \
    POETRY_NO_INTERACTION=1 \
    POETRY_CACHE_DIR=/var/cache/pypoetry \
    PATH=${PATH}:/root/.local/bin

# copy project files
COPY pyproject.toml poetry.lock main.py /

# install poetry & dependencies
RUN apt-get update && apt-get install --no-install-recommends -y curl \
    && curl -sSL https://install.python-poetry.org | python - \
    && poetry install --no-root --no-ansi --only main

# copy and run program
CMD [ "poetry", "run", "python", "/main.py" ]
