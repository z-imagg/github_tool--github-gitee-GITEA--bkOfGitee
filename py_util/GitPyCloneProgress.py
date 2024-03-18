import git
from git.remote import RemoteProgress
from rich import print
from rich.progress import Progress,TaskID
import threading
import typing

from global_var import getGlbVarInst

class GitPyCloneProgressC(RemoteProgress):
    def __init__(self,prgrsNm:str):
        super().__init__()
        #进度条标题
        self.prgrsNm:str=f"{prgrsNm},GPCPC,"
        self.task_id=None
        self.cur_gitOpCode:int=None
        self.gitOpCodeLs:typing.Set[int]=set()
        print(">")

    def update(self, gitOpCode:int, cur_count:typing.Union[str, float], max_count:typing.Union[str, float, None]=None, message:str=''):
        # print(".",end="")
        self.gitOpCodeLs.add(gitOpCode)
        opCodeLsTxt:str="、".join([f"{k}" for k in self.gitOpCodeLs])
        richPrgrs=getGlbVarInst().richPrgrs
        if self.cur_gitOpCode is None or self.cur_gitOpCode != gitOpCode:
            self.cur_gitOpCode = gitOpCode
            if self.task_id is not None:  richPrgrs.update(task_id=self.task_id,visible=False)

            self.task_id=richPrgrs.add_task(description=f"{self.prgrsNm},{opCodeLsTxt}",total=max_count)

        # thrdId=threading.get_ident(); print(f"thrdId@prgs={thrdId}")
        #gitpython独自拥有多个线程，因为走到这里多了多个线程
        richPrgrs.update(task_id=self.task_id, advance=cur_count,total=max_count)


          
# repo = git.Repo.clone_from(url="git@gitee/xx/xx.git", to_path="xx/xx/xx", progress=GitPyCloneProgressC())
