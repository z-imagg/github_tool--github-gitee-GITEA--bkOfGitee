#!/usr/bin/env python
# -*- coding: <encoding name> -*-


from pathlib import Path
import git
from git import cmd
import shutil

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
    print(f"{sbmKBg.name}, {sbmKBg.path}, {sbmKBg.url}, {sbmKBg.hexsha}, {sbmKBg.branch_name}, {sbmKBg.branch_path}")

_end=True