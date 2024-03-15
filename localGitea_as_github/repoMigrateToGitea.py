#!/usr/bin/env python
# -*- coding: <encoding name> -*-

# 【文件作用】 【RepoMigrateToGiteaFunc.py 即 "迁移给定git仓库url到gitea服务" 】 的命令行包装

import argparse

from  RepoMigrateToGiteaFunc import giteaMigrateApi

parser = argparse.ArgumentParser(
prog=f'repoMigrateToGitea.py',
description='【迁移给定git仓库url到gitea服务】')

parser.add_argument('-f', '--from_repo_url',required=True,type=str,help="【父仓库url,常为gitee仓库】",metavar='')
parser.add_argument('-h', '--goal_gitea_host',required=True,type=int,help=f"【目标， gitea主机ip或域名】",metavar='')
parser.add_argument('-k', '--goal_gitea_token',required=True,type=str,help="【目标，调用gitea接口的token】",metavar='')
args=parser.parse_args()


giteaMigrateApi(args.from_repo_url, args.goal_gitea_host, args.goal_gitea_token)