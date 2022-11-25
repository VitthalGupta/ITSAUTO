import git
from path import path

def update_script():
    print("Fetching updates from GithHub")
    repo = git.Repo(path)
    repo.remotes.origin.pull()
    print("Updates fetched successfully")