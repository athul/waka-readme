import base64
import requests
import re
import os
from github import Github

START_COMMENT = '<!--START_SECTION:waka-->'
END_COMMENT = '<!--END_SECTION:waka-->'
listReg = f'{START_COMMENT}[\\s\\S]+{END_COMMENT}'

user = os.getenv("USERNAME")
gistid = os.getenv("GIST_ID")
ghtoken = os.getenv("GH_TOKEN")

def getStats():
    data = requests.get(f"https://gist.githubusercontent.com/{user}/{gistid}/raw/").text
    return ("```text\n"+data+"\n```")
    
def decodeReadme(data:str):
    decodedBytes = base64.b64decode(data)
    decodedStr = str(decodedBytes, "utf-8")
    return decodedStr

def generatenewReadme(stats:str,readme:str):
    statsinReadme = f"{START_COMMENT}\n{stats}\n{END_COMMENT}"
    newReadme = re.sub(listReg,statsinReadme,readme)
    return newReadme

if __name__ == '__main__':
    g = Github(ghtoken)
    repo = g.get_repo(f"{user}/{user}")
    contents = repo.get_readme()
    stats = getStats()
    rdmd = decodeReadme(contents.content)
    newreadme = generatenewReadme(stats=stats,readme=rdmd)
    repo.update_file(path=contents.path,message="Updated with Dev Metrics",content=newreadme,sha=contents.sha,branch="master")