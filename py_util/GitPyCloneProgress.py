import git
from rich import print
from rich.progress import Progress,TaskID
import threading

from global_var import getGlbVarInst

class GitPyCloneProgressC(git.remote.RemoteProgress):
    def __init__(self,prgrsNm:str):
        super().__init__()
        #进度条标题
        self.prgrsNm:str=f"{prgrsNm},GPCPC,"
        self.task_id=None
        self.cur_opCode:int=None
        print(">")

    def update(self, op_code, cur_count, max_count=None, message=''):
        # print(".",end="")
        richPrgrs=getGlbVarInst().richPrgrs
        if self.cur_opCode is None or self.cur_opCode != op_code:
            self.cur_opCode = op_code
            # if self.task_id is not None:  richPrgrs.update(task_id=self.task_id,visible=False)

            self.task_id=richPrgrs.add_task(description=f"{self.prgrsNm},{self.cur_opCode}",total=max_count)

        # thrdId=threading.get_ident(); print(f"thrdId@prgs={thrdId}")
        #gitpython独自拥有多个线程，因为走到这里多了多个线程
        richPrgrs.update(task_id=self.task_id, advance=cur_count,total=max_count)


          
# repo = git.Repo.clone_from(url="git@gitee/xx/xx.git", to_path="xx/xx/xx", progress=GitPyCloneProgressC())
