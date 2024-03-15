#!/usr/bin/env python
# -*- coding: <encoding name> -*-

# 【文件作用】 迁移给定git仓库url到gitea服务

from pathlib import Path
import re
import random

import argparse
import httpx


parser = argparse.ArgumentParser(
prog=f'repoMigrateToGitea.py',
description='【迁移给定git仓库url到gitea服务】')

parser.add_argument('-f', '--from_repo_url',required=True,type=str,help="【父仓库url,常为gitee仓库】",metavar='')
parser.add_argument('-h', '--goal_gitea_host',required=True,type=int,help=f"【目标， gitea主机ip或域名】",metavar='')
parser.add_argument('-k', '--goal_gitea_token',required=True,type=str,help="【目标，调用gitea接口的token】",metavar='')
args=parser.parse_args()


repoUrl:str=args.from_repo_url
giteaHost:str=args.goal_gitea_host
giteaToken:str=args.goal_gitea_token




errMsg=f"断言失败【 sleep_seconds>={MINI_sleep_seconds} 】且【【 sleep_seconds_delta>={MINI_sleep_seconds_delta} 】】"
assert _sleepSeconds >= MINI_sleep_seconds and args.sleep_seconds_delta >= MINI_sleep_seconds_delta, errMsg

#                    //host/mrrOrg/org--repo
urlReExpr=r"http[s]?://(.+)/(.+)/(.+)--(.+)\.git"
_GIT=".git"
repoUrl=repoUrl if repoUrl.endswith(_GIT) else f"{repoUrl}{_GIT}"
urlMatch=re.match(pattern=urlReExpr,string=repoUrl)
assert urlMatch is not None,f"断言失败，【{repoUrl}】不匹配正则表达式【{urlReExpr}】【忽略末尾.git】"
urlFieldLs=urlMatch.groups()
assert urlFieldLs is not None and len(urlFieldLs) == 4 ,f"断言失败，【{repoUrl}】不匹配正则表达式【{urlReExpr}】【忽略末尾.git】，字段个数不为4，实际字段个数【{len(urlFieldLs)}】"
host=urlFieldLs[0]
mirrorOrgName=urlFieldLs[1]
orgName=urlFieldLs[2]
repoName=urlFieldLs[3]


"""
curl -k -X 'POST' \
  'https://github.local/api/v1/repos/migrate?token=b1d490eaf6b88a6c37bd482d8e05e3a0061f066c' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "clone_addr": "https://gitee.com/mirrr/NVlabs--cub.git",
  "repo_name": "cub",
  "repo_owner": "NVlabs"
}'

"""

#https://github.local/api/v1/repos/migrate?token=b1d490eaf6b88a6c37bd482d8e05e3a0061f066c
migrate_url=f'https://{giteaHost}/api/v1/repos/migrate?token={giteaToken}'
reqBodyDct={
    "clone_addr": repoUrl,
  "repo_owner": orgName,
  "repo_name": repoName
}
resp=httpx.post(url=migrate_url,json=reqBodyDct)
msg=f"【gitea迁移接口响应】状态码【{resp.status_code}】，响应文本【{resp.text}】"
if resp.is_success():
    print(f"迁移成功，{msg}")
else :
    print(f"迁移失败，{msg}")

cmd_import2gitee=f"import_githubRepo_to_gitee.sh --from_repo {urlK}  --goal_org {giteeMirrorOrgName}  --goal_repoPath {newRepoName} --goal_repoName {newRepoName}  --goal_repoDesc 【镜像】{urlK}; sleep {random.randint(_sleepSeconds,_sleepSecEnd)}"
print(cmd_import2gitee)

_end=True