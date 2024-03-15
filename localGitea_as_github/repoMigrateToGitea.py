#!/usr/bin/env python
# -*- coding: <encoding name> -*-

# 【文件作用】 【RepoMigrateToGiteaFunc.py 即 "迁移给定git仓库url到gitea服务" 】 的命令行包装

import argparse

from  RepoMigrateToGiteaFunc import giteaMigrateApi
from gitea_api_cfg import gitea_base_url, gitea_token


def giteaMigrateApiCmd():
    parser = argparse.ArgumentParser(
    prog=f'repoMigrateToGitea.py',
    description='【迁移给定git仓库url到gitea服务】')

    parser.add_argument('-f', '--from_repo_url',required=True,type=str,help="【父仓库url,常为gitee仓库】",metavar='')
    parser.add_argument('-m', '--mirror_base_url',required=True,type=str,help="【 镜像基础url】",metavar='')
    parser.add_argument('-n', '--mirror_org_name',required=True,type=str,help="【 镜像组织名】",metavar='')
    args=parser.parse_args()


    giteaMigrateApi(args.from_repo_url, args.mirror_base_url, args.mirror_org_name, gitea_base_url, gitea_token)


if __name__=="__main__":
    giteaMigrateApiCmd()