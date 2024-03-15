#!/usr/bin/env python
# -*- coding: <encoding name> -*-

# 【文件作用】 【RepoMigrateToGiteaFunc.py 即 "迁移给定git仓库url到gitea服务" 】 的命令行包装

import argparse

from  RepoMigrateToGiteaFunc import giteaMigrateApi
from gitea_api_cfg import gitea_host, gitea_port, gitea_token

parser = argparse.ArgumentParser(
prog=f'repoMigrateToGitea.py',
description='【迁移给定git仓库url到gitea服务】')

parser.add_argument('-f', '--from_repo_url',required=True,type=str,help="【父仓库url,常为gitee仓库】",metavar='')
args=parser.parse_args()


giteaMigrateApi(args.from_repo_url, gitea_host,gitea_port, gitea_token)