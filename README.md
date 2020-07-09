# Dev Metrics in Readme

[Wakatime](https://wakatime.com) Weekly Metrics on your Profile Readme

## How to get it
**You Need to Have [waka-box](https://github.com/matchai/waka-box) in your Repo**
> *This maybe temporary and will be updated soon as  I'll update this to an Action*

- Clone the Repo
- Install the dependencies `pip install -r requirements.txt`
- Get a GitHub Access Token with a `repo` scope
- Load env vars like
  
  ```text
  GH_TOKEN = <ghtoken>
  GIST_ID = <gist_id of the waka-box gist>
  USERNAME = <github_username>
  ```

- Run the Script with `python main.py`
