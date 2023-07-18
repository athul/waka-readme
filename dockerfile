FROM docker.io/python:3-slim

ENV INPUT_GH_TOKEN \
    INPUT_WAKATIME_API_KEY \
    INPUT_API_BASE_URL \
    INPUT_REPOSITORY \
    INPUT_COMMIT_MESSAGE \
    INPUT_SHOW_TITLE \
    INPUT_SECTION_NAME \
    INPUT_BLOCKS \
    INPUT_SHOW_TIME \
    INPUT_SHOW_TOTAL \
    INPUT_TIME_RANGE \
    INPUT_SHOW_MASKED_TIME \
    INPUT_LANG_COUNT \
    INPUT_STOP_AT_OTHER

ENV PATH="${PATH}:/root/.local/bin" \
    # python
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    # pip
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DEFAULT_TIMEOUT=100

# copy project files
COPY --chown=root:root requirements.txt main.py /app/

# install dependencies
RUN python -m pip install -r /app/requirements.txt

# execute program
CMD python /app/main.py
