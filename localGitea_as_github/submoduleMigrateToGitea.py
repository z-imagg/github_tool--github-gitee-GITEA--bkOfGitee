#!/usr/bin/env python
# -*- coding: <encoding name> -*-

# 【文件作用】 遍历给定git仓库中的子模块列表， 将子模块url替换为镜像模块url，迁移该镜像url到gitea

# from pathlib import Path
import git
# from git import cmd

import sys
import argparse

#或者 export PYTHONPATH=/fridaAnlzAp/github-gitee-gitea/py_util/
sys.path.append("/fridaAnlzAp/github-gitee-gitea/py_util/")
from GitRepoUrlParser import gitRepoUrlParseF,gitMirrorRepoUrlParseF,GitRepoUrlC

from RepoMigrateToGiteaFunc import giteaMigrateApi

from gitea_api_cfg import gitea_base_url, gitea_token

def submoduleLsMigrateToGitea():

    parser = argparse.ArgumentParser(
    prog=f'submoduleMigrateToGitea.py',
    description='【迁移本地仓库中的子模块们到gitea服务】')

    parser.add_argument('-p', '--from_parent_repo_dir',required=True,type=str,help="【父仓库本地目录,常为gitee仓库】",metavar='')
    parser.add_argument('-b', '--mirror_base_url',required=True,type=str,help="【 镜像基础url】",metavar='')
    parser.add_argument('-o', '--mirror_org_name',required=True,type=str,help="【 镜像组织名】",metavar='')
    args=parser.parse_args()


    # print(sys.argv)
    bigRpPath:str=args.from_parent_repo_dir
    mirrorBaseUrl:str=args.mirror_base_url
    mirrorOrg:str=args.mirror_org_name

    BgRp:git.Repo=git.Repo(path=bigRpPath)
    BgRpRmt:git.Remote=BgRp.remote()
    originUrlBgRp:str=BgRpRmt.url
    # BgRp_:cmd.Git=BgRp.git

    repoK:git.Submodule
    for k,repoK in enumerate( BgRp.submodules):
        # print(f"{repoK.name}, {repoK.path}, {repoK.url}, {repoK.hexsha}, {repoK.branch_name}, {repoK.branch_path}")
        originUrl=gitRepoUrlParseF(repoK.url)
        originUrlTxt=originUrl.url_str()
        # newRepo=f"{originUrl.orgName}--{originUrl.repoName}"
        # mrrRepoUrl=GitRepoUrlC(baseUrl=mirrorBaseUrl, orgName=mirrorOrg,repoName=newRepo)
        # mrrRepoUrlTxt=mrrRepoUrl.url_str()
        
        giteaMigrateApi(originUrlTxt, args.mirror_base_url, args.mirror_org_name, gitea_base_url, gitea_token)

if __name__=="__main__":
    submoduleLsMigrateToGitea()

