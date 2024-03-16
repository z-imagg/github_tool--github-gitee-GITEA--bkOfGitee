import git
from GitPyCloneProgress import GitPyCloneProgressC
import time
from IdUtil import basicUqIdF
from DirUtil import dirIsEmptyExcludeHidden
def loop_clone_wait_F(repoUrl:str)->git.Repo:
    dir=f"/tmp/{basicUqIdF()}"
    while True:
        try:
            repo:git.Repo=git.Repo.clone_from(url=repoUrl,to_path=dir,  progress=GitPyCloneProgressC())
            if dirIsEmptyExcludeHidden(dir): #克隆到的是空仓库。 gitee 导入仓库逻辑， 收到请求后 立即创建一个空仓库，然后跑任务慢慢塞
                time.sleep(2)
                print(".",end="")#等待中
                continue
            return repo
        except git.GitCommandError as e:#克隆仓库报错
            time.sleep(2)
        print("*",end="")
