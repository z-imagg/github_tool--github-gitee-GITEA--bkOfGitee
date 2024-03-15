#!/usr/bin/env python
# -*- coding: <encoding name> -*-

# 【文件作用】 迁移给定git仓库url到gitea服务

from pathlib import Path
import re

import httpx


def giteaMigrateApiCall(from_repo_url:str,goal_gitea_host:str,goal_gitea_token:str):
  repoUrl:str=from_repo_url
  giteaHost:str=goal_gitea_host
  giteaToken:str=goal_gitea_token

  #                    //host/mrrOrg/org--repo
  urlReExpr=r"http[s]?://(.+)/(.+)/(.+)--(.+)\.git"
  _GIT=".git"
  repoUrl=repoUrl if repoUrl.endswith(_GIT) else f"{repoUrl}{_GIT}"
  urlMatch=re.match(pattern=urlReExpr,string=repoUrl)
  assert urlMatch is not None,f"断言失败，【{repoUrl}】不匹配正则表达式【{urlReExpr}】【忽略末尾.git】"
  urlFieldLs=urlMatch.groups()
  assert urlFieldLs is not None and len(urlFieldLs) == 4 ,f"断言失败，【{repoUrl}】不匹配正则表达式【{urlReExpr}】【忽略末尾.git】，字段个数不为4，实际字段个数【{len(urlFieldLs)}】"
  giteaHost=urlFieldLs[0]
  _mirrorOrgName=urlFieldLs[1]
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
  ok= resp.is_success()
  msg=f'{"迁移成功" if ok else "迁移失败" }，{msg}'
  print(msg)
  return ok