import git
from path import path

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