FROM python:slim-bullseye

WORKDIR /root/waka-readme/

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

# import project
ADD waka-readme.tar.gz .

# install poetry & dependencies
RUN apt-get update && apt-get install --no-install-recommends -y curl git micro \
    && curl -sSL https://install.python-poetry.org | python - \
    && poetry install --no-root --no-ansi

# copy and run program
CMD [ "sleep", "infinity" ]
