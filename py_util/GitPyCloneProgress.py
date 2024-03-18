import git
import threading

from global_var import getGlbVarInst

class GitPyCloneProgressC(git.remote.RemoteProgress):
    def __init__(self,prgrsNm:str):
        super().__init__()
        #进度条标题
        self.prgrsNm:str=f"{prgrsNm},GPCPC,"

    def update(self, op_code, cur_count, max_count=None, message=''):
        print("#",end="")
        # thrdId=threading.get_ident(); print(f"thrdId@prgs={thrdId}")
        #gitpython独自拥有多个线程，因为走到这里多了多个线程


# repo = git.Repo.clone_from(url="git@gitee/xx/xx.git", to_path="xx/xx/xx", progress=GitPyCloneProgressC())
