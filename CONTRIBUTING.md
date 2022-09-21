# Contributing

![python_ver](https://img.shields.io/badge/python-%5E3.10-blue.svg)

First off, thank you! Please follow along. 

> **_You need to fork this repository and clone it, onto your system._**

## Using docker (recommended)

> Assumes you've already installed & configured latest version of [docker](https://www.docker.com/).

1. **Inside the cloned folder**, run:

   ```console
   $ git archive -o 'waka-readme.tar.gz' HEAD
   $ docker build . -t 'waka-readme:dev' -f 'DockerfileDev'
   ```

   to build an image. (Image is identified as `<name>:<tag>`)

2. Then create containers and use them as dev environments.
    - Temporary:

        ```console
        $ docker run --rm -it --name 'WakaReadme' 'waka-readme:dev' bash
        ```

    - or Persistent

        ```console
        $ docker run --detach --name 'WakaReadme' 'waka-readme:dev'
        $ docker exec -it 'WakaReadme' bash
        ```

        where `WakaReadme` is the docker container name.

3. For development, you can attach code editor of your choice to this container.
4. Export environnement variables with edits, as required:

    ```console
    // inside container

    # export INPUT_GH_TOKEN='<GITHUB TOKEN>' \
    && export INPUT_WAKATIME_API_KEY='<WAKATIME API KEY>' \
    && export INPUT_API_BASE_URL='https://wakatime.com/api' \
    && export INPUT_REPOSITORY='<REPOSITORY SLUG>' \
    && export INPUT_COMMIT_MESSAGE='<COMMIT MESSAGE>' \
    && export INPUT_SHOW_TITLE='True' \
    && export INPUT_BLOCKS='->' \
    && export INPUT_SHOW_TIME='True' \
    && export INPUT_SHOW_TOTAL='True' \
    && export INPUT_TIME_RANGE='last_7_days' \
    && export INPUT_SHOW_MASKED_TIME='True'
    ```

    and execute program with:

    ```console
    # poetry shell
    (venv)# python -m main --dev
    ```

5. Later, to remove stop and remove the container:

    ```console
    // exit container
    # exit

    $ docker container stop 'WakaReadme'
    $ docker container rm 'WakaReadme'
    ```

## Manual

> Assumes you've already installed & configured latest version of [python](https://www.python.org/) and [poetry](https://python-poetry.org/).

1. Inside the cloned folder run:

   ```console
   $ poetry shell
   (venv)$ poetry install
   ```

   to create and activate a virtual environnement and install dependencies.

2. Put environment variables in a `.env` file

    ```env
    INPUT_GH_TOKEN='<GITHUB TOKEN>'
    INPUT_WAKATIME_API_KEY='<WAKATIME API KEY>'
    INPUT_API_BASE_URL='https://wakatime.com/api'
    INPUT_REPOSITORY='<REPOSITORY SLUG>'
    INPUT_COMMIT_MESSAGE='<COMMIT MESSAGE>'
    INPUT_SHOW_TITLE='True'
    INPUT_BLOCKS='->'
    INPUT_SHOW_TIME='True'
    INPUT_SHOW_TOTAL='True'
    INPUT_TIME_RANGE='last_7_days'
    INPUT_SHOW_MASKED_TIME='True'
    ```

3. Execute program in development mode with:

    ```console
    (venv)$ python -m main --dev
    ```
