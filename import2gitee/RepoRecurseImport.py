#!/usr/bin/env python
# -*- coding: utf8 -*-

# 【文件作用】 遍历给定git仓库中的子模块列表， 并打印对应命令import_githubRepo_to_gitee.sh

import sys
sys.path.append("/app/github-gitee-GITEA/py_util/")


from global_var import GlbVar
from pathlib import Path
import git
from git import cmd
import shutil
import re
import random
import time

import argparse

from HostUtil import hasLocalGithubDomain

from GitPyCloneProgress import GitPyCloneProgressC
from gitee_import_repo_wrap import gitee_import_repo_wrap_F,SimpleRespI
from GitRepoUrlParser import gitRepoUrlParseF,GitRepoUrlC
from LoopCloneWait import loop_clone_wait_F
from RandomUtil import randSecs
from SleepUtil import sleepVerbose
from MiscUtil import fullUrl, isEmptyStr, firstLine
from CntUtil import Counter
from DirUtil import getScriptDir
from GitPyUtil import tagNameLsByCmtId,printFrmRepoMsg

cntr:Counter=Counter()
MINI_sleep_seconds = 8


def main_cmd():
    parser = argparse.ArgumentParser(
    prog=f'gitSubmoduleImportCmdGen.py',
    description='【子模块导入命令生成】')

    parser.add_argument('-f', '--from_repo_url',required=True,type=str,help="【父仓库url,常为gitee仓库】",metavar='')
    parser.add_argument('-c', '--from_commit_id',required=False,type=str,help="【父仓库的commitId】『可选』",metavar='')
    parser.add_argument('-o', '--goal_org',required=True,type=str,help="【目标，gitee的组织】",metavar='')
    parser.add_argument('-s', '--sleep_seconds',required=True,type=int,help=f"【 相邻两个子模块导入命令间休眠秒数】 ",metavar='')
    args=parser.parse_args()

    print(":")

    scriptDir:Path=getScriptDir()
    #scriptDir==/app/github-gitee-GITEA/import2gitee/
    prjHmDir:str=f"{scriptDir.parent.absolute()}"
    #prjHmDir==/app/github-gitee-GITEA/

    importGithubRepo2GiteeRecurse(prjHmDir=prjHmDir, from_repo_url=args.from_repo_url,from_commit_id=args.from_commit_id,giteeMirrOrg=args.goal_org,sleep_seconds=args.sleep_seconds)

def importGithubRepo2GiteeRecurse(prjHmDir:str, from_repo_url:str,from_commit_id:str,giteeMirrOrg:str,sleep_seconds:int=2):
    assert not hasLocalGithubDomain(), f"断言失败，导入步不要在本地解析域名github.com，请将文件【/etc/hosts】中的github.com解析行删除或注释掉。（本断言的目的是防止混淆，导入步允许 本地解析域名github.com）"
    assert from_repo_url.startswith("https://github.com"), f"断言失败，只允许github.com的仓库导入到gitee. from_repo_url=【{from_repo_url}】"
    repoUrlO:GitRepoUrlC=gitRepoUrlParseF(repoUrl=from_repo_url)

    #1. 调用gitee导入接口
    newRepoName=f"{repoUrlO.orgName}--{repoUrlO.repoName}"
    simpleRespI,respFP=gitee_import_repo_wrap_F(prjHmDir,fromRepoUrl=from_repo_url,mirrOrg=giteeMirrOrg,newRepoName=newRepoName)
    print(f"已接口导入【{from_repo_url}】---> 【{simpleRespI.goal_repoUrl}】; respBodyLen=【{len(simpleRespI.reqBody)}】; respFP=【{respFP}】")
    sleepVerbose(sleep_seconds,"接口导入后休眠"); 

    mirrRepoUrl:str=simpleRespI.goal_repoUrl

    #2. 克隆仓库
    #   以 循环克隆仓库 等待 gitee导入仓库任务 完毕
    repo:git.Repo=loop_clone_wait_F(repoUrl=mirrRepoUrl,title="导入确认中")
    
    # 若指定了cmtId, 则 重置到给定commitId
    if not isEmptyStr (from_commit_id):
        repo.git.checkout(from_commit_id)
    else:
    # 否则，用头的cmtId
        from_commit_id = repo.head.commit.hexsha
    
    # 打印该仓库消息
    printFrmRepoMsg(from_repo_url,from_commit_id,repo,cntr)
    
    #3. 递归子仓库
    for k,sonRepoK in enumerate( repo.submodules):
        sonUrl:str=fullUrl(from_repo_url,sonRepoK.url)
        # print(f"{repoK.name}, {repoK.path}, {repoK.url}, {repoK.hexsha}, {repoK.branch_name}, {repoK.branch_path}")
        importGithubRepo2GiteeRecurse(prjHmDir, sonUrl, sonRepoK.hexsha, giteeMirrOrg, randSecs(sleep_seconds))

if __name__=="__main__":
    GlbVar(66)
    main_cmd()