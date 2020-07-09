# Dev Metrics in Readme

[Wakatime](https://wakatime.com) Weekly Metrics on your Profile Readme

## Update your Readme

Add a comment to your README like the follows

```md
<!--START_SECTION:waka-->
<!--END_SECTION:waka-->
```

The lines will be our entrypoints for our metrics.

## How to get it

- Clone the Repo
- Install the dependencies `pip install -r requirements.txt`
- Get a GitHub Access Token with a `repo` scope.
- Get your Wakatime API Key.
- Load env vars like
  
  ```text
  GH_TOKEN = <ghtoken>
  WAKATIME_API_KEY = <your wakatime API Key>
  USERNAME = <github_username>
  ```

- Run the Script with `python main.py`
