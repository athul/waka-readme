<center>

![waka-readme](https://socialify.git.ci/athul/waka-readme/image?description=1&forks=1&name=1&pulls=1&stargazers=1&theme=Light)

</center>

# Dev Metrics in Readme [![Unit Tests](https://github.com/athul/waka-readme/actions/workflows/testing.yml/badge.svg?branch=master)](https://github.com/athul/waka-readme/actions/workflows/testing.yml) ![Python Version](https://img.shields.io/badge/Python-^3.11-blue)

[WakaTime](https://wakatime.com) weekly metrics on your profile readme.

![Project Preview](https://user-images.githubusercontent.com/8397274/87243943-e6b45c00-c457-11ea-94c9-2aa0bf241be8.png)

:speech_balloon: **Forum** | [GitHub discussions][gh_discuss]

## New to WakaTime?

> Nope? Skip to [prep work](#prep-work).

WakaTime gives you an idea of the time you spent on coding. This helps you boost your productivity and competitive edge.

1. Head over to <https://wakatime.com/> and create an account.
2. After logging in get your WakaTime API Key from <https://wakatime.com/api-key/>.
3. Install [WakaTime plugin][waka_plugins] in your favorite editor / IDE.
4. Paste in your API key to start telemetry.

:information_source: **Info** | You can read [WakaTime help][waka_help] to know more about configurations.
Alternatively, you can also fetch data from WakaTime compatible services like [Wakapi][wakapi] or [Hakatime][hakatime].

## Prep Work

A GitHub repository and a `README.md` file is required. We'll be making use of readme in the [profile repository][profile_readme].

- Save the `README.md` file after copy-pasting the following special comments. Your dev-metics will show up in between.

  ```md
  <!--START_SECTION:waka-->
  <!--END_SECTION:waka-->
  ```

  `<!--START_SECTION: -->` and `<!--END_SECTION: -->` are placeholders and must be retained as is. Whereas "`waka`" can be replaced by any alphanumeric string. See [#Tweaks](#tweaks) section for more.

- Navigate to your repo's `Settings > Secrets` and add a new secret _named_ `WAKATIME_API_KEY` with your API key as it's _value_.

  > Or use the url <https://github.com/USERNAME/USERNAME/settings/secrets/actions/new> by replacing the `USERNAME` with your own username.
  >
  > ![new_secrets_actions][new_secrets_actions]

  - If you're not using [profile repository][profile_readme], add another secret _named_ `GH_TOKEN` and insert your [GitHub token][gh_access_token]\* in place of _value_.

- Create a new workflow file (`waka-readme.yml`) inside `.github/workflows/` folder of your repository. You can create it from a template using the _actions tab_ of your repository too.
- Clear any existing contents, add the following lines and save the `waka-readme.yml` workflow file.

  ```yml
  name: Waka Readme

  on:
    workflow_dispatch: # for manual workflow trigger
    schedule:
      - cron: "0 0 * * *" # runs at every 12AM UTC

  jobs:
    update-readme:
      name: WakaReadme DevMetrics
      runs-on: ubuntu-latest
      steps:
        - uses: athul/waka-readme@master
          with:
            WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
            # following flags are required, only if this is not on
            # profile readme, remove the leading `#` to use them
            #GH_TOKEN: ${{ secrets.GH_TOKEN }}
            #REPOSITORY: <gh_username/gh_username>
  ```

  Refer [#Example](#example) section for a full blown workflow file.

## Tweaks

There are many flags that you can tweak as you wish!

### Meta Tweaks

| Environment flag | Options (`Default`, `Other`, ...)                                                        | Description                                                                   |
| ---------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `API_BASE_URL`   | `https://wakatime.com/api`, `https://wakapi.dev/api`, `https://hakatime.mtx-dev.xyz/api` | Use WakaTime compatible services like [Wakapi][wakapi] & [Hakatime][hakatime] |
| `REPOSITORY`     | `<gh_username>/<gh_username>`, `<gh_username>/<repo_name>`                               | Waka-readme stats will appear on the provided repository                      |

### Content Tweaks

| Environment flag   | Options (`Default`, `Other`, ...)                                       | Description                                                                       |
| ------------------ | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `SHOW_TITLE`       | `false`, `true`                                                         | Add title to waka-readme stats blob                                               |
| `SECTION_NAME`     | `waka`, any alphanumeric string                                         | The generator will look for section name to fill up the readme.                   |
| `BLOCKS`           | `░▒▓█`, `⣀⣄⣤⣦⣶⣷⣿`, `-#`, `=>`, you can be creative                      | Ascii art used to build stats graph                                               |
| `CODE_LANG`        | `txt`, `python` `ruby` `json` , you can use other languages also        | Language syntax based highlighted text                                            |
| `TIME_RANGE`       | `last_7_days`, `last_30_days`, `last_6_months`, `last_year`, `all_time` | String representing a dispensation from which stats are aggregated                |
| `LANG_COUNT`       | `5`, any plausible number                                               | Number of languages to be displayed                                               |
| `SHOW_TIME`        | `true`, `false`                                                         | Displays the amount of time spent for each language                               |
| `SHOW_TOTAL`       | `false`, `true`                                                         | Show total coding time                                                            |
| `SHOW_MASKED_TIME` | `false`, `true`                                                         | Adds total coding time including unclassified languages (overrides: `SHOW_TOTAL`) |
| `STOP_AT_OTHER`    | `false`, `true`                                                         | Stop when language marked as `Other` is retrieved (overrides: `LANG_COUNT`)       |

### Commit Tweaks

| Environment flag  | Options (`Default`, `Other`, ...)                                    |
| ----------------- | -------------------------------------------------------------------- |
| `COMMIT_MESSAGE`  | `Updated waka-readme graph with new metrics`, any reasonable message |
| `TARGET_BRANCH`   | `NOT_SET`, target branch name                                        |
| `TARGET_PATH`     | `NOT_SET`, `/path/to/target/file`                                    |
| `COMMITTER_NAME`  | `NOT_SET`, committer name                                            |
| `COMMITTER_EMAIL` | `NOT_SET`, committer email                                           |
| `AUTHOR_NAME`     | `NOT_SET`, author name                                               |
| `AUTHOR_EMAIL`    | `NOT_SET`, author email                                              |

All of these flags are _optional_.

# Example

**`waka-readme.yml`**

```yml
name: Waka Readme

on:
  workflow_dispatch:
  schedule:
    # Runs at 12am UTC
    - cron: "0 0 * * *"

jobs:
  update-readme:
    name: WakaReadme DevMetrics
    runs-on: ubuntu-latest
    steps:
      - uses: athul/waka-readme@master
        with:
          GH_TOKEN: ${{ secrets.GH_TOKEN }}
          WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
          # meta
          API_BASE_URL: https://wakatime.com/api
          REPOSITORY: athul/athul
          # content
          SHOW_TITLE: true
          SECTION_NAME: waka
          BLOCKS: ->
          CODE_LANG: all_time 
          TIME_RANGE: true
          LANG_COUNT: 10
          SHOW_TIME: true
          SHOW_TOTAL: true
          SHOW_MASKED_TIME: false
          STOP_AT_OTHER: true
          # commit
          COMMIT_MESSAGE: Updated waka-readme graph with new metrics
          TARGET_BRANCH: master
          TARGET_PATH: README.md
          COMMITTER_NAME: GitHubActionBot
          COMMITTER_EMAIL: action-bot@github.org
          AUTHOR_NAME: Athul
          AUTHOR_EMAIL: athul@example.org
          # you can populate email-id with secretes instead
```

> Note:
>
> - Flags `REPOSITORY` and `GH_TOKEN` are required, ONLY if you're NOT using [profile readme][profile_readme].
> - `WAKATIME_API_KEY` is a required secret.
> - Every other environment variables is optional.
> - The above example does not show proper default values, refer [#Tweaks](#tweaks) for the same.

**`README.md`**

```md
From: 10 July 2020 - To: 06 August 2022

Total Time: 1,464 hrs 54 mins

Python             859 hrs 29 mins >>>>>>>>>>>>>>-----------   54.68 %
Markdown           132 hrs 33 mins >>-----------------------   08.43 %
TeX                103 hrs 52 mins >>-----------------------   06.61 %
HTML               94 hrs 48 mins  >>-----------------------   06.03 %
Nim                64 hrs 31 mins  >------------------------   04.11 %
Other              47 hrs 58 mins  >------------------------   03.05 %
```

## Why only the language stats (and not other data) from the API?

I am a fan of minimal designs and the profile readme is a great way to show off your skills and interests. The WakaTime API, gets us a **lot of data** about a person's **coding activity including the editors and Operating Systems you used and the projects you worked on**. Some of these projects maybe secretive and should not be shown out to the public. Using up more data via the Wakatime API will clutter the profile readme and hinder your chances on displaying what you provide **value to the community** like the pinned Repositories. I believe that **Coding Stats is nerdiest of all** since you can tell the community that you are **_exercising these languages or learning a new language_**, this will also show that you spend some amount of time to learn and exercise your development skills. That's what matters in the end :heart:

[//]: #(Links)
[wakapi]: https://wakapi.dev
[hakatime]: https://github.com/mujx/hakatime
[waka_plugins]: https://wakatime.com/plugins
[waka_help]: https://wakatime.com/help/editors
[profile_readme]: https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme
[new_secrets_actions]: https://user-images.githubusercontent.com/52720626/151221742-bc37d139-2bb3-4554-b27c-46b107d1f408.png
[gh_access_token]: https://docs.github.com/en/actions/configuring-and-managing-workflows/authenticating-with-the-github_token
[gh_discuss]: https://github.com/athul/waka-readme/discussions
