<center>

![waka-readme](https://socialify.git.ci/athul/waka-readme/image?description=1&forks=1&name=1&pulls=1&stargazers=1&theme=Light)

</center>

# Dev Metrics in Readme [![Build Status](https://travis-ci.com/athul/waka-readme.svg?branch=master)](https://travis-ci.com/athul/waka-readme)

![Project Preview](https://user-images.githubusercontent.com/8397274/87243943-e6b45c00-c457-11ea-94c9-2aa0bf241be8.png)

[WakaTime](https://wakatime.com) Weekly Metrics on your Profile Readme:

**Forum**: [GitHub Discussions](https://github.com/athul/waka-readme/discussions)

## Prep Work

1. You need to update a markdown file (`.md`) with 2 special comments. You can refer [this](#update-your-readme) to update it.
2. You'll need a WakaTime API Key, which you can get from your WakaTime Account Settings. Click [here](#new-to-wakatime), if you're new to WakaTime.
3. **Optionally** you might need a GitHub API Token with `repo` scope, generated from [here](https://github.com/settings/tokens), if you're running this 'action' on any repo other than your [profile repository](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme). Then go to [this](#other-repository-not-profile) example to work it out.
4. You need to save the WakaTime API Key (and the GitHub API Token, if you need it) in the repository secrets. You can find that in your repository settings. Be sure to save those as the following.
   - WakaTime-api-key as `WAKATIME_API_KEY = <your wakatime API Key>` and
   - The GitHub Access Token as `GH_TOKEN=<your github access token>`
5. You can follow either of the Two Examples according to your needs to get started with.

> I strongly suggest you to run the 'Action' in your Profile Repo since you won't be needing a GitHub Access Token

This Action will run everyday at 00:00 UTC.

## Update your Readme

Add comments to your `README.md` like this:

```md
<!--START_SECTION:waka-->
<!--END_SECTION:waka-->
```

These lines will be the entry-points for dev metrics.

## New to WakaTime?

WakaTime gives you an idea of the time you spent on coding. This helps you boost your productivity and competitive edge.

- Head over to <https://wakatime.com> and create an account.
- Get your WakaTime API Key from your [Account Settings in WakaTime](https://wakatime.com/settings/account).
- Install the [WakaTime plugin](https://wakatime.com/plugins) in your favourite editor / IDE.
- Paste in your API key to start the analysis.

Alternatively, you can also choose to fetch data from third-party WakaTime-compatible services like [Wakapi](https://wakapi.dev) or [Hakatime](https://github.com/mujx/hakatime) instead. For details, see [extras](#extras) section below.

## Profile Repository

_If you're executing the workflow on your Profile Repository (`<username>/<username>`)_

Please follow the steps below:

1. Go to your `<username>/<username>/actions`, hit `New workflow` and `set up a workflow yourself`, then delete all the default content.
2. Copy the following code and paste it to your new workflow file you just created and save/commit it as `wakatime.yml`.

   ```yml
   name: Waka Readme

   on:
     workflow_dispatch:
     schedule:
       # Runs at every 12AM UTC
       - cron: "0 0 * * *"

   jobs:
     update-readme:
       name: Update this repo's README
       runs-on: ubuntu-latest
       steps:
         - uses: athul/waka-readme@master
           with:
             WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
   ```

3. Go to your repo secrets by hitting `Settings > Secrets`. You can also enter the url <https://github.com/USERNAME/USERNAME/settings/secrets/actions/new> . Please replace the `USERNAME` with your own username.
4. Create a new Secret. `Name: WAKATIME_API_KEY` and `Value:` Paste the Wakatime API key here.

   ![new-secrets-actions](https://user-images.githubusercontent.com/52720626/151221742-bc37d139-2bb3-4554-b27c-46b107d1f408.png)

   If you don't know what the key is, please go to [Wakatime API](https://wakatime.com/api-key) to get your API Key (See [New to WakaTime?](#new-to-wakatime)).

   Add secret.

   ~~5. Go to Action tab, click on `Waka Readme`, and `Run workflow`.~~

5. Go to your profile page. you will be able to see it in 24 hrs.

## Other Repository (not Profile)

_If you're executing the workflow on another repo other than `<username>/<username>`_

You'll need to get a [GitHub Access Token](https://docs.github.com/en/actions/configuring-and-managing-workflows/authenticating-with-the-github_token) with a `repo` scope and save it in the Repo Secrets `GH_TOKEN = <Your GitHub Access Token>`

Here is Sample Workflow File for running it:

```yml
name: Waka Readme

on:
  schedule:
    # Runs at 12am UTC
    - cron: "0 0 * * *"

jobs:
  update-readme:
    name: Update Readme with Metrics
    runs-on: ubuntu-latest
    steps:
      - uses: athul/waka-readme@master
        with:
          WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
          GH_TOKEN: ${{ secrets.GH_TOKEN }}
          REPOSITORY: <username/username> # optional, By default, it will automatically use the repository which is executing the workflow.
```

## Extras

1. As an alternative to official WakaTime, _waka-readme_ also integrates with WakaTime-compatible services like [Wakapi](https://wakapi.dev) and [Hakatime](https://github.com/mujx/hakatime). To use one of these, **adapt the API URL accordingly and use the respective service's API key** instead:

   ```yml
   - uses: athul/waka-readme@master
           with:
             WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
             API_BASE_URL: https://wakapi.dev/api
   ```

2. If you want to add a title for your stats, by setting `SHOW_TITLE: true` (which by default is `false`) in your workflow file like this

   ```yml
   - uses: athul/waka-readme@master
           with:
             WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
             GH_TOKEN: ${{ secrets.GH_TOKEN }}
             SHOW_TITLE: true
   ```

   Here is an example output with `SHOW_TITLE` set to `true`.

   ```text
   From: 12 February, 2022 - To: 19 February, 2022

   Python      8 hrs 52 mins       ███████████████████░░░░░░   75.87 %
   Go          1 hr 15 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   10.79 %
   Markdown    52 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   07.43 %
   Docker      16 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   02.32 %
   YAML        7 mins              ░░░░░░░░░░░░░░░░░░░░░░░░░   01.07 %
   ```

3. You can specify the time range in the parameter (default `last_7_days`):

   ```yml
   - uses: athul/waka-readme@master
         with:
           WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
           TIME_RANGE: last_30_days
   ```

   See [Wakatime API docs](https://wakatime.com/developers#stats) for more possible values.

4. You can specify a commit message to override the default _"Updated the Graph with new Metrics"_. Here is how you do it

   ```yml
   - uses: athul/waka-readme@master
           with:
             WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
             GH_TOKEN: ${{ secrets.GH_TOKEN }}
             COMMIT_MESSAGE: Updated the Readme
   ```

   If no commit message is specified in the `yml` file, it defaults to _"Updated the Graph with new Metrics"_

5. You can change the block characters to match with the style of your readme. By default the one show in the graphs before is used. Here is how you do it.

   ```yml
   - uses: athul/waka-readme@master
           with:
             WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
             BLOCKS: ⣀⣄⣤⣦⣶⣷⣿
   ```

   Requires `BLOCKS` to be of at least 2 characters in length. It will change the graph to something like this:

   ```text
   Python      8 hrs 52 mins       ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⣀⣀⣀⣀⣀   75.87 %
   Go          1 hr 15 mins        ⣿⣿⣦⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀   10.79 %
   Markdown    52 mins             ⣿⣿⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀   07.43 %
   Docker      16 mins             ⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀   02.32 %
   YAML        7 mins              ⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀   01.07 %
   ```

6. If you want to add total time in stats, by setting `SHOW_TOTAL: true` (which by default is `false`) in your workflow file like this:

   ```yml
   - uses: athul/waka-readme@master
           with:
             WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
             GH_TOKEN: ${{ secrets.GH_TOKEN }}
             SHOW_TOTAL: true
   ```

   It will change the graph to something like this:

   ```text
   Total Time: 44 hrs 27 mins

   Python       36 hrs 28 mins  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⣀⣀⣀⣀   80.09 %
   YAML         2 hrs 30 mins   ⣿⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀   05.52 %
   TOML         1 hr 36 mins    ⣷⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀   03.54 %
   Docker       1 hr 11 mins    ⣶⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀   02.61 %
   Other        1 hr 4 mins     ⣶⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀   02.37 %
   ```

7. If you do not like to share how much time you spent on each language, you can add `SHOW_TIME: false` (by default it will be `true`) in your workflow file like so:

   ```yml
       - uses: athul/waka-readme@master
           with:
             WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
             SHOW_TIME: false
   ```

   Here is an example output with `SHOW_TIME` set to `false`.

   ```text
   From: 12 February, 2022 - To: 19 February, 2022

   PHP          ████████████████████▒░░░░░░░░░░░░░░░░░░░░   49.98 %
   Twig         ████▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   11.07 %
   YAML         ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   09.77 %
   JavaScript   ██▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   06.34 %
   Other        ██▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   05.87 %
   ```

8. If your readme file is symlinked or is in another location, you can point to it by adding `README_PATH: <your path here>` (by default it will be the readme in the root directory) in your workflow file like so:

  ```yml
      - uses: athul/waka-readme@master
            with:
              WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
              README_PATH: 'profile-readme/README.md'
  ```

> You can find all the options in [action.yml](action.yml) and a sample workflow [here](https://github.com/athul/athul/blob/master/.github/workflows/update-readme.yml).
>
> Tip 💡: Add `on: workflow_dispatch:` to enable manual runs. [See](https://github.com/joe733/joe733/blob/master/.github/workflows/waka.yml#L4).

## Why only the language stats and not other data from the API?

I am a fan of minimal designs and the profile readme is a great way to show off your skills and interests. The WakaTime API, gets us a **lot of data** about a person's **coding activity including the editors and Operating Systems you used and the projects you worked on**. Some of these projects maybe secretive and should not be shown out to the public. Using up more data via the Wakatime API will clutter the profile readme and hinder your chances on displaying what you provide **value to the community** like the pinned Repositories. I believe that **Coding Stats is nerdiest of all** since you can tell the community that you are _**exercising these languages or learning a new language**_, this will also show that you spend some amount of time to learn and exercise your development skills. That's what matters in the end :heart:
