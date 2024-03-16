from pathlib import Path
import shutil

def dirIsEmptyExcludeHidden(dir:str)->bool:
    ls=list(Path(dir).glob("[!.]*"))
    has:bool = (ls is not None and len(ls)>0)
    return not has

def rmDirRecurse(dir:str):
    shutil.rmtree(path=dir,ignore_errors=True)