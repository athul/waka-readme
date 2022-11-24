"""
WakaReadme : WakaTime progress visualizer
=========================================

Wakatime Metrics on your Profile Readme.

Title:
------

```txt
From: 15 February, 2022 - To: 22 February, 2022
````

Byline:
-------

```txt
Total: 34 hrs 43 mins
```

Body:
-----

```txt
Python     27 hrs 29 mins  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⣀⣀⣀⣀   77.83 %
YAML       2 hrs 14 mins   ⣿⣦⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀   06.33 %
Markdown   1 hr 54 mins    ⣿⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀   05.39 %
TOML       1 hr 48 mins    ⣿⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀   05.11 %
Other      35 mins         ⣦⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀   01.68 %
```

#### Contents = Title + Byline + Body
"""

# standard
from dataclasses import dataclass
from random import SystemRandom
from datetime import datetime
from base64 import b64encode
import logging as logger
from time import sleep
from typing import Any
import sys
import re
import os

# external
# # requests
from requests.exceptions import RequestException
from requests import get as rq_get
# # github
from github import GithubException, Github
# # faker
from faker import Faker


# pylint: disable=logging-fstring-interpolation

################### data ###################

@dataclass(frozen=True, slots=True)
class WakaConstants:
    """
    WakaConstants
    -------------
    """
    prefix_length: int = 16
    graph_length: int = 25
    start_comment: str = f'<!--START_SECTION:{os.getenv('SECTION_NAME')}-->'
    end_comment: str = f'<!--END_SECTION:{os.getenv('SECTION_NAME')}-->'
    waka_block_pattern: str = f'{start_comment}[\\s\\S]+{end_comment}'


class WakaInput:
    """
    WakaInput Env Vars
    ------------------
    """

    def __init__(self) -> None:
        """
        WakaInput Initialize
        --------------------
        """
        # mapped environment variables
        # # required
        self.gh_token: str = os.getenv('INPUT_GH_TOKEN')
        self.waka_key: str = os.getenv('INPUT_WAKATIME_API_KEY')
        self.api_base_url: str = os.getenv(
            'INPUT_API_BASE_URL', 'https://wakatime.com/api'
        )
        self.repository: str = os.getenv('INPUT_REPOSITORY')
        # # depends
        self.commit_message: str = os.getenv(
            'INPUT_COMMIT_MESSAGE', 'Updated WakaReadme graph with new metrics'
        )
        # # optional
        self.show_title: str | bool = os.getenv('INPUT_SHOW_TITLE', 'False')
        self.block_style: str = os.getenv('INPUT_BLOCKS', '░▒▓█')
        self.time_range: str = os.getenv('INPUT_TIME_RANGE', 'last_7_days')
        self.show_time: str | bool = os.getenv('INPUT_SHOW_TIME', 'False')
        self.show_total_time: str | bool = os.getenv(
            'INPUT_SHOW_TOTAL', 'False'
        )
        self.show_masked_time: str | bool = os.getenv(
            'INPUT_SHOW_MASKED_TIME', 'False'
        )

    def validate_input(self) -> bool:
        """
        WakaInput Validate
        ------------------
        """

        if not (self.gh_token and self.waka_key and self.api_base_url and self.repository):
            logger.error('Invalid required input(s), refer README')
            return False

        if len(self.commit_message) < 1:
            logger.error(
                'Commit message length must be greater than 1 character long'
            )
            return False

        try:
            self.show_title: bool = strtobool(self.show_title)
            self.show_time: bool = strtobool(self.show_time)
            self.show_total_time: bool = strtobool(self.show_total_time)
            self.show_masked_time: bool = strtobool(self.show_masked_time)
        except (ValueError, AttributeError) as err:
            logger.error(err)
            return False

        if len(self.block_style) < 2:
            logger.warning(
                'Block length should be greater than 2 characters long'
            )
            logger.debug('Using default blocks: ░▒▓█')

        # 'all_time' is un-documented, should it be used?
        if self.time_range not in {
            'last_7_days', 'last_30_days', 'last_6_months', 'last_year', 'all_time'
        }:
            logger.warning('Invalid time range')
            logger.debug('Using default time range: last_7_days')
            self.time_range: str = 'last_7_days'

        return True


def strtobool(val: str) -> bool:
    """
    strtobool
    ---------

    PEP 632 https://www.python.org/dev/peps/pep-0632/ is depreciating distutils

    Following code is somewhat shamelessly copied from the original source.

    Convert a string representation of truth to True or False.

    - True values are `'y', 'yes', 't', 'true', 'on', and '1'`
    - False values are `'n', 'no', 'f', 'false', 'off', and '0'`
    - Raises `ValueError` if `val` is anything else.
    """
    val = val.lower()

    if val in {'y', 'yes', 't', 'true', 'on', '1'}:
        return True

    if val in {'n', 'no', 'f', 'false', 'off', '0'}:
        return False

    raise ValueError(f'invalid truth value for {val}')


################### logic ###################

def make_title(dawn: str, dusk: str, /) -> str:
    """
    WakaReadme Title
    ----------------

    Makes title for WakaReadme.
    """
    logger.debug('Making title')
    if not (dawn or dusk):
        logger.error('Cannot find start/end date')
        sys.exit(1)
    api_dfm, msg_dfm = '%Y-%m-%dT%H:%M:%SZ', '%d %B %Y'
    try:
        start_date = datetime.strptime(dawn, api_dfm).strftime(msg_dfm)
        end_date = datetime.strptime(dusk, api_dfm).strftime(msg_dfm)
    except ValueError as err:
        logger.error(err)
        sys.exit(1)
    logger.debug('Title was made\n')
    return f'From: {start_date} - To: {end_date}'


def make_graph(
    block_style: str, percent: float, gr_len: str, /,
    *, lg_nm: str = ''
) -> str:
    """
    WakaReadme Graph
    ----------------

    Makes time graph from the API's data.
    """
    logger.debug(f'Generating graph for "{lg_nm or "..."}"')
    markers: int = len(block_style) - 1
    proportion: float = percent / 100 * gr_len
    graph_bar: str = block_style[-1] * int(proportion + 0.5 / markers)
    remainder_block: int = int(
        (proportion - len(graph_bar)) * markers + 0.5
    )
    graph_bar += block_style[remainder_block] if remainder_block > 0 else ''
    graph_bar += block_style[0] * (gr_len - len(graph_bar))
    logger.debug(f'{lg_nm or "..."} graph generated')
    return graph_bar


def prep_content(stats: dict | None, /) -> str:
    """
    WakaReadme Prepare Markdown
    ---------------------------

    Prepared markdown content from the fetched statistics
    ```
    """
    contents: str = ''

    # Check if any data exists
    if not (lang_info := stats.get('languages')):
        logger.debug('The data seems to be empty, please wait for a day')
        contents += 'No activity tracked'
        return contents

    # make title
    if wk_i.show_title:
        contents += make_title(stats.get('start'), stats.get('end')) + '\n\n'

    # make byline
    if wk_i.show_masked_time and (
        total_time := stats.get('human_readable_total_including_other_language')
    ):
        # overrides 'human_readable_total'
        contents += f'Total Time: {total_time}\n\n'
    elif wk_i.show_total_time and (
        total_time := stats.get('human_readable_total')
    ):
        contents += f'Total Time: {total_time}\n\n'

    # make content
    logger.debug('Making contents')
    pad_len = len(
        # comment if it feels way computationally expensive
        max((str(l.get('name')) for l in lang_info), key=len)
        # and then don't for get to set pad_len to say 13 :)
    )
    for idx, lang in enumerate(lang_info):
        lang_name: str = lang.get('name')
        # >>> add languages to filter here <<<
        # if lang_name in {...}: continue
        lang_time: str = lang.get('text') if wk_i.show_time else ''
        lang_ratio: float = lang.get('percent')
        lang_bar: str = make_graph(
            wk_i.block_style, lang_ratio, wk_c.graph_length,
            lg_nm=lang_name
        )
        contents += (
            f'{lang_name.ljust(pad_len)}   ' +
            f'{lang_time: <16}{lang_bar}   ' +
            f'{lang_ratio:.2f}'.zfill(5) + ' %\n'
        )
        if idx >= 5 or lang_name == 'Other':
            break

    logger.debug('Contents were made\n')
    return contents.rstrip('\n')


def fetch_stats() -> Any:
    """
    WakaReadme Fetch Stats
    ----------------------

    Returns statistics as JSON string
    """
    attempts, statistic = 4, {}
    encoded_key: str = str(b64encode(bytes(wk_i.waka_key, 'utf-8')), 'utf-8')
    logger.debug(
        f'Pulling WakaTime stats from {" ".join(wk_i.time_range.split("_"))}'
    )

    while attempts > 0:
        resp_message, fake_ua = None, cryptogenic.choice(
            [str(fake.user_agent()) for _ in range(5)]
        )
        # making a request
        if (resp := rq_get(
            url=f'{wk_i.api_base_url.rstrip("/")}/v1/users/current/stats/{wk_i.time_range}',
            headers={
                'Authorization': f'Basic {encoded_key}',
                'User-Agent': fake_ua,
            },
        )).status_code != 200:
            resp_message = f'• {resp.json().get("message")}'
        logger.debug(
            f'API response #{5 - attempts}: {resp.status_code} • {resp.reason} {resp_message or ""}'
        )
        if resp.status_code == 200 and (statistic := resp.json()):
            logger.debug('Fetched WakaTime statistics')
            break
        logger.debug(f'Retrying in {30 * (5 - attempts )}s ...')
        sleep(30 * (5 - attempts))
        attempts -= 1

    if err := (statistic.get('error') or statistic.get('errors')):
        logger.error(err)
        sys.exit(1)

    print()
    return statistic.get('data')


def churn(old_readme: str, /) -> str | None:
    """
    WakaReadme Churn
    ----------------

    Composes WakaTime stats within markdown code snippet
    """
    # getting content
    if not (waka_stats := fetch_stats()):
        logger.error('Unable to fetch data, please rerun workflow')
        sys.exit(1)

    # processing content
    generated_content = prep_content(waka_stats)
    print(generated_content, '\n', sep='')
    new_readme = re.sub(
        pattern=wk_c.waka_block_pattern,
        repl=f'{wk_c.start_comment}\n\n```text\n{generated_content}\n```\n\n{wk_c.end_comment}',
        string=old_readme
    )
    if len(sys.argv) == 2 and sys.argv[1] == '--dev':
        logger.debug('Detected run in `dev` mode.')
        # to avoid accidentally writing back to Github
        # when developing and testing WakaReadme
        return None
    return None if new_readme == old_readme else new_readme


def genesis() -> None:
    """Run Program"""
    logger.debug('Connecting to GitHub')
    gh_connect = Github(wk_i.gh_token)
    gh_repo = gh_connect.get_repo(wk_i.repository)
    readme_file = gh_repo.get_readme()
    logger.debug('Decoding readme contents\n')
    readme_contents = str(readme_file.decoded_content, encoding='utf-8')
    if new_content := churn(readme_contents):
        logger.debug('WakaReadme stats has changed')
        gh_repo.update_file(
            path=readme_file.path,
            message=wk_i.commit_message,
            content=new_content,
            sha=readme_file.sha
        )
        logger.info('Stats updated successfully')
        return
    logger.info('WakaReadme was not updated')


################### driver ###################
print()
# hush existing loggers
# pylint: disable = no-member # see: https://stackoverflow.com/q/20965287
for lgr_name in logger.root.manager.loggerDict:
    # to disable log propagation completely set '.propagate = False'
    logger.getLogger(lgr_name).setLevel(logger.WARNING)
# pylint: enable = no-member
# somehow github.Requester gets missed out from loggerDict
logger.getLogger('github.Requester').setLevel(logger.WARNING)
# configure logger
logger.basicConfig(
    datefmt='%Y-%m-%d %H:%M:%S',
    format='[%(asctime)s] ln. %(lineno)-3d %(levelname)-8s %(message)s',
    level=logger.DEBUG
)
try:
    if len(sys.argv) == 2 and sys.argv[1] == '--dev':
        # get env-vars from .env file for development
        from dotenv import load_dotenv
        # comment this out to disable colored logging
        from loguru import logger
        load_dotenv()
except ImportError as im_err:
    logger.warning(im_err)


if __name__ == '__main__':
    # faker data preparation
    fake = Faker()
    Faker.seed(0)
    cryptogenic = SystemRandom()

    # initial waka-readme setup
    logger.debug('Initialize WakaReadme')
    wk_c = WakaConstants()
    wk_i = WakaInput()
    if not wk_i.validate_input():
        logger.error('Environment variables are misconfigured')
        sys.exit(1)
    logger.debug('Input validation complete')

    # run
    try:
        genesis()
    except KeyboardInterrupt:
        print()
        logger.error('Interrupt signal received')
        sys.exit(1)
    except (GithubException, RequestException) as rq_exp:
        logger.critical(rq_exp)
        sys.exit(1)
    print('\nThanks for using WakaReadme!')
