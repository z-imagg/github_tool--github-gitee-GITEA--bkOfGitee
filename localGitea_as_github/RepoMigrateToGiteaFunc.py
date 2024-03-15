#!/usr/bin/env python
# -*- coding: <encoding name> -*-

# 【文件作用】 迁移给定git仓库url到gitea服务

from pathlib import Path
import re

import httpx

import sys
sys.path.append("/fridaAnlzAp/github-gitee-gitea/py_util/")

from GitRepoUrlParser import gitMirrorRepoUrlParseF,gitRepoUrlParseF

def giteaMigrateApi(originRpoUrlTxt:str,mirrorBaseUrl,mirrorOrg,giteaBaseUrl:str,giteaToken:str):
  originRpoUrl=gitRepoUrlParseF(originRpoUrlTxt)

  """
  curl -X 'POST' \
  'https://github.local/api/v1/orgs?token=ab2a90dc37210a4f9aee91ab959bfa3fc1f6ba6a' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "NVlabs",
  "repo_admin_change_team_access": true,
  "visibility": "public"
}'
"""

  apiUrl_newOrg=f'{giteaBaseUrl}/api/v1/orgs?token={giteaToken}'
  reqBdy_newOrg={
    "username": originRpoUrl.orgName,
  }
  resp_newOrg=httpx.post(url=apiUrl_newOrg,json=reqBdy_newOrg,verify=False)
  ok_newOrg=resp_newOrg.status_code==422 or resp_newOrg.is_success #422 gitea 已经存在组织
  if(not ok_newOrg):
    msg_newOrg=f"创建gitea组织失败，【${resp_newOrg.status_code}, ${resp_newOrg.text}】"
    print(msg_newOrg)
    return False
  

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

  mirrRepoUrl=originRpoUrl.to_mirror_url(mirrorBaseUrl,mirrorOrg)
  mirrRpoUrlTxt:str = mirrRepoUrl.url_str()
  apiUrl_migrate=f'{giteaBaseUrl}/api/v1/repos/migrate?token={giteaToken}'
  reqBdy_migrate={
      "clone_addr": mirrRpoUrlTxt,
    "repo_owner": originRpoUrl.orgName,
    "repo_name": originRpoUrl.repoName
  }
  resp_migrate=httpx.post(url=apiUrl_migrate,json=reqBdy_migrate,verify=False,timeout=120)
  msg_migrate=f"【gitea迁移接口响应】状态码【{resp_migrate.status_code}】，响应文本【{resp_migrate.text}】\n 【迁移仓库】【{originRpoUrlTxt}】--->【{mirrRpoUrlTxt}】"
  ok_migrate= resp_migrate.status_code == 409 or resp_migrate.is_success #409 gitea 已经存在仓库
  msg_migrate=f'{"迁移成功" if ok_migrate else "迁移失败" }，{msg_migrate}'
  print(msg_migrate)
  return ok_migrate