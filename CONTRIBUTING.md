# Contributing

![python_ver](https://img.shields.io/badge/Python-%3E%3D3.11-blue.svg)

> First off, thank you! Please follow along.

**You need to _`fork`_ this repository and _`clone`_ it onto your system.** Inside the cloned folder, create a `.env` file with the following contents (without `# comments`):

```ini
INPUT_GH_TOKEN=EXAMPLE_GITHUB_PAT # required (for development)
INPUT_WAKATIME_API_KEY=EXAMPLE-WAKATIME-API-KEY # required
INPUT_API_BASE_URL=https://wakatime.com/api # required
INPUT_REPOSITORY=GITHUB_USERNAME/REPOSITORY_NAME # required
INPUT_COMMIT_MESSAGE=Updated WakaReadme graph with new metrics
INPUT_SHOW_TITLE=true
INPUT_SECTION_NAME=waka
INPUT_BLOCKS=->
INPUT_SHOW_TIME=true
INPUT_SHOW_TOTAL=true
INPUT_TIME_RANGE=last_7_days
INPUT_SHOW_MASKED_TIME=false
INPUT_LANG_COUNT=0
INPUT_STOP_AT_OTHER=true
```

**NEVER commit this `.env` file!**

## Using containers (recommended)

> Assumes that you already have latest version of either [`podman`](https://podman.io/) or [`docker`](https://www.docker.com/) (with [`compose`](https://docs.docker.com/compose/)) installed & configured.
>
> Replace `podman` with `docker` everywhere, if you're using the latter.

```sh
# Build
$ podman-compose -p waka-readme -f ./docker-compose.yml up -d
# Logs
$ podman logs WakaReadmeDev
# Cleanup
$ podman-compose -p waka-readme -f ./docker-compose.yml down
```

---

## Using virtual environments

> Assumes you've already installed & configured latest version of [python](https://www.python.org/) and [pdm](https://pdm.fming.dev/latest/).

1. Inside the cloned folder run the following commands to install dependencies

   ```console
   $ pdm install
   $ eval $(pdm venv activate)
   ```

   in a virtual environnement and activate it. In windows use the following

   ```ps1
   > Invoke-Expression (pdm venv activate)
   ```

   to activate virtual environment.

2. To test or execute the program in development, run:

   ```console
   (waka-readme-py3_11)$ python -m unittest discover # run tests
   (waka-readme-py3_11)$ python -m main --dev # execute program in dev mode
   ```
