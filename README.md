<center>

![waka-readme](https://socialify.git.ci/athul/waka-readme/image?description=1&forks=1&name=1&pulls=1&stargazers=1&theme=Light)

</center>

# Dev Metrics in Readme [![Unit Tests](https://github.com/athul/waka-readme/actions/workflows/testing.yml/badge.svg?branch=master)](https://github.com/athul/waka-readme/actions/workflows/testing.yml) ![Python Version](https://img.shields.io/badge/python-v3.11-blue)

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

A GitHub repository and a `README.md` file is required. We'll be making use of readme in the [profile repository][profile_readme]\*.

- Save the `README.md` file after copy-pasting the following special comments. Your dev-metics will show up in between.

  ```md
  <!--START_SECTION:waka-->
  <!--END_SECTION:waka-->
  ```

  "`waka`" can be replaced by any alphanumeric string with the `SECTION_NAME` environment variable. See the [#tweaks](#tweaks) section for more.

- Navigate to your repo's `Settings > Secrets` and add a new secret _named_ `WAKATIME_API_KEY` with your API key as it's _value_.

  > Or use the url <https://github.com/USERNAME/USERNAME/settings/secrets/actions/new> by replacing the `USERNAME` with your own username.
  >
  > ![new_secrets_actions][new_secrets_actions]

  - If you're not using [profile repository][profile_readme], add another secret _named_ `GH_TOKEN` and insert your [GitHub token][gh_access_token]\* in place of _value_.

- Create a new workflow file (`waka-readme.yml`) inside `.github/workflows/` folder of your repository. You can create it from a template using the _actions tab_ of your repository too.
- Clear any existing contents, add the following lines and save the file.

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

## Tweaks

There are many flags that you can tweak to suit your taste!

| Flag               | Default                                      | Options                                                                                  | Meaning                                                                                                 |
| ------------------ | -------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `API_BASE_URL`     | `https://wakatime.com/api`                   | `https://wakatime.com/api`, `https://wakapi.dev/api`, `https://hakatime.mtx-dev.xyz/api` | Integration with WakaTime compatible services like [Wakapi][wakapi] & [Hakatime][hakatime] are possible |
| `REPOSITORY`       | `<gh_username>/<gh_username>`                | `<gh_username>/<repo_name>`                                                              | Waka-readme stats will appear on the provided repository                                                |
| `SECTION_NAME`     | `waka`                                       | Any alphanumeric string                                                                  | The generator will look for this section to fill up the readme.                                         |
| `COMMIT_MESSAGE`   | `Updated waka-readme graph with new metrics` | Any string                                                                               | Messaged used when committing updated stats                                                             |
| `SHOW_TITLE`       | `false`                                      | `false`, `true`                                                                          | Add title to waka-readme stats blob                                                                     |
| `BLOCKS`           | `░▒▓█`                                       | `░▒▓█`, `⣀⣄⣤⣦⣶⣷⣿`, `-#`, you can be creative!                                            | Ascii art used to build stats graph                                                                     |
| `TIME_RANGE`       | `last_7_days`                                | `last_7_days`, `last_30_days`, `last_6_months`, `last_year`, `all_time`                  | String representing a dispensation from which stats are aggregated                                      |
| `SHOW_TIME`        | `true`                                       | `false`, `true`                                                                          | Displays the amount of time spent for each language                                                     |
| `SHOW_TOTAL`       | `false`                                      | `false`, `true`                                                                          | Show total coding time                                                                                  |
| `SHOW_MASKED_TIME` | `false`                                      | `false`, `true`                                                                          | Adds total coding time including unclassified languages (overrides: `SHOW_TOTAL`)                       |
| `LANG_COUNT`       | `5`                                          | Any reasonable number                                                                    | Number of languages to be displayed                                                                     |

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
          WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
          SHOW_TITLE: true
          BLOCKS: ->
          TIME_RANGE: all_time
          SHOW_TIME: true
          SHOW_MASKED_TIME: true
          LANG_COUNT: 10
```

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

---

<sup>\*</sup>`REPOSITORY` flag and `GH_TOKEN` secret are required you're not using profile readme.

[//]: #(Links)
[wakapi]: https://wakapi.dev
[hakatime]: https://github.com/mujx/hakatime
[waka_plugins]: https://wakatime.com/plugins
[waka_help]: https://wakatime.com/help/editors
[profile_readme]: https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme
[new_secrets_actions]: https://user-images.githubusercontent.com/52720626/151221742-bc37d139-2bb3-4554-b27c-46b107d1f408.png
[gh_access_token]: https://docs.github.com/en/actions/configuring-and-managing-workflows/authenticating-with-the-github_token
[gh_discuss]: https://github.com/athul/waka-readme/discussions
