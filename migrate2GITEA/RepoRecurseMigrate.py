#!/usr/bin/env python
# -*- coding: utf8 -*-

# 【文件作用】  
# 【术语】CmtId == CommitId == 提交Id  == git的某次提交的数字签名 , localRUrl == localRepoUrl == 本地GITEE仓库Url

import sys

sys.path.append("/fridaAnlzAp/github-gitee-GITEA/py_util/")

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
from GitRepoUrlParser import gitRepoUrlParseF,GitRepoUrlC
from LoopCloneWait import loop_clone_wait_F
from RandomUtil import randSecs
from SleepUtil import sleepVerbose
from MiscUtil import fullUrl,isEmptyStr
from CntUtil import Counter
from  RepoMigrateToGiteaFunc import giteaMigrateApi
from GitPyUtil import printFrmRepoMsg

cntr:Counter=Counter()

def main_cmd():
    parser = argparse.ArgumentParser(
    prog=f'gitSubmoduleImportCmdGen.py',
    description='【递归迁移仓库】【镜像gitee--->本地GITEA】')

    parser.add_argument('-f', '--from_repo_url',required=True,type=str,help="【父仓库url,常为gitee仓库】",metavar='')
    parser.add_argument('-c', '--from_commit_id',required=False,type=str,help="【看父仓库的commitId】",metavar='')
    parser.add_argument('-m', '--mirror_base_url',required=True,type=str,help="【 镜像基础url】",metavar='')
    parser.add_argument('-n', '--mirror_org_name',required=True,type=str,help="【 镜像组织名】",metavar='')
    parser.add_argument('-s', '--sleep_seconds',required=True,type=int,help=f"【 相邻两个子模块导入命令间休眠秒数】 ",metavar='')
    args=parser.parse_args()
    
    print(":")
    migrateRecurse(ornRUrl=args.from_repo_url, ornCmtId=args.from_commit_id, frmBaseUrl=args.mirror_base_url, frmOrgNm=args.mirror_org_name, slpSecs=args.sleep_seconds)

def migrateRecurse(ornRUrl:str, ornCmtId:str, frmBaseUrl:str, frmOrgNm:str, slpSecs:int=2):
    assert hasLocalGithubDomain(), f"断言失败，迁移步要在本地解析域名github.com，请在文件【/etc/hosts】中添加一行将github.com解析到本地GITEA服务IP"
    assert ornRUrl.startswith("https://github.com") and frmBaseUrl.startswith("https://gitee.com") , "断言失败，只允许github.com、gitee.com做迁移到本地gitea服务"
    repoUrlO:GitRepoUrlC=gitRepoUrlParseF(repoUrl=ornRUrl)

    #1. 调用本地GITEA服务的迁移接口
    frmRUrlO:GitRepoUrlC
    ok_mgr,frmRUrlO,localRUrl=giteaMigrateApi(ornRUrl, frmBaseUrl, frmOrgNm)
    assert ok_mgr==True and frmRUrlO is not None,f"断言失败，GITEA迁移接口失败， ornRUrl=【{ornRUrl}】, frmBaseUrl=【{frmBaseUrl}】, frmOrgNm=【{frmOrgNm}】"
    mrrRpoUrl:str=frmRUrlO.url_str()
    sleepVerbose(slpSecs,"迁移后休眠")
    # print(f"已迁移 【{mrrRpoUrl}】---> 本地GITEA 【{localRUrl}】") 

    #2. 克隆仓库
    #   以 循环克隆仓库 等待 GITEA迁移仓库 完毕
    repo:git.Repo=loop_clone_wait_F(repoUrl=localRUrl,title="休眠等待迁移完成后克隆")
    # 若指定了cmtId, 则 重置到给定commitId
    if not isEmptyStr (ornCmtId):
        repo.git.checkout(ornCmtId)
    else:
    # 否则，用头的cmtId
        ornCmtId = repo.head.commit.hexsha

    # 打印该仓库消息
    printFrmRepoMsg(ornRUrl,ornCmtId,repo,cntr)
    
    #3. 递归子仓库
    for k,sonRpo in enumerate( repo.submodules):
        sonUrl:str=fullUrl(ornRUrl,sonRpo.url)
        # print(f"{repoK.name}, {repoK.path}, {repoK.url}, {repoK.hexsha}, {repoK.branch_name}, {repoK.branch_path}")
        migrateRecurse(sonUrl, sonRpo.hexsha, frmBaseUrl, frmOrgNm, randSecs(slpSecs))

if __name__=="__main__":
    main_cmd( )