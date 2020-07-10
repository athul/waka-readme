import base64
import requests
import re
import os
from github import Github

START_COMMENT = '<!--START_SECTION:waka-->'
END_COMMENT = '<!--END_SECTION:waka-->'
listReg = f'{START_COMMENT}[\\s\\S]+{END_COMMENT}'

user = os.getenv("INPUT_USERNAME")
waka_key = os.getenv("INPUT_WAKATIME_API_KEY")
ghtoken = os.getenv("INPUT_GH_TOKEN")


def makeGraph(percent: float):
    done_block = "█"
    empty_block = "░"
    pc_rnd = round(percent)
    return (f'{done_block*int(pc_rnd/4)}{empty_block*int( 25-int(pc_rnd/4))}')


def getStats():
    data = requests.get(
        f"https://wakatime.com/api/v1/users/current/stats/last_7_days?api_key={waka_key}").json()
    lang_data = data['data']['languages']
    data_list = []
    for l in lang_data[:5]:
        ln = len(l['name'])
        ln_text = len(l['text'])
        op = f"{l['name']}{' '*(12-ln)}{l['text']}{' '*(20-ln_text)}{makeGraph(l['percent'])}   {l['percent']}"
        data_list.append(op)
    data = " \n".join(data_list)
    return ("```text\n"+data+"\n```")


def decodeReadme(data: str):
    decodedBytes = base64.b64decode(data)
    decodedStr = str(decodedBytes, "utf-8")
    return decodedStr


def generatenewReadme(stats: str, readme: str):
    statsinReadme = f"{START_COMMENT}\n{stats}\n{END_COMMENT}"
    newReadme = re.sub(listReg, statsinReadme, readme)
    return newReadme


if __name__ == '__main__':
    g = Github(ghtoken)
    repo = g.get_repo(f"{user}/{user}")
    contents = repo.get_readme()
    stats = getStats()
    rdmd = decodeReadme(contents.content)
    newreadme = generatenewReadme(stats=stats, readme=rdmd)
    if newreadme != rdmd:
        repo.update_file(path=contents.path, message="Updated with Dev Metrics",
                     content=newreadme, sha=contents.sha, branch="master")
