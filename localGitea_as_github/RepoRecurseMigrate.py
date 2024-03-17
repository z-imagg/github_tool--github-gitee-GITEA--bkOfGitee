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

from git_submodule_import_cmd_gen.RepoRecurseImport import printFrmRepoMsg
sys.path.append("/fridaAnlzAp/github-gitee-gitea/py_util/")
from GitPyCloneProgress import GitPyCloneProgressC
from gitee_import_repo_wrap import gitee_import_repo_wrap_F,SimpleRespI
from GitRepoUrlParser import gitRepoUrlParseF,GitRepoUrlC
from LoopCloneWait import loop_clone_wait_F
from RandomUtil import randSecs
from SleepUtil import sleepVerbose
from MiscUtil import fullUrl
from CntUtil import Counter
from  RepoMigrateToGiteaFunc import giteaMigrateApi
from gitea_api_cfg import api_base_url, api_token

cntr:Counter=Counter()
MINI_sleep_seconds = 8

def main_cmd():
    parser = argparse.ArgumentParser(
    prog=f'gitSubmoduleImportCmdGen.py',
    description='【递归迁移仓库】【镜像gitee--->本地GITEA】')

    parser.add_argument('-f', '--from_repo_url',required=True,type=str,help="【父仓库url,常为gitee仓库】",metavar='')
    parser.add_argument('-c', '--from_commit_id',required=True,type=str,help="【看父仓库的commitId】",metavar='')
    parser.add_argument('-m', '--mirror_base_url',required=True,type=str,help="【 镜像基础url】",metavar='')
    parser.add_argument('-n', '--mirror_org_name',required=True,type=str,help="【 镜像组织名】",metavar='')
    parser.add_argument('-s', '--sleep_seconds',required=True,type=int,help=f"【 相邻两个子模块导入命令间休眠秒数】 ",metavar='')
    args=parser.parse_args()


    migrateRecurse(ornRUrl=args.from_repo_url, ornCmtId=args.from_commit_id, frmBaseUrl=args.mirror_base_url, frmOrgNm=args.mirror_org_name, slpSecs=args.sleep_seconds)

def migrateRecurse(ornRUrl:str, ornCmtId:str, frmBaseUrl:str, frmOrgNm:str, slpSecs:int=2):
    assert ornRUrl.startswith("https://github.com") and frmBaseUrl.startswith("https://gitee.com") , "断言失败，只允许github.com、gitee.com做迁移到本地gitea服务"
    repoUrlO:GitRepoUrlC=gitRepoUrlParseF(repoUrl=ornRUrl)

    #1. 调用本地GITEA服务的迁移接口
    frmRUrlO:GitRepoUrlC
    ok_mgr,frmRUrlO,localRUrl=giteaMigrateApi(ornRUrl, frmBaseUrl, frmOrgNm)
    assert ok_mgr==True and frmRUrlO is not None,"断言4"
    mrrRpoUrl:str=frmRUrlO.url_str()
    sleepVerbose(slpSecs,"#"); print(f"调用本地GITEA服务的迁移接口 【{mrrRpoUrl}】---> 本地GITEA服务的 【{localRUrl}】")

    #2. 克隆仓库
    #   以 循环克隆仓库 等待 GITEA迁移仓库 完毕
    repo:git.Repo=loop_clone_wait_F(repoUrl=localRUrl)
    #重置到给定commitId
    repo.git.checkout(ornCmtId)

    # 打印该仓库消息
    printFrmRepoMsg(ornRUrl,ornCmtId,repo,cntr)
    
    #3. 递归子仓库
    for k,sonRpo in enumerate( repo.submodules):
        sonUrl:str=fullUrl(ornRUrl,sonRpo.url)
        # print(f"{repoK.name}, {repoK.path}, {repoK.url}, {repoK.hexsha}, {repoK.branch_name}, {repoK.branch_path}")
        migrateRecurse(sonUrl, sonRpo.hexsha, frmBaseUrl, randSecs(slpSecs))

if __name__=="__main__":
    main_cmd()