import git
from GitPyCloneProgress import GitPyCloneProgressC
import time
from IdUtil import basicUqIdF
from DirUtil import dirIsEmptyExcludeHidden,rmDirRecurse
from RandomUtil import randSecs
from SleepUtil import sleepVerbose
from rich.progress import Progress

from global_var import GlbVar,getGlbVarInst
def loop_clone_wait_F(repoUrl:str)->git.Repo:
    while True:
        try:
            progressTitle=f"【loop_clone_wait_F,{repoUrl}】"
            dir=f"/tmp/loop_clone_wait_F_{basicUqIdF()}"
            repo:git.Repo=git.Repo.clone_from(url=repoUrl,to_path=dir,  progress=GitPyCloneProgressC(progressTitle,getGlbVarInst().richPrgrs))
            if dirIsEmptyExcludeHidden(dir): #克隆到的是空仓库。 gitee 导入仓库逻辑， 收到请求后 立即创建一个空仓库，然后跑任务慢慢塞
                sleepVerbose( randSecs(5) ,"以克隆代检测")
                rmDirRecurse(dir)
                print(".",end="")#等待中
                continue
            else:
                #正常克隆仓库
                return repo
        except git.GitCommandError as e:#克隆仓库报错
            sleepVerbose( randSecs(5) ,"以克隆代检测_")
        rmDirRecurse(dir)
        print("x",end="")
