import git
from git.remote import RemoteProgress
import threading
import typing

from progress.counter import Countdown , Counter
from progress.bar import Bar
from progress.spinner import LineSpinner

from global_var import getGlbVarInst

class GitPyCloneProgressC(RemoteProgress):
    def __init__(self,prgrsNm:str):
        super().__init__()
        #进度条标题
        self.prgrsNm:str=f"{prgrsNm},ClnProg"
        self.cur_gitOpCode:int=None
        self.gitOpCodeLs:typing.List[int]=[]
        print(">")
        self.prgrsBar:Bar=None
        self.opCodeLsTxt:str=None

    def update(self, gitOpCode:int, cur_count:typing.Union[str, float], max_count:typing.Union[str, float, None]=None, message:str=''):
        print("#",end="")
        
        #保存有史以来的所有git操作码， gitOpCode按照来的时刻保持顺序
        if gitOpCode not in self.gitOpCodeLs:
            self.gitOpCodeLs.append(gitOpCode)
        
        #若 来了第一个git操作码 或 git操作码 变化了
        if self.cur_gitOpCode is None or self.cur_gitOpCode != gitOpCode:
            # 更新 当前git操作码
            self.cur_gitOpCode = gitOpCode

            # 新建进度条
            #    参考 https://github.com/verigak/progress/
            self.prgrsBar:Bar=Bar(f"{self.prgrsNm},gitOpCd【{gitOpCode}】", max=max_count,fill="!", suffix="【%(percent)d％;%(index)d;%(max)d】")

        self.opCodeLsTxt:str=">".join([f"{k}" for k in self.gitOpCodeLs])

        # 进度条 创建后 不能直接修改标题，否则 完全乱套了
        # self.countDown.message=f"{self.countDown.message},{opCodeLsTxt}"
          
        #更新当前进度条
        self.prgrsBar.goto(cur_count)

        #数字到达的时候，进度条调用finish方法 以 结束，否则不换行
        if cur_count == max_count: self.prgrsBar.finish()


# repo = git.Repo.clone_from(url="git@gitee/xx/xx.git", to_path="xx/xx/xx", progress=GitPyCloneProgressC())
