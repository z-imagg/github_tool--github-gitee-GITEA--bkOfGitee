import git
from rich import print
from rich.progress import Progress,TaskID

from global_var import getGlbVarInst

class GitPyCloneProgressC(git.remote.RemoteProgress):
    def __init__(self,prgrsNm:str):
        super().__init__()
        #进度条标题
        self.prgrsNm:str=f"{prgrsNm},GPCPC,"
        self.task_id:TaskID=None

    def update(self, op_code, cur_count, max_count=None, message=''):
        # print(".",end="")
        if self.task_id is None:
            self.task_id=getGlbVarInst().richPrgrs.add_task(description=self.prgrsNm, total=max_count)
        getGlbVarInst().richPrgrs.update(task_id=self.task_id, advance=cur_count)


          
# repo = git.Repo.clone_from(url="git@gitee/xx/xx.git", to_path="xx/xx/xx", progress=GitPyCloneProgressC())
