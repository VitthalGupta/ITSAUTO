from path import path
from utility.install_package import install
import urllib.request
import json
# check for git is installed
try:
    import git
except ImportError as e:
    print("Installing git")
    install("GitPython")
    import git
# check if requests is installed
try:
    import requests
except ImportError as e:
    print("Installing requests")
    install("requests")
    import requests

# check if packaging is installed
try:
    import packaging
except ImportError as e:
    print("Installing packaging")
    install("packaging")
    import packaging

def update_script():
    print("Fetching updates from GithHub")
    repo = git.Repo(path)
    repo.remotes.origin.pull()
    print("Updates fetched successfully")

# check for new releases
def check_release():
    print("Checking for new releases")
    repo = git.Repo(path)
    # get the latest tag
    latest_tag = repo.tags[-1]
    # get the current tag
    current_tag = repo.git.describe('--tags')
    if latest_tag == current_tag:
        print("No new releases")
    else:
        print("New release found")
        print("Do you wish to update (Y/n)")
        update = input()
        if update == "Y" or update == "y":
            update_script()
        else:
            print("Update skipped")