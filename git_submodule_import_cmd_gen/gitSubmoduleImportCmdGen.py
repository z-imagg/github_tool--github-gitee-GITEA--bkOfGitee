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
import argparse

MINI_sleep_seconds = 8
MINI_sleep_seconds_delta = 5

parser = argparse.ArgumentParser(
prog=f'gitSubmoduleImportCmdGen.py',
description='【子模块导入命令生成】')

parser.add_argument('-f', '--parent_repo_dir',required=True,type=str,help="【父仓库本地目录,常为gitee仓库】",metavar='')
parser.add_argument('-o', '--goal_org',required=True,type=str,help="【目标，gitee的组织】",metavar='')
parser.add_argument('-s', '--sleep_seconds',required=True,type=int,help=f"【 相邻两个子模块导入命令间休眠秒数】最小【{MINI_sleep_seconds}秒】",metavar='')
parser.add_argument('-t', '--sleep_seconds_delta',required=True,type=int,help=f"【 相邻两个子模块导入命令间休眠秒数随机增量】最小【{MINI_sleep_seconds_delta}秒】",metavar='')
args=parser.parse_args()


# print(sys.argv)
_BgRp:str=args.parent_repo_dir
giteeMirrorOrgName=args.goal_org #"imagg"
_sleepSeconds:str=args.sleep_seconds
_sleepSecEnd:str=args.sleep_seconds+args.sleep_seconds_delta

errMsg=f"断言失败【 sleep_seconds>={MINI_sleep_seconds} 】且【【 sleep_seconds_delta>={MINI_sleep_seconds_delta} 】】"
assert _sleepSeconds >= MINI_sleep_seconds and args.sleep_seconds_delta >= MINI_sleep_seconds_delta, errMsg

BgRp:git.Repo=git.Repo(path=_BgRp)
BgRpRmt:git.Remote=BgRp.remote()
originUrlBgRp:str=BgRpRmt.url
# BgRp_:cmd.Git=BgRp.git

repoK:git.Submodule
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
    cmd_import2gitee=f"import_githubRepo_to_gitee.sh --from_repo {urlK}  --goal_org {giteeMirrorOrgName}  --goal_repoPath {newRepoName} --goal_repoName {newRepoName}  --goal_repoDesc 【镜像】{urlK}; #sleep {random.randint(_sleepSeconds,_sleepSecEnd)}"
    print(cmd_import2gitee)

_end=True