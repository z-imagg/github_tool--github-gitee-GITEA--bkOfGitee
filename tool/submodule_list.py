#!/usr/bin/env python
# -*- coding: <encoding name> -*-

# 【文件作用】 遍历给定git仓库中的子模块列表， 并打印对应命令import_githubRepo_to_gitee.sh

from pathlib import Path
import git
from git import cmd
import shutil
import re
import random

import sys
# print(sys.argv)
CurScriptNm:str=sys.argv[0]
assert sys.argv[1:].__len__() == 3, "断言错误，参数个数必须等于3. 【用法为】python3 me.py 父git仓库路径 导入命令休眠秒数起点 导入命令休眠秒数增量"
_BgRp:str=sys.argv[1]
_sleepSeconds:str=int(sys.argv[2])
_sleepSecEnd:str=int(sys.argv[3])

assert _sleepSeconds >=8 and _sleepSecEnd >= 5

BgRp:git.Repo=git.Repo(path=_BgRp)
BgRpRmt:git.Remote=BgRp.remote()
originUrlBgRp:str=BgRpRmt.url
# BgRp_:cmd.Git=BgRp.git

repoK:git.Submodule
giteeMirrorOrgName="imagg"
#                    //host/org /repo
urlReExpr=r"http[s]?://(.+)/(.+)/(.+)\.git"
_GIT=".git"
for k,repoK in enumerate( BgRp.submodules):
    # print(f"{repoK.name}, {repoK.path}, {repoK.url}, {repoK.hexsha}, {repoK.branch_name}, {repoK.branch_path}")
    urlK=repoK.url
    urlK=urlK if urlK.endswith(_GIT) else f"{urlK}{_GIT}"
    urlMatch=re.match(pattern=urlReExpr,string=urlK)
    assert urlMatch is not None,f"断言失败，【{repoK.url}】不匹配正则表达式【{urlReExpr}】【忽略末尾.git】"
    urlFieldLs=urlMatch.groups()
    assert urlFieldLs is not None and len(urlFieldLs) == 3 ,f"断言失败，【{repoK.url}】不匹配正则表达式【{urlReExpr}】【忽略末尾.git】，字段个数不为3，实际字段个数【{len(urlFieldLs)}】"
    host=urlFieldLs[0]
    orgName=urlFieldLs[1]
    repoName=urlFieldLs[2]
    newRepoName=f"{orgName}--{repoName}"
    #import_githubRepo_to_gitee.sh --from_repo https://github.com/pytorch/pytorch.git  --goal_org imagg  --goal_repoPath pytorch--pytorch --goal_repoName pytorch--pytorch  --goal_repoDesc 来源https://github.com/pytorch/pytorch.git
    cmd_import2gitee=f"import_githubRepo_to_gitee.sh --from_repo {urlK}  --goal_org {giteeMirrorOrgName}  --goal_repoPath {newRepoName} --goal_repoName {newRepoName}  --goal_repoDesc 【镜像】{urlK}; sleep {random.randint(_sleepSeconds,_sleepSecEnd)}"
    print(cmd_import2gitee)

_end=True