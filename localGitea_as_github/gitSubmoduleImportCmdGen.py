#!/usr/bin/env python
# -*- coding: <encoding name> -*-

# 【文件作用】 遍历给定git仓库中的子模块列表， 将子模块url替换为镜像模块url，迁移该镜像url到gitea

# from pathlib import Path
import git
# from git import cmd

import sys
import argparse

from GitRepoUrlParser import gitRepoUrlParseF,gitMirrorRepoUrlParseF,GitRepoUrlC
from RepoMigrateToGiteaFunc import giteaMigrateApi

from gitea_api_cfg import gitea_base_url, gitea_token

MINI_sleep_seconds = 8
MINI_sleep_seconds_delta = 5

parser = argparse.ArgumentParser(
prog=f'gitSubmoduleImportCmdGen.py',
description='【子模块导入命令生成】')

parser.add_argument('-f', '--parent_repo_dir',required=True,type=str,help="【父仓库本地目录,常为gitee仓库】",metavar='')
parser.add_argument('-m', '--mirror_org_name',required=True,type=str,help="【 】",metavar='')
args=parser.parse_args()


# print(sys.argv)
_BgRp:str=args.parent_repo_dir
mirrorOrgName:str=args.mirror_org_name

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
    url_k=gitRepoUrlParseF(repoK.url)
    newRepoName=f"{url_k.orgName}--{url_k.repoName}"
    mirror_repo_url=GitRepoUrlC(host="gitee.com", orgName=mirrorOrgName,repoName=newRepoName)
    
    giteaMigrateApi(mirror_repo_url.url_str(), gitea_base_url, gitea_token)

_end=True

