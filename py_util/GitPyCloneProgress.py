import git
from git.remote import RemoteProgress
import threading
import typing
import sys

from global_var import getGlbVarInst

class SimpleProgressC:
    def __init__(self,prgrsLen:int,symbol:str) -> None:
        self.curIdx:int=0
        self.prgrsLen:int=prgrsLen
        self.symbol:str=symbol
    def doing():
        pass
class GitPyCloneProgressC(RemoteProgress):
    def __init__(self,prgrsNm:str):
        super().__init__()
        #进度条标题
        self.prgrsNm:str=f"{prgrsNm},GPCPC,"
        self.prgrsLen:int=10
        self.prgrsCurIdx:int=0

    def update(self, op_code:int, cur_count:typing.Union[str, float], max_count:typing.Union[str, float, None]=None, message:str=''):
        rate:float=cur_count/max_count
        prgrsCurIdx:int=int(self.prgrsLen*rate)
        if prgrsCurIdx >= self.prgrsCurIdx:
            print("#",end="")
            sys.stdout.flush()
            self.prgrsCurIdx+=1

            
        # thrdId=threading.get_ident(); print(f"thrdId@prgs={thrdId}")
        #gitpython独自拥有多个线程，因为走到这里多了多个线程


# repo = git.Repo.clone_from(url="git@gitee/xx/xx.git", to_path="xx/xx/xx", progress=GitPyCloneProgressC())
