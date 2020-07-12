# Dev Metrics in Readme

[Wakatime](https://wakatime.com) Weekly Metrics on your Profile Readme

## Update your Readme

Add a comment to your README like the follows

```md
<!--START_SECTION:waka-->
<!--END_SECTION:waka-->
```

The lines will be our entrypoints for our metrics.

## Using it

- Get your Wakatime API Key from your [Account Settings in Wakatime](https://wakatime.com/settings/account) and save it as `WAKATIME_API_KEY = <your wakatime API Key>` in your Repository Secrets

That's it. The Action runs everyday at 00.00 UTC

### Profile Repository

If you're executing the workflow on your Profile Repository (`<username>/<username>`)

**You wouldn't need an GitHub Access Token since GitHub Actions already makes one for you.**

Here is a sample workflow file for you to get started,

```yml
name: Waka Readme

on:
  schedule:
    # Runs at 12am UTC
    - cron: '0 0 * * *'

jobs:
  update-readme:
    name: Update this repo's README
    runs-on: ubuntu-latest
    steps:
      - uses: athul/waka-readme@master
        with:
          WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
```

### Different Repository than Profile Repository

if you're executing the workflow on another repo other than `<username>/<username>`

- You'll need to get a GitHub Access Token with a `repo` scope and save it in the Repo Secrets `GH_TOKEN = <Your GitHub Access Token>`

Here is Sample Worflow File for running it

```yml
name: Waka Readme

on:
  schedule:
    # Runs at 12am UTC
    - cron: '0 0 * * *'

jobs:
  update-readme:
    name: Update Readme with Metrics
    runs-on: ubuntu-latest
    steps:
      - uses: athul/waka-readme@master
        with:
          WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
          GH_TOKEN: ${{ secrets.GH_TOKEN}}
          USERNAME: <username> # optional, it will automaticially use the username that executing the workflow
```
