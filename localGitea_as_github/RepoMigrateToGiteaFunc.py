#!/usr/bin/env python
# -*- coding: <encoding name> -*-

# 【文件作用】 迁移给定git仓库url到gitea服务

from pathlib import Path
import re

import httpx

import sys
sys.path.append("/fridaAnlzAp/github-gitee-gitea/py_util/")

from GitRepoUrlParser import gitMirrorRepoUrlParseF

def giteaMigrateApi(repoUrl:str,giteaBaseUrl:str,giteaToken:str):
  repo_url=gitMirrorRepoUrlParseF(repoUrl)


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
  migrate_url=f'{giteaBaseUrl}/api/v1/repos/migrate?token={giteaToken}'
  reqBodyDct={
      "clone_addr": repoUrl,
    "repo_owner": repo_url.orgName,
    "repo_name": repo_url.repoName
  }
  resp=httpx.post(url=migrate_url,json=reqBodyDct)
  msg=f"【gitea迁移接口响应】状态码【{resp.status_code}】，响应文本【{resp.text}】"
  ok= resp.is_success()
  msg=f'{"迁移成功" if ok else "迁移失败" }，{msg}'
  print(msg)
  return ok