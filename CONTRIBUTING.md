# Contributing

![python_ver](https://img.shields.io/badge/python-%5E3.10-blue.svg)

> First off, thank you! Please follow along.

**You need to _fork_ this repository and _clone_ it, onto your system.**

## Using Docker/Podman (recommended)

> Assumes you've already installed & configured latest version of [docker](https://www.docker.com/) or [podman](https://podman.io/).
>
> Replace `docker` with `podman` everywhere, if you're using the latter.

1. **Inside the cloned folder**, run:

   ```console
   $ git archive -o 'waka-readme.tar.gz' HEAD
   $ docker build . -f containerfile -t 'waka-readme:dev'
   ```

   to build an image. (Image is identified as `<name>:<tag>`)

2. Then create containers and use them as dev environments.

   - Temporary:

     ```console
     $ docker run --rm -it --name 'WakaReadmeDev' 'waka-readme:dev' bash
     ```

   - or Persistent

     ```console
     $ docker run --detach --name 'WakaReadmeDev' 'waka-readme:dev'
     ```

   where `WakaReadmeDev` is the docker container name. Then execute `bash` in the container:

   ```console
   $ docker exec -it 'WakaReadmeDev' bash
   ```

3. For development, you can attach code editor of your choice to this container.
4. Export environnement variables with edits, as required:

   ```console
   // inside container, create a file `.env`
   # micro .env
   ```

   paste (`Ctrl+Shift+V`) the following contents:

   ```env
   INPUT_GH_TOKEN='<GITHUB TOKEN>'
   INPUT_WAKATIME_API_KEY='<WAKATIME API KEY>'
   INPUT_API_BASE_URL='https://wakatime.com/api'
   INPUT_REPOSITORY='<REPOSITORY SLUG>'
   INPUT_COMMIT_MESSAGE='<COMMIT MESSAGE>'
   INPUT_SHOW_TITLE='True'
   INPUT_SECTION_NAME='waka'
   INPUT_BLOCKS='->'
   INPUT_SHOW_TIME='True'
   INPUT_SHOW_TOTAL='True'
   INPUT_TIME_RANGE='last_7_days'
   INPUT_SHOW_MASKED_TIME='True'
   ```

   and execute program with:

   ```console
   # poetry shell
   # set -a && . ./.env && set +a # optional
   (venv)# python -m main --dev
   (venv)# python -m unittest discover # run tests
   ```

5. Later, to remove stop and remove the container:

   ```console
   // exit container
   # exit

   $ docker container stop 'WakaReadmeDev'
   $ docker container rm 'WakaReadmeDev'
   ```

---

> **NOTE** With VSCode on Windows
>
> Add these to `.vscode/settings.json`
>
> ```json
> {
>   "terminal.integrated.commandsToSkipShell": [
>     "-workbench.action.quickOpenView"
>   ]
> }
> ```
>
> To quit the `micro` editor from the vscode terminal.

---

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
   INPUT_SECTION_NAME='waka'
   INPUT_BLOCKS='->'
   INPUT_SHOW_TIME='True'
   INPUT_SHOW_TOTAL='True'
   INPUT_TIME_RANGE='last_7_days'
   INPUT_SHOW_MASKED_TIME='True'
   ```

3. Execute program in development mode with:

   ```console
   $ set -a && . ./.env && set +a # optional
   (venv)$ python -m main --dev
   (venv)$ python -m unittest discover # run tests
   ```
