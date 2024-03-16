from pathlib import Path

def dirIsEmptyExcludeHidden(dir:str)->bool:
    ls=list(Path(dir).glob("[!.]*"))
    has:bool = (ls is not None and len(ls)>0)
    return not has