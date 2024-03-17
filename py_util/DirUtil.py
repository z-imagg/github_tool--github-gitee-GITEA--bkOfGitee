from pathlib import Path
import shutil

def dirIsEmptyExcludeHidden(dir:str)->bool:
    ls=list(Path(dir).glob("[!.]*"))
    has:bool = (ls is not None and len(ls)>0)
    return not has

def rmDirRecurse(dir:str):
    shutil.rmtree(path=dir,ignore_errors=True)


from pathlib import Path
#设置此脚本所在目录 为 工作目录
def setScriptDirAsCwd()->Path:
    import sys
    import os
    scriptF=sys.argv[0]
    scriptDir:Path=Path(scriptF).parent
    os.chdir(path=scriptDir)
    return scriptDir