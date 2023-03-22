import os
from git import Repo
from dotenv import load_dotenv
load_dotenv()

repoLocation = os.getenv('PATH_OF_GIT_REPO')

def git_push(COMMIT_MESSAGE):
    try:
        repo = Repo(repoLocation)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    

