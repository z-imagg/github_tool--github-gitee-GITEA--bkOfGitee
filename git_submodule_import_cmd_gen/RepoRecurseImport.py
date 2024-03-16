#!/usr/bin/env python
# -*- coding: <encoding name> -*-

# 【文件作用】 遍历给定git仓库中的子模块列表， 并打印对应命令import_githubRepo_to_gitee.sh

from pathlib import Path
import git
from git import cmd
import shutil
import re
import random
import time

import sys
import argparse
sys.path.append("/fridaAnlzAp/github-gitee-gitea/py_util/")
from GitPyCloneProgress import GitPyCloneProgressC
from gitee_import_repo_wrap import gitee_import_repo_wrap_F,SimpleRespI
from GitRepoUrlParser import gitRepoUrlParseF,GitRepoUrlC
from LoopCloneWait import loop_clone_wait_F

MINI_sleep_seconds = 8
MINI_sleep_seconds_delta = 5

def main_cmd():
    parser = argparse.ArgumentParser(
    prog=f'gitSubmoduleImportCmdGen.py',
    description='【子模块导入命令生成】')

    parser.add_argument('-f', '--from_repo_url',required=True,type=str,help="【父仓库url,常为gitee仓库】",metavar='')
    parser.add_argument('-o', '--goal_org',required=True,type=str,help="【目标，gitee的组织】",metavar='')
    parser.add_argument('-s', '--sleep_seconds',required=True,type=int,help=f"【 相邻两个子模块导入命令间休眠秒数】 ",metavar='')
    args=parser.parse_args()


    importGithubRepo2GiteeRecurse(from_repo_url=args.from_repo_url,giteeMirrOrg=args.goal_org,sleep_seconds=args.sleep_seconds)

def importGithubRepo2GiteeRecurse(from_repo_url:str,giteeMirrOrg:str,sleep_seconds:int=2):
    assert from_repo_url.startswith("https://github.com"), "断言失败，只允许github.com的仓库导入到gitee"
    repoUrlO:GitRepoUrlC=gitRepoUrlParseF(repoUrl=from_repo_url)

    newRepoName=f"{repoUrlO.orgName}--{repoUrlO.repoName}"
    simpleRespI:SimpleRespI=gitee_import_repo_wrap_F(fromRepoUrl=from_repo_url,mirrOrg=giteeMirrOrg,newRepoName=newRepoName)
    time.sleep(sleep_seconds); print(f"调用gitee的接口后休眠2秒,【{simpleRespI.goal_repoUrl}】---> 【{simpleRespI.url}】")
    mirrRepoUrl:str=simpleRespI.goal_repoUrl

    #以 循环克隆仓库 等待 gitee导入仓库任务 完毕
    repo:git.Repo=loop_clone_wait_F(repoUrl=mirrRepoUrl)

    #递归子仓库
    for k,sonRepoK in enumerate( repo.submodules):
        # print(f"{repoK.name}, {repoK.path}, {repoK.url}, {repoK.hexsha}, {repoK.branch_name}, {repoK.branch_path}")
        importGithubRepo2GiteeRecurse(sonRepoK.url)

if __name__=="__main__":
    main_cmd()