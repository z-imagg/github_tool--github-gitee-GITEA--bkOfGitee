#!/usr/bin/env python
# -*- coding: <encoding name> -*-


from pathlib import Path
import git
from git import cmd
import shutil
import re

import sys
# print(sys.argv)
CurScriptNm:str=sys.argv[0]
assert sys.argv[1:].__len__() == 1, "断言错误，参数个数必须等于1. 【用法为】python3 me.py git仓库路径"
_BgRp:str=sys.argv[1]



BgRp:git.Repo=git.Repo(path=_BgRp)
BgRpRmt:git.Remote=BgRp.remote()
originUrlBgRp:str=BgRpRmt.url
BgRp_:cmd.Git=BgRp.git

# BgRp.submodules

sbmKBg:git.Submodule


for k,sbmKBg in enumerate( BgRp.submodules):
    #import_githubRepo_to_gitee.sh --from_repo https://github.com/pytorch/pytorch.git  --goal_org imagg  --goal_repoPath pytorch--pytorch --goal_repoName pytorch--pytorch  --goal_repoDesc 来源https://github.com/pytorch/pytorch.git
    x=f"import_githubRepo_to_gitee.sh --from_repo {sbmKBg.url}  --goal_org imagg  --goal_repoPath pytorch--pytorch --goal_repoName pytorch--pytorch  --goal_repoDesc 来源https://github.com/pytorch/pytorch.git"
    urlMatch=re.match(pattern=r"http[s]?://(.+)/(.+)/(.+)\.git",string=sbmKBg.url)
    if urlMatch is not None:
        host=urlMatch.group(1)
        path=urlMatch.group(2)
        repoName=urlMatch.group(3)
    print(f"{sbmKBg.name}, {sbmKBg.path}, {sbmKBg.url}, {sbmKBg.hexsha}, {sbmKBg.branch_name}, {sbmKBg.branch_path}")

_end=True