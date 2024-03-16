import git
from GitPyCloneProgress import GitPyCloneProgressC
import time
from datetime import datetime
from IdUtil import basicUqIdF
def loop_clone_wait_F(repoUrl:str)->git.Repo:
    dir=f"/tmp/{basicUqIdF()}"
    while True:
        try:
            repo:git.Repo=git.Repo.clone_from(url=repoUrl,to_path=dir,  progress=GitPyCloneProgressC())
            return repo
        except git.GitCommandError as e:
            print(".",end="")
            time.sleep(2)
